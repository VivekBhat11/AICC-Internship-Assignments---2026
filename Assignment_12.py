"""
Assignment (26/02/2026)

Assignment Name : Data Doctor
Description : Clean a dataset by handling missing values, removing duplicates, standardizing text, and explain why cleaning matters.

This program cleans a dataset using pandas. It handles missing values by filling them, removes duplicate records, and standardizes text by converting it to lowercase. Data cleaning improves data quality and ensures accurate analysis and better machine learning results.

"""

import pandas as pd

# Load dataset
data = pd.read_csv("data.csv")

# Handle missing values (fill with mean)
data.fillna(data.mean(numeric_only=True), inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Standardize text (lowercase)
for col in data.select_dtypes(include='object'):
    data[col] = data[col].str.lower()

# Show cleaned data
print(data.head())