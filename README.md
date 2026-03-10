# 📊 Telco Customer Churn - MLOps Pipeline

This project implements an End-to-End MLOps pipeline to predict customer churn for a telecommunications company. It covers everything from data preprocessing to model deployment and workflow orchestration.

## 🚀 Key Features
- **Data Engineering:** Automated cleaning and feature scaling.
- **Data Versioning:** Managed using **DVC** for reproducibility.
- **Experiment Tracking:** All model runs and metrics logged with **MLflow**.
- **Orchestration:** Pipeline tasks automated via **Apache Airflow**.
- **Model Serving:** Real-time prediction API built with **FastAPI**.
- **Containerization:** Entire stack managed using **Docker Compose**.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **ML Libraries:** XGBoost, Scikit-Learn, Pandas
- **MLOps Tools:** DVC, MLflow, Apache Airflow
- **Deployment:** FastAPI, Docker

## 📂 Project Structure
- `src/`: Core logic for preprocessing and training.
- `api/`: FastAPI implementation for model serving.
- `airflow_dags/`: Workflow definitions.
- `data/`: DVC tracked dataset directory.

## 📝 How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Start the MLOps stack: `docker-compose up`