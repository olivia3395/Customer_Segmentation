import pandas as pd

# Customer Segmentation Functions
def segment_customers(rfm):
    # Define customer segments based on RFM cluster scores
    rfm['CustomerSegment'] = pd.cut(rfm['Cluster'], 
                                    bins=[-1, 1, 3, rfm['Cluster'].max()],
                                    labels=['Low Value', 'Mid Value', 'High Value'])
    return rfm

def get_segment_statistics(rfm):
    # Calculate statistics for each customer segment
    segment_stats = rfm.groupby('CustomerSegment').agg({
        'Recency': ['mean', 'median', 'min', 'max'],
        'Frequency': ['mean', 'median', 'min', 'max'],
        'Monetary': ['mean', 'median', 'min', 'max'],
        'CustomerID': 'count'
    }).reset_index()
    return segment_stats

def suggest_customer_actions(segment):
    # Suggest actions based on customer segment
    if segment == 'High Value':
        return "Reward loyalty with exclusive offers and VIP events."
    elif segment == 'Mid Value':
        return "Encourage more frequent purchases with targeted promotions."
    elif segment == 'Low Value':
        return "Re-engage with special discounts or win-back campaigns."
    else:
        return "Segment not recognized."

# Usage example:
# rfm_segmented = segment_customers(rfm_clustered)
# segment_stats = get_segment_statistics(rfm_segmented)
# action = suggest_customer_actions('High Value')