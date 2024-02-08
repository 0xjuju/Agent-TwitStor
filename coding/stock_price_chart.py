# filename: stock_price_chart.py
import pandas as pd
import matplotlib.pyplot as plt

# Read the historical stock price data for NVDA and TESLA from CSV files
nvda_data = pd.read_csv('path_to_nvda_csv_file.csv')
tesla_data = pd.read_csv('path_to_tesla_csv_file.csv')

# Convert the date column to datetime format
nvda_data['Date'] = pd.to_datetime(nvda_data['Date'])
tesla_data['Date'] = pd.to_datetime(tesla_data['Date'])

# Calculate the YTD price change for NVDA and TESLA
nvda_ytd_change = (nvda_data['Close'].iloc[-1] - nvda_data['Close'].iloc[0]) / nvda_data['Close'].iloc[0] * 100
tesla_ytd_change = (tesla_data['Close'].iloc[-1] - tesla_data['Close'].iloc[0]) / tesla_data['Close'].iloc[0] * 100

# Plot the YTD price change for NVDA and TESLA
plt.figure(figsize=(10, 5))
plt.plot(nvda_data['Date'], nvda_data['Close'], label='NVDA')
plt.plot(tesla_data['Date'], tesla_data['Close'], label='TESLA')
plt.title('YTD Stock Price Change')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()