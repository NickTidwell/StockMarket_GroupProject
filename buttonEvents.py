from importModule import loadStock
from tkinter import *
import csv

def clicked(txt, lbl):
    res = txt.get()
    lbl.configure(text= res)

def displayGrid(window, txt):
    with open('StockData/' + txt + '.csv', newline = "") as file:
        reader = csv.reader(file)
        r = 1
        for col in reader:
            c = 0
            for row in col:
                label = Label(window, width = 15, height = 2,text = row, relief = RIDGE)
                label.grid(row = r, column = c)
                c += 1
            r += 1
def loadStockClicked(txt, window):
    loadStock(txt.get())
    displayGrid(window,txt.get())
