# Discover optimal hyperparameters for model
# Author: Oscar Kosar-Kosarewicz

from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import ParameterGrid
from StockPrediction.LSTM.CreateModel import create_model, gen_data
import pandas as pd

# parameters to test
stock_name = 'amzn'
batch_size = [5, 10, 20, 50]
time_steps_in_batch = [5, 10, 20]
hidden_layers_LSTM = [20, 50, 100]
hidden_layers_relu = [5, 20]
dropout = [x * 0.05 for x in range(0, 3)]


param_grid = ParameterGrid(dict(batch_size=batch_size, time_steps_in_batch=time_steps_in_batch, hidden_layers_LSTM=hidden_layers_LSTM,
                  hidden_layers_relu=hidden_layers_relu, dropout=dropout))
results = pd.DataFrame()

for i, kwargs in enumerate(param_grid):
    x_train, y_train, x_validate, y_validate = gen_data(stock_name, kwargs['batch_size'], kwargs['time_steps_in_batch'])
    model = create_model(**kwargs)
    model.fit(x_train, y_train, epochs=150, batch_size=kwargs['batch_size'], validation_data=(x_validate, y_validate), verbose=0)
    score = model.evaluate(x_validate, y_validate, batch_size=kwargs['batch_size'])
    kwargs['score'] = score
    kwargs['index'] = i
    print(i)
    results = results.append(kwargs, ignore_index=True)
results.to_csv('results.csv')
