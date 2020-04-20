 # Plots the model loss from file
# Author: Oscar Kosar-Kosarewicz

import matplotlib.pyplot as plt
import pandas as pd


def plot_loss(file_path):
    data = pd.read_csv(file_path)

    #data.loc[data['epoch'] == 99, ['loss', 'val_loss']] = np.nan

    title = 'Model Loss'
    plt.figure(num=title)
    ax = plt.subplot(1, 1, 1)
    plt.title(title)
    #ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
    #ax.xaxis.set_minor_locator(ticker.MaxNLocator(100))
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    loss_line, = ax.plot(data['epoch'], data['loss'])
    val_loss_line, = ax.plot(data['epoch'], data['val_loss'])
    loss_line.set_label('loss')
    val_loss_line.set_label('val loss')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    plot_loss('loss.csv')
