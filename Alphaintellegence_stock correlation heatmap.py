import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_stock_data(companies, start_date='2023-01-01', end_date='2024-01-01'):
    """
    Fetch stock data for given company names.
    
    Parameters:
    - companies (list): List of company full names or stock symbols
    - start_date (str): Start date for data collection
    - end_date (str): End date for data collection
    
    Returns:
    - DataFrame with adjusted closing prices
    """
    # Dictionary to map full company names to stock symbols
    company_symbols = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Amazon': 'AMZN',
        'Alphabet': 'GOOGL',
        'Meta': 'META',
        'Tesla': 'TSLA',
        'Nvidia': 'NVDA',
        'JPMorgan Chase': 'JPM',
        'Walmart': 'WMT',
        'ExxonMobil': 'XOM',
        'Johnson & Johnson': 'JNJ',
        'Visa': 'V',
        'Mastercard': 'MA',
        'Intel': 'INTC',
        'Coca-Cola': 'KO'
    }
    
    # Convert company names to symbols
    symbols = [company_symbols.get(company, company) for company in companies]
    
    # Fetch stock data
    data = yf.download(symbols, start=start_date, end=end_date)['Adj Close']
    return data

def create_correlation_heatmap(data):
    """
    Create a correlation heatmap with blue color gradient.
    
    Parameters:
    - data (DataFrame): Stock price data
    
    Returns:
    - Correlation matrix
    """
    # Calculate correlation matrix using percentage change
    correlation_matrix = data.pct_change().corr()
    
    # Create figure and heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap='Blues', 
        center=0, 
        vmin=-1, 
        vmax=1, 
        square=True,
        linewidths=0.5
    )
    plt.title('Stock Price Correlation Heatmap', fontsize=16)
    plt.tight_layout()
    return correlation_matrix

def create_candlestick_charts(data, companies):
    """
    Create candlestick charts for selected companies.
    
    Parameters:
    - data (DataFrame): Stock price data
    - companies (list): Selected company names
    """
    # Create subplots
    fig, axes = plt.subplots(len(companies), 1, figsize=(12, 5*len(companies)))
    
    if len(companies) == 1:
        axes = [axes]
    
    for i, company in enumerate(companies):
        # Prepare data
        stock_data = data[company]
        
        # Calculate price changes
        stock_data_pct = stock_data.pct_change()
        
        # Create candlestick-like visualization
        axes[i].plot(stock_data.index, stock_data, label='Price')
        axes[i].set_title(f'{company} Stock Price', fontsize=14)
        axes[i].set_xlabel('Date')
        axes[i].set_ylabel('Price ($)')
        
        # Add price change indicators
        positive_changes = stock_data_pct > 0
        negative_changes = stock_data_pct < 0
        
        axes[i].scatter(
            stock_data.index[positive_changes], 
            stock_data[positive_changes], 
            color='green', 
            marker='^', 
            alpha=0.7, 
            label='Positive Change'
        )
        axes[i].scatter(
            stock_data.index[negative_changes], 
            stock_data[negative_changes], 
            color='red', 
            marker='v', 
            alpha=0.7, 
            label='Negative Change'
        )
        
        axes[i].legend()
    
    plt.tight_layout()

def main():
    print("Stock Correlation and Visualization Tool")
    print("\nAvailable Companies:")
    available_companies = [
        'Apple', 'Microsoft', 'Amazon', 'Alphabet', 'Meta', 
        'Tesla', 'Nvidia', 'JPMorgan Chase', 'Walmart', 'ExxonMobil', 
        'Johnson & Johnson', 'Visa', 'Mastercard', 'Intel', 'Coca-Cola'
    ]
    
    for company in available_companies:
        print(f"- {company}")
    
    # Get user input
    while True:
        try:
            print("\nEnter at least 2 company names (comma-separated):")
            user_input = input().split(',')
            companies = [company.strip() for company in user_input]
            
            # Validate input
            if len(companies) < 2:
                print("Please enter at least 2 companies.")
                continue
            
            invalid_companies = [c for c in companies if c not in available_companies]
            if invalid_companies:
                print(f"Invalid companies: {invalid_companies}")
                print("Please choose from the available list.")
                continue
            
            break
        except Exception as e:
            print(f"An error occurred: {e}")
    
    # Fetch stock data
    try:
        stock_data = fetch_stock_data(companies)
        
        # Create correlation heatmap
        correlation_matrix = create_correlation_heatmap(stock_data)
        plt.show()
        
        # Print correlation details
        print("\nCorrelation Matrix:")
        print(correlation_matrix)
        
        # Create candlestick charts
        create_candlestick_charts(stock_data, companies)
        plt.show()
        
    except Exception as e:
        print(f"Error processing stock data: {e}")

if __name__ == "__main__":
    main()
