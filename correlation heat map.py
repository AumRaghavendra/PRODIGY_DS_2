import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Exploratory Data Analysis (EDA)
# Remove non-numeric column before creating the correlation heatmap
numeric_cols = iris_df.select_dtypes(include=[np.number])

# Visualize the correlation between variables
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
