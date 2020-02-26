from tkinter import * 
from tkinter.ttk import Progressbar
from tkcalendar import Calendar, DateEntry
from importModule import loadStockList, getFortune500Ticker
from functools import partial

class ImportFrame(Frame):

        def okClicked(self,startCal, endCal, Progressbar, root):
            getFortune500Ticker()
            loadStockList(startCal.get_date(), endCal.get_date(), Progressbar, root)
            self.main.destroy()
        def __init__(self):

            Frame.__init__(self)
            self.main = Tk()
            self.main.geometry('400x100')
            self.main.title("Enter Date Range To Import")

            progress = Progressbar(self.main, orient=HORIZONTAL, length=200, mode = 'determinate')
            progress.grid(column=0,row=4)
            startData_lbl = Label(self.main, text="Pick Start Day")
            endDate_lbl = Label(self.main, text="Pick End Date")
            startCal = DateEntry(self.main)
            endCal = DateEntry(self.main)
            click_ok = partial(self.okClicked, startCal, endCal, progress, self.main)
            btn_okClicked = Button(self.main, text="Ok", width=5, command=click_ok)

            startData_lbl.grid(column=0, row=1)
            endDate_lbl.grid(column=0, row=2)
            endCal.grid(column=1, row=2)
            startCal.grid(column=1, row=1)
            btn_okClicked.grid(column=3,row=2)
            return

