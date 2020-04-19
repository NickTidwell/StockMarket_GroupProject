from tkinter import *
import buttonEvents as be
from functools import partial
from pandastable import Table
from tkcalendar import Calendar, DateEntry


window = Tk()
window.geometry('600x400')
window.title("Python Stock Market")


lbl_searchText = Label(window, text="Enter Stock To Display: ")
startData_lbl = Label(window, text="Start Day")
endDate_lbl = Label(window, text="End Date")
lbl_importName = Label(window, text="Enter stock to import")
entry_import = Entry(window, width = 15)

entry_stock = Entry(window, width = 15)

startCal = DateEntry(window)
endCal = DateEntry(window)

click_searchStock = partial(be.loadStockClicked, entry_stock)
btn_searchStock = Button(window, text="Display Data", width=10, command=click_searchStock)

click_graph = partial(be.plotStock, entry_stock)
btn_graph = Button(window, text="Graph Data", width=15, command=click_graph)

click_import = partial(be.importSingleStock, entry_import, startCal, endCal)
btn_import = Button(window, text="Import", width=10, command=click_import)

btn_import500 = Button(window, text="Import Fortune 500", width = 15, command=be.importStockClicked)


lbl_searchText.grid(column=0, row=0)
btn_searchStock.grid(column=2, row=0)
entry_stock.grid(column=1, row=0)
btn_import500.grid(column=3, row=2)
btn_graph.grid(column=3,row=0)


lbl_importName.grid(column=0,row=2)
entry_import.grid(column=1,row=2)
startData_lbl.grid(column=0, row=3)
endDate_lbl.grid(column=0, row=4)
btn_import.grid(column=2, row=2)
endCal.grid(column=2, row=4)
startCal.grid(column=2, row=3)
window.mainloop()