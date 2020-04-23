import pandas as pd
import numpy as np


def back_test(strategy, seq_len, dim):
    """
    A simple back test for a given date period
    :param strategy: the chosen strategy. Note to have already formed the model, and fitted with training data.
    :param seq_len: length of the days used for prediction
    :param ticker: company ticker
    :param start_date: starting date
    :type start_date: "YYYY-mm-dd"
    :param end_date: ending date
    :type end_date: "YYYY-mm-dd"
    :param dim: dimension required for strategy: 3dim for LSTM and 2dim for MLP
    :type dim: tuple
    :return: Percentage errors array that gives the errors for every test in the given date range
    """
    df = pd.read_csv("../../StockData/amzn.csv")
    close_data = df["Adj Close"]

    errors = []
    for i in range((len(close_data)//10)*10 - seq_len - 1):
        x = np.array(close_data.iloc[i: i + seq_len, 1]).reshape(dim) / 200
        y = np.array(close_data.iloc[i + seq_len + 1, 1]) / 200
        predict = strategy.predict(x)
        while predict == 0:
            predict = strategy.predict(x)
        error = (predict - y) / 100
        errors.append(error)
        total_error = np.array(errors)
    print(f"Average error = {total_error.mean()}")