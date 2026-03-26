"""
Assignment (11/03/2026)

Assignment Name : Customer Segmentation
Description : Perform K-Means clustering on a mall dataset and describe customer groups.


This program uses K-Means clustering to group customers based on their income and spending behavior. The algorithm divides customers into clusters where similar customers are grouped together. This helps businesses understand different types of customers for better marketing strategies.

"""

from sklearn.cluster import KMeans
import pandas as pd

# Sample dataset (you can replace with mall.csv)
data = pd.DataFrame({
    'Income': [15, 16, 17, 40, 42, 43, 80, 82, 85],
    'Spending': [39, 40, 42, 60, 65, 63, 80, 85, 90]
})

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(data)

print(data)

"""
Customer Groups
Low Income – Low Spending
    → Budget customers
Medium Income – Medium Spending
    → Average customers
High Income – High Spending
    → Premium customers

"""