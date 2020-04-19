# Plots a stock from StockData (generated by MainForm) of your choosing
# Author: Oscar Kosar-Kosarewicz

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

y_value = 'Open'

stock_name = input('Enter stock name: ')
data_file_path = f'../StockData/{stock_name}.csv'

data = pd.read_csv(data_file_path)
title = f'{stock_name.upper()} Stock'
plt.figure(figsize=(12, 6), num=title)
ax = plt.subplot(1, 1, 1)
plt.title(title)
ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
ax.xaxis.set_minor_locator(ticker.MaxNLocator(100))
plt.xlabel('Date')
plt.ylabel(f'{y_value} Price ($)')
ax.plot(data['Date'], data[y_value])
plt.show()