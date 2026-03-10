import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data():
    # 1. Define paths
    input_path = 'data/raw/Churn Prediction DataSet.csv'
    output_dir = 'data/processed'
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found!")
        return

    # 2. Load the dataset
    df = pd.read_csv(input_path)
    
    # 3. Handle missing values & Clean 'TotalCharges'
    # This is a specific requirement in your assignment
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna(subset=['TotalCharges'])
    
    # 4. Feature Engineering: Encoding categorical variables
    # Drop CustomerID as it's not a feature for prediction
    df = df.drop(columns=['customerID'])
    
    # Use LabelEncoder for binary columns and Churn
    le = LabelEncoder()
    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    for col in binary_cols:
        df[col] = le.fit_transform(df[col])
    
    # One-hot encoding for multi-category columns
    categorical_cols = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
                        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
                        'Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=categorical_cols)
    
    # 5. Save processed data
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(f'{output_dir}/cleaned_data.csv', index=False)
    
    print("Preprocessing completed successfully!")
    print(f"Cleaned data saved to: {output_dir}/cleaned_data.csv")

if __name__ == "__main__":
    preprocess_data()