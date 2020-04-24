# Create LST prediction model
# Author: Oscar Kosar-Kosarewicz

import numpy as np
import keras as ks
from StockPrediction.LSTM.CreateTrainingData import generate_training_data
from StockPrediction.LSTM.PlotLoss import plot_loss
from StockPrediction.LSTM.PlotModelPrediction import plot_prediction
from StockPrediction.LSTM.CreateTrainingData import trim_data

# generate training and test data
def gen_data(stock_name, batch_size, time_steps_in_batch):
    x_train, y_train, x_temp, y_temp = generate_training_data(stock_name, time_steps_in_batch)
    x_train = trim_data(x_train, batch_size)
    y_train = trim_data(y_train, batch_size)
    x_validate, x_test = np.array_split(x_temp, 2)
    y_validate, y_test = np.array_split(y_temp, 2)

    x_validate = trim_data(x_validate, batch_size)
    y_validate = trim_data(y_validate, batch_size)
    # x_test, y_test = trim_data(x_test, y_test, batch_size)
    return x_train, y_train, x_validate, y_validate


# Create and return LSTM Model
def create_model(batch_size, time_steps_in_batch, hidden_layers_LSTM, hidden_layers_relu, dropout):
    model = ks.Sequential()
    model.add(ks.layers.LSTM(hidden_layers_LSTM, batch_input_shape=(batch_size, time_steps_in_batch, 6),
                             dropout=0,
                             recurrent_dropout=0, stateful=True,
                             kernel_initializer=ks.initializers.random_uniform(seed=0)))

    model.add(ks.layers.Dropout(dropout))
    model.add(ks.layers.Dense(hidden_layers_relu, activation='relu'))
    model.add(ks.layers.Dense(1, activation='linear'))
    model.compile(loss='mean_squared_error', optimizer='adam')

    return model


if __name__ == '__main__':
    stock_name = 'amzn'
    batch_size = 5
    time_steps_in_batch = 10
    hidden_layers_LSTM = 50
    hidden_layers_relu = 10
    dropout = 0

    x_train, y_train, x_validate, y_validate = gen_data(stock_name, batch_size, time_steps_in_batch)

    model = create_model(batch_size, time_steps_in_batch, hidden_layers_LSTM, hidden_layers_relu, dropout)
    csv_logger = ks.callbacks.CSVLogger('loss.csv', append=False)
    model.fit(x_train, y_train, epochs=200, batch_size=batch_size, verbose=2, shuffle=False,
              validation_data=(x_validate, y_validate), callbacks=[csv_logger])
    model.save('LSTM_model')
    meta_data = dict(batch_size=batch_size, time_steps_in_batch=time_steps_in_batch)
    np.save('LSTM_model_metadata', meta_data)
    plot_loss('loss.csv')
    plot_prediction('LSTM_model', batch_size)
