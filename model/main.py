import data_preparation as dp
import rfm_analysis as rfm_an
import visualization as vis
import customer_segmentation as cs

# Main script to run the customer segmentation analysis
if __name__ == "__main__":
    # Load and clean data
    filepath = './OnlineRetail.csv'
    tx_data = dp.load_and_clean_data(filepath)
    
    # Perform RFM analysis
    rfm = rfm_an.calculate_rfm(tx_data)
    
    # Perform clustering
    rfm_clustered = rfm_an.perform_rfm_clustering(rfm, n_clusters=4)
    
    # Segment customers
    rfm_segmented = cs.segment_customers(rfm_clustered)
    segment_stats = cs.get_segment_statistics(rfm_segmented)
    print(segment_stats)
    
    # Plot results
    vis.plot_monthly_revenue(tx_data.groupby('YearMonth').agg({'TotalPrice': 'sum'}).reset_index().rename(columns={'TotalPrice': 'Revenue'}))
    vis.plot_rfm_distributions(rfm_segmented)
    vis.plot_rfm_clusters(rfm_segmented)
    
    # Example: Suggest action for a customer segment
    action = cs.suggest_customer_actions('High Value')
    print(f"Suggested action for High Value customers: {action}")