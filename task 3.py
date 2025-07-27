import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data resembling telco_customer_churn.csv
data = {
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male'],
    'SeniorCitizen': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'InternetService': ['DSL', 'DSL', 'DSL', 'DSL', 'Fiber optic', 'Fiber optic', 'Fiber optic', 'DSL', 'Fiber optic', 'Fiber optic'],
    'MonthlyCharges': [29.85, 56.95, 53.85, 42.30, 70.70, 99.65, 89.10, 29.75, 108.15, 88.35],
    'tenure': [1, 34, 2, 45, 2, 8, 22, 10, 28, 62],
    'Churn': [0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

# Visualization function
def plot_all(df):
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    
    sns.countplot(x='Churn', data=df, ax=axes[0,0])
    axes[0,0].set_title("Churn Distribution")
    axes[0,0].set_xticklabels(['No', 'Yes'])

    sns.countplot(x='gender', hue='Churn', data=df, ax=axes[0,1])
    axes[0,1].set_title("Gender vs Churn")

    sns.countplot(x='SeniorCitizen', hue='Churn', data=df, ax=axes[1,0])
    axes[1,0].set_title("Senior Citizen vs Churn")
    axes[1,0].set_xticklabels(['No', 'Yes'])

    sns.countplot(x='InternetService', hue='Churn', data=df, ax=axes[1,1])
    axes[1,1].set_title("Internet Service vs Churn")
    axes[1,1].tick_params(axis='x', rotation=30)

    sns.histplot(data=df, x='MonthlyCharges', hue='Churn', kde=True, bins=10, ax=axes[2,0])
    axes[2,0].set_title("Monthly Charges vs Churn")

    sns.histplot(data=df, x='tenure', hue='Churn', kde=True, bins=10, ax=axes[2,1])
    axes[2,1].set_title("Tenure vs Churn")

    plt.tight_layout()
    plt.show()

# Call the function to plot
plot_all(df)
