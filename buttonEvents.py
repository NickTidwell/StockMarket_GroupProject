from importModule import loadStock
from tkinter import *
import importForm
import csv
import csvTable

def displayGrid(txt):
    dow = Tk()
    app = csvTable.CreateTable(txt, dow)
    app.mainloop()

def loadStockClicked(txt, start, end):
    loadStock(txt.get(), start.get_date(), end.get_date())
    displayGrid(txt.get())

def importStockClicked():
    popUp = importForm.ImportFrame()
    popUp.mainloop()
    
    

