import pandas as pd
import numpy as np
from datetime import datetime

# Data Cleaning and Preparation Functions
def load_and_clean_data(filepath):
    # Load the dataset, handling encoding issues
    data = pd.read_csv(filepath, encoding='ISO-8859-1')
    
    # Drop missing CustomerID and filter out invalid Quantity and UnitPrice
    data = data.dropna(subset=['CustomerID'])
    data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]
    
    # Create 'TotalPrice' column
    data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
    
    # Convert 'InvoiceDate' to datetime format
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    
    # Create 'YearMonth' for monthly aggregation
    data['YearMonth'] = data['InvoiceDate'].dt.to_period('M')
    
    # Create additional columns for hour and day of the week
    data['Hour'] = data['InvoiceDate'].dt.hour
    data['DayOfWeek'] = data['InvoiceDate'].dt.dayofweek  # 0 = Monday, 6 = Sunday
    
    return data

# Usage example:
# tx_data = load_and_clean_data('./OnlineRetail.csv')