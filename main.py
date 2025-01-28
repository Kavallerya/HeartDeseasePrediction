import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

class DataLoader:
    """
    Handles loading and preprocessing of the dataset.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        print("Data Loaded Successfully.")
        return self.data


class DataAnalyzer:
    """
    Performs exploratory data analysis.
    """
    @staticmethod
    def plot_correlation_matrix(data):
        plt.figure(figsize=(12, 10))
        correlation_matrix = data.corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
        plt.title("Correlation Matrix")
        plt.show()

    @staticmethod
    def show_target_distribution(data, target_column='target'):
        distribution = data[target_column].value_counts(normalize=True) * 100
        print("Target variable distribution (%):\n", distribution)


class ModelTrainer:
    """
    Handles model training and evaluation.
    """
    def __init__(self, models):
        self.models = models
        self.trained_models = {}
        self.scaler = StandardScaler()

    def train(self, X_train, y_train):
        for name, model in self.models.items():
            print(f"Training {name}...")
            if name == 'Logistic Regression':
                X_train = self.scaler.fit_transform(X_train)
            model.fit(X_train, y_train)
            self.trained_models[name] = model

    def evaluate(self, X_test, y_test):
        for name, model in self.trained_models.items():
            print(f"Evaluating {name}...")
            X_test_scaled = self.scaler.transform(X_test) if name == 'Logistic Regression' else X_test
            y_pred = model.predict(X_test_scaled)
            print(f"Classification Report for {name}:")
            print(classification_report(y_test, y_pred))
            roc_auc = roc_auc_score(y_test, y_pred)
            print(f"ROC-AUC for {name}: {roc_auc:.2f}\n")

    def save_model(self, model_name, file_path):
        if model_name in self.trained_models:
            joblib.dump(self.trained_models[model_name], file_path)
            print(f"Model {model_name} saved at {file_path}.")
        else:
            print(f"Model {model_name} not found.")


class HeartDiseasePredictorApp:
    """
    Main application class for the heart disease prediction system.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        # Load and analyze data
        loader = DataLoader(self.file_path)
        data = loader.load_data()

        DataAnalyzer.show_target_distribution(data)
        DataAnalyzer.plot_correlation_matrix(data)

        # Data preparation
        X, y = data.drop('target', axis=1), data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

        # Model definitions
        models = {
            'Random Forest': RandomForestClassifier(),
            'Gradient Boosting': GradientBoostingClassifier(),
            'Logistic Regression': LogisticRegression()
        }

        # Train and evaluate models
        trainer = ModelTrainer(models)
        trainer.train(X_train, y_train)
        trainer.evaluate(X_test, y_test)

        # Save one model as an example
        trainer.save_model('Random Forest', 'random_forest_model.pkl')


if __name__ == "__main__":
    app = HeartDiseasePredictorApp('data/heart.csv')
    app.run()