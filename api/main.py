from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import os

app = FastAPI()

# Define the path to the trained model
model_path = 'models/model.pkl'

# Load the model if it exists
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None

# Define the data structure for the API request
class CustomerData(BaseModel):
    tenure: float
    MonthlyCharges: float
    TotalCharges: float
    gender: int
    Partner: int
    Dependents: int

@app.get("/")
def home():
    """Endpoint to check if the API is running."""
    return {"message": "Churn Prediction API is Running!"}

@app.post("/predict")
def predict(data: CustomerData):
    """Endpoint to receive customer data and return a churn prediction."""
    if model is None:
        return {"error": "Model file not found. Please ensure the model is trained."}
    
    # 1. Convert input data into a pandas DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # 2. Identify all feature columns the model was trained on
    model_columns = model.feature_names_in_
    
    # 3. Create a complete DataFrame with all required columns, filling missing ones with 0
    full_df = pd.DataFrame(columns=model_columns)
    full_df = pd.concat([full_df, input_df], axis=0).fillna(0)
    
    # 4. Reorder columns to match the exact order used during model training
    full_df = full_df[model_columns]
    
    try:
        # Perform the prediction
        prediction = model.predict(full_df)[0]
        result = "Churn" if prediction == 1 else "No Churn"
        
        return {
            "prediction": result,
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e), "status": "failed"}
