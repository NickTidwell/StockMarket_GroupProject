import numpy as np
from os import path
import pandas as pd

class DataSplitter:
    def __init__(self, filename, train_rate):
        self.file = pd.read_csv(filename)   # read csv file into pandas df
        self.train_rate = train_rate

        self.i = int(self.train_rate * len(self.file))   # index for train vs test data
        self.train_data = self.file[0: self.i]  # save training data to new df
        self.test_data = self.file[self.i :]    # save testing data to new df
        
        self.input_train = []   # create lists for inputs and outputs
        self.output_train = []
        self.input_test = []
        self.output_test = []

        self.length = len(self.file)

    def create_training(self, train_size):      # splits traing data in to test_size np arrays
        iterations = (len(self.train_data)// train_size)*train_size - train_size - 1
        for i in range(iterations):
            x = np.array(self.train_data.iloc[i: i + train_size, 1])
            y = np.array([self.train_data.iloc[i + train_size + 1, 1]], np.float)
            self.input_train.append(x)
            self.output_train.append(y)


        
        self.trainX = np.array(self.input_train)
        self.trainY = np.array(self.output_train)  
        np.save('trainX', self.trainX)
        np.save('trainY', self.trainY)

        dates = np.zeros(train_size)
        np.save('Dates', dates)
         
        
    def create_testing(self, test_size):
        iterations = (len(self.test_data)// test_size)*test_size - test_size - 1
        for i in range(iterations):
            x = np.array(self.test_data.iloc[i: i + test_size, 1])
            y = np.array([self.test_data.iloc[i + test_size + 1, 1]], np.float)
            self.input_test.append(x)
            self.output_test.append(y)
        self.testX = np.array(self.input_test)        # each index of x is test_size prices for the stock
        self.testY = np.array(self.output_test)
        
        np.save('testX', self.testX)
        np.save('testY', self.testY)


# for testing individual model
# if __name__  == "__main__":

#     x = DataSplitter("stock.csv", 0.9)  
#     x.create_training(10)
#     x.create_testing(10)