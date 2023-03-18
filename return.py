# Import libraries
from pandas_datareader import data as wb
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# yfinance function override
''' Function that its used to override the functionality of pandas-datareader and allow the yfinance library 
 to be used instead to access Yahoo Finance data. '''
yf.pdr_override()

# I define the tickers and dates of the data that will be downloaded.
tickers = ['TSLA', 'AAPL', 'MSFT']
startdate = '2020-01-01'
enddate = '2023-01-01'

# Function to output the market data
def market_data(ticker, start_date, end_date):
   return wb.get_data_yahoo(ticker, start=start_date, end=end_date)

# I generate the TSLA market data
total_data = market_data(tickers, startdate, enddate)

# I create the returns of TSLA market data
returns = total_data.pct_change()

# Log returns
log_returns = np.log(1 + returns)

# Mean log returns
log_returns_mean = log_returns['Adj Close'].mean()

# Log annualized returns
log_returns_mean_an = log_returns['Adj Close'].mean() * 252

# Summary
print(f"Mean log returns: \n{log_returns_mean.round(4)}\nAnualized log returns: \n{log_returns_mean_an.round(4)}")

# Plots
def dist_plot(data, col_var):
        sns.displot(data[col_var])
        plt.title(f'{col_var}')
        plt.xlabel('Daily returns')
        plt.ylabel('Frequency')
        plt.show()

dist_plot(log_returns, 'Adj Close')

# Comparative line plot
comp_plot = total_data['Adj Close']
(comp_plot / comp_plot.iloc[0]*100).plot(figsize=(12,6))
plt.show()


