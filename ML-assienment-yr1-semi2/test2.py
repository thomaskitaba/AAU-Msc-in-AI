#!/usr/bin/python3
# Title: Concrete Compressive Strength Prediction with Gradient Boosting, SVR, and MLP + XAI (LIME & SHAP)

# ----------------------------------------
# Import necessary libraries
# ----------------------------------------
import pandas as pd
import numpy as np
import os

# Models
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Evaluation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Explainability
import lime.lime_tabular
import shap

# Visualization
import matplotlib
matplotlib.use('TkAgg')  # Ensures better plotting outside notebooks
import matplotlib.pyplot as plt

# Suppress warnings
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# ----------------------------------------
# STEP 1: Load and Prepare Data
# ----------------------------------------
data = pd.read_csv("Concret_data/Concrete_Data.csv")
data.columns = data.columns.str.strip().str.replace('"', '')  # Clean column names
print("📋 Cleaned Columns:", data.columns.tolist())

# Features and target
X = data.drop(columns=["Concrete compressive strength(MPa, megapascals)"])
y = data["Concrete compressive strength(MPa, megapascals)"]

# Save unscaled versions for explainability
X_train_df, X_test_df, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standard scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train_df)
X_test = scaler.transform(X_test_df)

# ----------------------------------------
# STEP 2: Define and Train Models
# ----------------------------------------
models = {
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42),
    "Support Vector Regressor": SVR(kernel='rbf', C=100, epsilon=0.2),
    "MLP Regressor": MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', max_iter=1000, random_state=42)
}

trained_models = {}

for name, model in models.items():
    print(f"🚀 Training {name}...")
    model.fit(X_train, y_train)
    trained_models[name] = model

# ----------------------------------------
# STEP 3: Evaluation
# ----------------------------------------
def evaluate_model(model, name):
    y_pred = model.predict(X_test)
    print(f"\n📈 Evaluation for {name}:")
    print(f"  MAE:  {mean_absolute_error(y_test, y_pred):.3f}")
    print(f"  MSE:  {mean_squared_error(y_test, y_pred):.3f}")
    print(f"  RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.3f}")
    print(f"  R²:   {r2_score(y_test, y_pred):.3f}")

# ----------------------------------------
# STEP 4: LIME Explanation
# ----------------------------------------
def lime_explanation(model, name):
    print(f"\n🔍 LIME Explanation for {name}...")
    try:
        explainer = lime.lime_tabular.LimeTabularExplainer(
            training_data=np.array(X_train_df),  # Unscaled data
            feature_names=X.columns.tolist(),
            mode="regression",
            random_state=42  # For reproducibility
        )
        # Ensure model.predict works with scaled data for LIME
        def predict_fn(X):
            return model.predict(scaler.transform(X))
        
        exp = explainer.explain_instance(
            X_test_df.iloc[0].values,  # Unscaled test instance
            predict_fn,  # Use scaled predictions
            num_features=8
        )
        fig = exp.as_pyplot_figure()
        plt.title(f"LIME Explanation - {name}")
        plt.tight_layout()
        plt.show()
        plt.pause(1)  # Short pause for display
        plt.close()
    except Exception as e:
        print(f"⚠️ LIME explanation failed for {name}: {e}")

# ----------------------------------------
# STEP 5: SHAP Explanation
# ----------------------------------------
def shap_explanation(model, name):
    print(f"\n🔍 SHAP Explanation for {name}...")
    try:
        # Ensure model predicts on scaled data
        def predict_fn(X):
            return model.predict(scaler.transform(X))
        
        if name == "Gradient Boosting":
            explainer = shap.TreeExplainer(model, X_train_df)  # Optimized for tree-based models
            shap_values = explainer.shap_values(X_test_df.iloc[:1])  # Unscaled test data
            shap.plots.waterfall(shap_values[0], max_display=8)
        else:
            # Use KernelExplainer for non-tree models (SVR, MLP)
            background = shap.sample(X_train_df, 100, random_state=42)  # Unscaled background
            explainer = shap.KernelExplainer(predict_fn, background)
            shap_values = explainer.shap_values(X_test_df.iloc[:1].values, nsamples=100)
            shap.plots.waterfall(shap_values[0], max_display=8)
        plt.tight_layout()
        plt.show()
        plt.pause(1)  # Short pause for display
        plt.close()
    except Exception as e:
        print(f"⚠️ SHAP explanation failed for {name}: {e}")

# ----------------------------------------
# STEP 6: Run Pipeline
# ----------------------------------------
if __name__ == "__main__":
    for name, model in trained_models.items():
        evaluate_model(model, name)
        lime_explanation(model, name)
        shap_explanation(model, name)
