from importModule import loadStock
from tkinter import *
import csv
import csvTable
def clicked(txt, lbl):
    res = txt.get()
    lbl.configure(text= res)

def displayGrid(txt):
    dow = Tk()
    app = csvTable.TestApp(txt, dow)
    app.mainloop()

def loadStockClicked(txt):
    loadStock(txt.get())
    displayGrid(txt.get())
