import matplotlib.pyplot as plt
import pandas as pd
import keras as ks
import numpy as np
from keras.models import load_model
from os import path
from  StockPrediction.MLP.split_data import DataSplitter

def plotter(data_file_path):
    datasource = DataSplitter(data_file_path, 1)
    length = datasource.length // 100
    offset = datasource.length- ((datasource.length // length)*length - 1)
    datasource.create_training(length)

    x = datasource.trainX

    file_path = path.join(path.dirname(__file__), 'MLP_model.h5')

    restored_model = load_model(file_path)
    prediction = restored_model.predict(x)
    date = np.arange(offset,len(prediction)+offset)
    return date, prediction
      

