import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import joblib
import os
mlflow.set_tracking_uri(f"file:///{os.path.join(os.getcwd(), 'mlruns').replace('\\', '/')}")


def train_model():
    # 1. Load the cleaned data
    processed_data_path = 'data/processed/cleaned_data.csv'
    if not os.path.exists(processed_data_path):
        print("Error: Cleaned data not found. Run preprocessing.py first.")
        return

    df = pd.read_csv(processed_data_path)
    
    # 2. Split features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Start MLflow tracking locally
    # This will create a folder named 'mlruns' in your project
    mlflow.set_experiment("Churn_Prediction_Experiment")
    
    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        predictions = model.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        
        # Log to local MLflow
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Training Successful! Accuracy: {acc}")
        
        # 4. Save the model locally
       # Updated Line 43:
        if not os.path.exists('models'):
            os.makedirs('models')
        joblib.dump(model, 'models/model.pkl')
        print("Model saved to models/model.pkl")

if __name__ == "__main__":
    train_model()