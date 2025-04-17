#!/usr/bin/python3

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import lime.lime_tabular

import lime.lime_tabular, shap, dice_ml 

import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import dice_ml

# from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_classification

def shap_xai(model_evaluation_list):
    model, X_test, y_test, model_name = model_evaluation_list
    explainer = None
    if model_name == "Linear Regression":
        explainer = shap.LinearExplainer(model, X_test)
    if model_name == "Random Forest":
        explainer = shap.TreeExplainer(model)
    if model_name == "Gradient Boost":
        explainer = shap.TreeExplainer(model)
        
    # Compute contriution of each feature to the models prediction
    shap_values = explainer.shap_values(X_test)
    # feature_names = [f'Feature_{i}' for i in range(X_test.shape[1])]
    feature_names = [
    "RevUtil",      # RevolvingUtilizationOfUnsecuredLines
    "Age",          # age
    "PastDue30_59", # NumberOfTime30-59DaysPastDueNotWorse
    "DebtRatio",    # DebtRatio
    "Income",       # MonthlyIncome
    "OpenCredits",  # NumberOfOpenCreditLinesAndLoans
    "Late90",       # NumberOfTimes90DaysLate
    "RELoans",      # NumberRealEstateLoansOrLines
    "PastDue60_89", # NumberOfTime60-89DaysPastDueNotWorse
    "Dependents"    # NumberOfDependents
]
    df_original = pd.read_csv('cs-training.csv')
    feature_names = df_original.columns[:-1].tolist()
    
    # X_train = pd.DataFrame(X_train, columns=feature_names)
    X_test = pd.DataFrame(X_test, columns=feature_names)
    # Visualize Feature importance
    shap.summary_plot(shap_values, X_test, feature_names=X_test.columns)
    
def lime_xai(model_evaluation_list):
    # Unpack the model and test data.
    model, X_test, y_test, model_name = model_evaluation_list

    # Load feature names from the original dataset.
    df_original = pd.read_csv('cs-training.csv')
    feature_names = df_original.columns[:-1].tolist()  # Exclude the target column

    # Convert test data to NumPy array (LIME requires it)
    X_test = np.array(X_test)

    # Initialize the LIME explainer.
    explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=X_test, 
        feature_names=feature_names,  # Use actual feature names
        mode="classification"
    )

    # Select the first instance from X_test.
    instance = X_test[0]

    print("**********************************************")

    # Generate the LIME explanation for the selected instance.
    exp = explainer.explain_instance(
        instance,            # Instance to explain.
        model.predict_proba, # Function to get model's probability predictions.
        num_features=len(feature_names)       # Number of features to display in the explanation.
    )

    # Get the predicted class from the explanation.
    predicted_class = np.argmax(exp.predict_proba)

    # Print explanation details.
    print("-------------------LIME----------------------------------")
    print(f"\nLIME text explanation for {model_name}")
    print("Predicted class:", predicted_class)
    print("Predicted probabilities:", exp.predict_proba)

    print("\nFeature contributions (feature importance):")
    for feature, weight in exp.as_list():
        print(f"{feature}: {weight:.2f}")

    # --- Modify the Plot to Display Feature Names on the y-axis ---
    fig = exp.as_pyplot_figure()
    ax = fig.gca()
    plt.subplots_adjust(left=0.35)

    # Get explanation feature names from LIME
    explanation_list = exp.as_list()
    feature_labels = [item[0] for item in explanation_list]  # Get feature labels
    
    # Set y-axis labels correctly
    ax.set_yticks(range(len(feature_labels)))
    ax.set_yticklabels(feature_labels)
    
    plt.show()

    # # To have more control over the visuslization use this Create a Matplotlib visualization
    # explanation_data = exp.as_list()  # Get explanation as a list of (feature, weight) tuples
    # plt.figure(figsize=(10, 6))  # Set figure size
    # features, weights = zip(*explanation_data)  # Unpack features and weights
    # colors = ['green' if w > 0 else 'red' for w in weights]  # Color code positive/negative contributions
    # # Plot the feature weights
    # plt.barh(features, weights, color=colors)
    # plt.xlabel('Weight (Contribution to Prediction)')  # Label for x-axis
    # plt.ylabel('Features')  # Label for y-axis
    # plt.title('LIME Explanation for Instance Prediction')  # Title of the plot
    # plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add gridlines for better readability
    # # Show the plot
    # plt.tight_layout()
    # plt.show()


def model_evaluation(model_evaluation_list):
    #model_evaluation_list = [linear_regression(X_train, y_train), X_test, y_test, "Linear Regression"]
    model, X_test, y_test, model_name = model_evaluation_list
    result = {}
    
    # Start testing and Evaluation
    model_predicted = model.predict(X_test)
    model_predicted_prob = model.predict_proba(X_test)[:, 1]  # Get predicted probabilities for ROC-AUC

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, model_predicted)
    F1_score = f1_score(y_test, model_predicted)
    Precision_score = precision_score(y_test, model_predicted)
    Recall_score = recall_score(y_test, model_predicted)
    
    Roc_auc_score = roc_auc_score(y_test, model_predicted_prob)
    result["model_name"] = f"{model_name}"
    result["accuracy"] = accuracy
    result["f1_score"] = F1_score
    result["precision_score"] = Precision_score
    result["recall_score"] = Recall_score
    result["roc_auc_score"] = Roc_auc_score
    return result
    
def linear_regression(X_train, y_train):
    """
    train and test dataset using linear regression learning model
    X_train: training data
    y_train: target data
    """
    result = []
    # Chose Model
    lgr_model = LogisticRegression(max_iter=500)
    # Start Training
    lgr_model.fit(X_train, y_train)
    return lgr_model

def random_forest(X_train, y_train):
    """
    Train and test dataset using Random Forest learning model
    X_train: training data
    y_train: target data
    """
    # Chose Model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42) #n_estiators = number of trees, randome_state = for reprocuction
    # Start Training
    rf_model.fit(X_train, y_train)
    return rf_model  # This is the trained model
    
def gradient_boost(X_train, y_train):
    """
    Train and test dataset using Gradient Boosting learning model
    X_train: training data
    y_train: target data
    """
    # Chose Model
    gb_model = XGBClassifier(eval_metric="logloss") #
    # Start Training
    gb_model.fit(X_train, y_train)
    # Start Testing
    return gb_model

if __name__ == "__main__":
    print("Thomas kitaba")
   

    # --- Use CSV Data Only ---
    df = pd.read_csv('cs-training.csv')

    # Separate features and labels
    X = df.iloc[:, :-1]  # All columns except the last one are features
    y = df.iloc[:, -1]   # The last column is the target label

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the data (to avoid convergence issues)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    #initialize an empty list to hold the three trained models
    model_evaluation_list = []
    
    # Train model using Linear Regression
    model_evaluation_list.append([linear_regression(X_train, y_train), X_test, y_test, "Linear Regression"]) # recive only model name

    # Train Model Using Randome Forest
    model_evaluation_list.append([random_forest(X_train, y_train), X_test, y_test, "Random Forest"]) # recive only model name
    
    # Train model using Gradient boost
    model_evaluation_list.append([gradient_boost(X_train, y_train), X_test, y_test, "Gradient Boost"])
    
    for model in model_evaluation_list:
        model_evaluation_results = model_evaluation(model)
        # print("-------------------Evaluation Matric----------------------------------")
        print(model_evaluation_results)
        # shap_xai(model)
        # lime_xai(model)
        
        print("===========================================")
        
    
