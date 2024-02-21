# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

#pairplot to visualize relationships between variables
sns.pairplot(iris_df, hue='species', palette='Set1')
plt.show()
