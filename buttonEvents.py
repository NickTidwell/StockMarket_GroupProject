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

def loadStockClicked(txt, start, end):
    loadStock(txt.get(), start.get_date(), end.get_date())
    displayGrid(txt.get())
