from tkinter import *
import buttonEvents as be
from functools import partial
from pandastable import Table
from tkcalendar import Calendar, DateEntry


window = Tk()
window.geometry('600x400')
window.title("Python Stock Market")


lbl_searchText = Label(window, text="Enter Stock To Search: ")
startData_lbl = Label(window, text="Start Day")
endDate_lbl = Label(window, text="End Date")

entry_stock = Entry(window, width = 15)

startCal = DateEntry(window)
endCal = DateEntry(window)

click_searchStock = partial(be.loadStockClicked, entry_stock, startCal, endCal)
btn_searchStock = Button(window, text="Search", width=10, command=click_searchStock)

btn_import500 = Button(window, text="Import Fortune 500", width = 15, command=be.importStockClicked)

startData_lbl.grid(column=0, row=1)
endDate_lbl.grid(column=0, row=2)
endCal.grid(column=1, row=2)
startCal.grid(column=1, row=1)
lbl_searchText.grid(column=0, row=0)
btn_searchStock.grid(column=2, row=0)
entry_stock.grid(column=1, row=0)
btn_import500.grid(column=5, row=0)

window.mainloop()