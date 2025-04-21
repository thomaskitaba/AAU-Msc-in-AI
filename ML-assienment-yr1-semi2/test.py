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
            random_state=42  # Added for reproducibility
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
        plt.pause(1)  # Reduced pause for faster execution
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
        plt.pause(1)  # Reduced pause
        plt.close()
    except Exception as e:
        print(f"⚠️ SHAP explanation failed for {name}: {e}")