from tkinter import * 
from tkinter.ttk import Progressbar
from tkcalendar import Calendar, DateEntry
from importModule import loadStockList, getFortune500Ticker, loadStock
from functools import partial
from concurrent import futures
import buttonEvents as be
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=2)

class ImportFrame(Frame):

        def okClicked(self,startCal, endCal, Progressbar, root, label):
            self.destroy()
            getFortune500Ticker()
            thread_pool_executor.submit(loadStockList(startCal.get_date(), endCal.get_date(), Progressbar, root, label))
            be.updateStockList()
            self.main.destroy()

        def __init__(self):
            Frame.__init__(self)
            self.main = Tk()
            self.main.geometry('400x100')
            self.main.title("Enter Date Range To Import")

            progress = Progressbar(self.main, orient=HORIZONTAL, maximum=500, value = 0, length=200, mode = 'determinate')
            progress.grid(column=0,row=3)

            startData_lbl = Label(self.main, text="Pick Start Day")
            endDate_lbl = Label(self.main, text="Pick End Date")
            running_lbl = Label(self.main)
            entry_import = Entry(self.main, width=15)

            startCal = DateEntry(self.main,year=2013)
            endCal = DateEntry(self.main)
            click_ok = partial(self.okClicked, startCal, endCal, progress, self.main, running_lbl)
            btn_okClicked = Button(self.main, text="Import All", width=10, command=click_ok)

            click_import_single = partial(be.importSingleStock, entry_import,startCal, endCal,running_lbl)
            btn_import_single = Button(self.main, text="Import Single", width=10, command=click_import_single)

            entry_import.grid(column=0,row=0)
            startData_lbl.grid(column=0, row=1)
            endDate_lbl.grid(column=0, row=2)
            endCal.grid(column=1, row=2)
            startCal.grid(column=1, row=1)
            btn_okClicked.grid(column=2,row=3)
            running_lbl.grid(column=1,row=3)
            btn_import_single.grid(column=1,row=0)
