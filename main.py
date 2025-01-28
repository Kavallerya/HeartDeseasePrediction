import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_curve, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

class DataHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.filepath)
        print("Data loaded successfully.")

    def get_features_and_target(self):
        X = self.data.drop('target', axis=1)
        y = self.data['target']
        return X, y

    def plot_correlation_matrix(self):
        plt.figure(figsize=(12, 10))
        correlation_matrix = self.data.corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
        plt.title("Correlation Matrix")
        plt.show()

class ModelTrainer:
    def __init__(self):
        self.models = {
            "RandomForest": RandomForestClassifier(),
            "GradientBoosting": GradientBoostingClassifier(),
            "LogisticRegression": LogisticRegression()
        }
        self.scaler = StandardScaler()
        self.feature_names = None

    def train_test_split(self, X, y):
        self.feature_names = X.columns.tolist()
        return train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    def scale_data(self, X_train, X_test):
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled

    def train_models(self, X_train, y_train):
        for name, model in self.models.items():
            if name == "LogisticRegression":
                X_train = self.scaler.fit_transform(X_train)  # Ensure scaling for Logistic Regression
            model.fit(X_train, y_train)
            print(f"{name} model trained successfully.")

    def evaluate_models(self, X_test, y_test):
        for name, model in self.models.items():
            if name == "LogisticRegression":
                X_test_scaled = self.scaler.transform(X_test)
                y_pred = model.predict(X_test_scaled)
            else:
                y_pred = model.predict(X_test)
            print(f"\n{name} Model Evaluation:")
            print(classification_report(y_test, y_pred))

    def save_model(self, model_name, filename):
        if model_name in self.models:
            joblib.dump((self.models[model_name], self.feature_names), filename)
            print(f"Model '{model_name}' saved to '{filename}'.")
        else:
            print("Invalid model name.")

    def load_model(self, filename):
        model, feature_names = joblib.load(filename)
        self.feature_names = feature_names
        return model

    def predict(self, model, input_data):
        input_df = pd.DataFrame([input_data], columns=self.feature_names)
        input_scaled = self.scaler.transform(input_df) if isinstance(model, LogisticRegression) else input_df
        prediction = model.predict(input_scaled)
        return prediction

if __name__ == "__main__":
    # Initialize and load data
    data_handler = DataHandler("data/heart.csv")
    data_handler.load_data()

    # Analyze data
    data_handler.plot_correlation_matrix()

    # Split data
    X, y = data_handler.get_features_and_target()
    trainer = ModelTrainer()
    X_train, X_test, y_train, y_test = trainer.train_test_split(X, y)

    # Train models
    trainer.train_models(X_train, y_train)

    # Evaluate models
    trainer.evaluate_models(X_test, y_test)

    # Save one of the models
    trainer.save_model("RandomForest", "random_forest_model.joblib")

    # Load the model and test with user input
    print("\n=== Heart Disease Prediction Test ===")
    model = trainer.load_model("random_forest_model.joblib")
    print("Enter patient data (numerical values for all features):")
    input_data = [float(x) for x in input("Example (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal): ").split(',')]
    prediction = trainer.predict(model, input_data)
    result = "Positive for heart disease" if prediction[0] == 1 else "Negative for heart disease"
    print(f"Prediction: {result}")
