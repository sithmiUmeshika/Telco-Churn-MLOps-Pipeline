import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# දත්ත ලබාගන්න (ඔයාගේ dataset එක තියෙන තැන දෙන්න)
df = pd.read_csv('data/raw/Churn_Prediction_DataSet.csv')

# 1. Tenure & Monthly Charges Histogram
plt.figure(figsize=(10,5))
plt.subplot(1,2,1); sns.histplot(df['tenure'], kde=True); plt.title('Tenure Distribution')
plt.subplot(1,2,2); sns.histplot(df['MonthlyCharges'], kde=True); plt.title('Monthly Charges')
plt.show() # මෙන්න මේකේ Screenshot එකක් ගන්න

# 2. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show() # මෙන්න මේකේ Screenshot එකක් ගන්න

# 3. Churn vs Contract Type
plt.figure(figsize=(8,5))
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title('Churn by Contract Type')
plt.show() # මෙන්න මේකේ Screenshot එකක් ගන්න