import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# RFM Analysis Functions
def calculate_rfm(data):
    # Calculate the latest date in the dataset
    latest_date = data['InvoiceDate'].max()
    
    # Aggregate RFM values for each customer
    rfm = data.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (latest_date - x.max()).days,  # Recency
        'InvoiceNo': 'nunique',  # Frequency (count unique transactions)
        'TotalPrice': 'sum'  # Monetary (total spending)
    }).reset_index()
    
    # Rename columns for better readability
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    
    return rfm

def perform_rfm_clustering(rfm, n_clusters=4):
    # Standardize the RFM values for clustering
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)
    
    return rfm

# Usage example:
# rfm = calculate_rfm(tx_data)
# rfm_clustered = perform_rfm_clustering(rfm, n_clusters=4)