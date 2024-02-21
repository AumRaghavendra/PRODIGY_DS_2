# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Display the first few rows of the dataset
print(iris_df.head())

print(iris_df.isnull().sum())
