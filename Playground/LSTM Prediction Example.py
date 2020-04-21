# Example of how to predict stocks using LSTM
# Author Oscar-Kosarewicz

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from StockPrediction.LSTM.PredictStock import predict_stocks

if __name__ == '__main__':
    stock_name='abc'
    # import predictor data into Dataframe
    data_source = f'../StockData/{stock_name}.csv'
    data = pd.read_csv(data_source)

    # Calculate predictions
    prediction_data = predict_stocks(data)

    # Set up plot
    plt.title(f'{stock_name} Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(5))   # number of major ticks
    ax.xaxis.set_minor_locator(ticker.MaxNLocator(25))  # number of minor ticks

    # Plot actual stock price
    actual_line, = ax.plot(data['Date'], data['Close'])
    actual_line.set_label('Actual')

    # Plot predicted stock price
    predicted_line, = ax.plot(prediction_data['Date'], prediction_data['Prediction'])
    predicted_line.set_label('Predicted')

    # Show Plot
    ax.legend()
    plt.show()
