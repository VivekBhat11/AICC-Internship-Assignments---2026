"""
Assignment (24/02/2026)
Assignment Name : Dataset Detective 
Description : Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.

This program uses pandas to load and analyze a dataset. It displays the top rows of the dataset, finds the highest values in numeric columns, and counts missing values. This helps in understanding basic data exploration and cleaning, which are important steps in data analysis and machine learning.

"""

import pandas as pd

# Load dataset (make sure CSV file is in same folder)
data = pd.read_csv("data.csv")

# Show top rows
print("Top 5 rows:\n", data.head())

# Find column with highest value
max_column = data.max(numeric_only=True)
print("\nHighest values in each column:\n", max_column)

# Count missing values
missing = data.isnull().sum()
print("\nMissing values:\n", missing)