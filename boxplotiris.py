# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

#Boxplot to visualize the distribution of each variable by species:
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris_df, x='species', y='sepal_length')
plt.title('Sepal Length by Species')
plt.show()
