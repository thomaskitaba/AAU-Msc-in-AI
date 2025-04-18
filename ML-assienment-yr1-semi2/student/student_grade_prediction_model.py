#!/usr/bin/python3

# Title: "Student Performance Prediction using Logistic Regression, Random Forest, and XGBoost with LIME and SHAP for Explainable AI (XAI)"

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
import shap
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# ----------------------------
# STEP-1: Load and preprocess dataset
# ----------------------------

df = pd.read_csv("student-mat.csv", sep=";")

# Convert target to binary classification: Pass (>=10) or Fail (<10)
df['G3'] = df['G3'].apply(lambda x: 1 if x >= 10 else 0)

# Check for duplicates and drop them
if df.duplicated().sum() > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates removed")

# Separate features and label
X = df.drop(columns=["G3"])
y = df["G3"]

# One-hot encode categorical features
X = pd.get_dummies(X, drop_first=True)
feature_names = X.columns.tolist()

# Impute missing values (if any)
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = pd.DataFrame(X_train, columns=feature_names)
X_test = pd.DataFrame(X_test, columns=feature_names)

# ----------------------------
# Train models
# ----------------------------

def train_models():
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "XGBoost": XGBClassifier(eval_metric="logloss", use_label_encoder=False)
    }

    trained = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained[name] = model
    return trained

# ----------------------------
# Evaluate models
# ----------------------------

def evaluate_model(model, name):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print(f"--- {name} ---")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))
    print("ROC AUC Score:", roc_auc_score(y_test, y_proba))
    print()

# ----------------------------
# LIME Explanation
# ----------------------------

def lime_explanation(model, name):
    explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=np.array(X_train),
        feature_names=X.columns.tolist(),
        class_names=["Fail", "Pass"],
        mode="classification"
    )

    exp = explainer.explain_instance(X_test.iloc[0], model.predict_proba, num_features=10)

    print(f"\nLIME explanation for {name}:")
    fig = exp.as_pyplot_figure()
    plt.title(f"LIME Explanation - {name}", fontsize=14)
    plt.tight_layout()
    plt.show()

# ----------------------------
# SHAP Explanation
# ----------------------------

def shap_explanation(model, name):
    if name != "Random Forest":
        print(f"\nSHAP explanation for {name}")
        explainer = shap.Explainer(model, X_train)
        shap_values = explainer(X_test, check_additivity=False) if isinstance(model, (RandomForestClassifier, XGBClassifier)) else explainer(X_test)

        plt.figure()
        if len(shap_values.values.shape) == 3:
            shap.plots.waterfall(shap_values[0, 1], show=False)
        else:
            shap.plots.waterfall(shap_values[0], show=False)
        
        plt.title(f"SHAP Explanation - {name}", fontsize=14)
        plt.tight_layout()
        plt.show()

# ----------------------------
# Run Everything
# ----------------------------

if __name__ == "__main__":
    print("📊 Training models on student-mat.csv...")

    trained_models = train_models()

    for name, model in trained_models.items():
        evaluate_model(model, name)
        lime_explanation(model, name)
        shap_explanation(model, name)
