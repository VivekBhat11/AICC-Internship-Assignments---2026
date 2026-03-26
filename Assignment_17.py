"""
Assignment (18/03/2026)

Assignment Name : Customer Segmentation
Description : Perform K-Means clustering on a mall dataset and describe customer groups.


This program uses K-Means clustering to segment mall customers based on their annual income and spending score. The algorithm groups similar customers into clusters without using labeled data. This helps businesses understand customer behavior and target them effectively.

Customer Groups (Example)
Low Income - Low Spending → Budget customers
Low Income - High Spending → Careless spenders
High Income - Low Spending → Careful customers
High Income - High Spending → Premium customers
Average Income - Average Spending → Regular customers

"""

import pandas as pd
from sklearn.cluster import KMeans

# Load dataset (replace with your file name)
data = pd.read_csv("mall_customers.csv")

# Select useful features
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Apply K-Means
kmeans = KMeans(n_clusters=5, random_state=0)
data['Cluster'] = kmeans.fit_predict(X)

# Show result
print(data.head())