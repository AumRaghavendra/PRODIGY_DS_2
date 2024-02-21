import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Data cleaning
print("Null Values:")
print(iris_df.isnull().sum())

# Exploratory Data Analysis (EDA)
# Summary statistics
print("\nSummary Statistics:")
print(iris_df.describe())

numeric_cols = iris_df.select_dtypes(include=[np.number])

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()