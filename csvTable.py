from tkinter import *
from pandastable import Table

class CreateStockTable(Frame):
        def __init__(self, csvName, master):
            Frame.__init__(self, master)
            self.main = master
            self.main.geometry('800x600+200+100')
            self.main.title(csvName + " ticker data")
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            self.table = pt = Table(f)
            pt.importCSV('StockData/' + csvName + '.csv')
            pt.show()
            return

class CreateReportTable(Frame):
    def __init__(self, csvName, master):
        Frame.__init__(self, master)
        self.main = master
        self.main.geometry('800x600+200+100')
        self.main.title(csvName + " report")
        f = Frame(self.main)
        f.pack(fill=BOTH, expand=1)
        self.table = pt = Table(f)
        pt.importCSV('Reports/' + csvName)
        pt.show()

