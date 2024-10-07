import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_revenue(monthly_revenue):
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_revenue['Month'].astype(str), monthly_revenue['Revenue'], marker='o', linestyle='--')
    plt.title('Monthly Revenue Over Time')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_rfm_distributions(rfm):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    sns.histplot(rfm['Recency'], bins=20, kde=True, ax=axes[0], color='blue')
    axes[0].set_title('Recency Distribution')
    
    sns.histplot(rfm['Frequency'], bins=20, kde=True, ax=axes[1], color='green')
    axes[1].set_title('Frequency Distribution')
    
    sns.histplot(rfm['Monetary'], bins=20, kde=True, ax=axes[2], color='red')
    axes[2].set_title('Monetary Distribution')
    
    plt.tight_layout()
    plt.show()

def plot_rfm_clusters(rfm):
    sns.pairplot(rfm, vars=['Recency', 'Frequency', 'Monetary'], hue='Cluster', palette='viridis')
    plt.title('RFM Clusters')
    plt.show()

# Usage example:
# plot_monthly_revenue(monthly_revenue)
# plot_rfm_distributions(rfm)
# plot_rfm_clusters(rfm_clustered)