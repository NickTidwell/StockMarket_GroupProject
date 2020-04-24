from tkinter import *
import buttonEvents as be
from tkinter import ttk
from functools import partial
from reportModule import openReport
class ReportFrame(Frame):


        def __init__(self):
            Frame.__init__(self)
            self.main = Tk()
            self.main.geometry('400x100')
            self.main.title("Enter Date Range To Import")

            tkvar_reports = StringVar()
            cb_reports = ttk.Combobox(self.main, width=15, values=be.reportList(), textvariable=tkvar_reports)

            click_open = partial(openReport, cb_reports)
            btn_open = Button(self.main, text="Display Data", width=10, command=click_open)

            cb_reports.grid(column=0,row=0)
            btn_open.grid(column=1,row=0)
