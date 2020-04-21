from tkinter import *
from tkinter import ttk
import buttonEvents as be
from functools import partial
from pandastable import Table
from tkcalendar import Calendar, DateEntry

window = Tk()
window.geometry('600x400')
window.title("Python Stock Market")



lbl_searchText = Label(window, text="Enter Stock To Display: ", width=20, anchor="w")
startData_lbl = Label(window, text="Start Day")
endDate_lbl = Label(window, text="End Date")
lbl_importName = Label(window, text="Enter Stock To Import:", width=20, anchor="w")
status_text = StringVar()
lbl_importStatus = Label(window, width=15,textvariable=status_text)
entry_import = Entry(window, width = 15)


startCal = DateEntry(window)
endCal = DateEntry(window)

tkvar = StringVar()
cb_stockList = ttk.Combobox(window, width=15, values=be.updateStockList(), textvariable=tkvar)

click_searchStock = partial(be.loadStockClicked, cb_stockList)
btn_searchStock = Button(window, text="Display Data", width=10, command=click_searchStock)

click_graph = partial(be.plotStock, cb_stockList)
btn_graph = Button(window, text="Graph Data", width=15, command=click_graph)

click_predictGraph = partial(be.graphPrediction, cb_stockList)
btn_predictGraph = Button(window, text="Predict Data", width=15, command=click_predictGraph)

click_import = partial(be.importSingleStock, entry_import, startCal, endCal, status_text)
btn_import = Button(window, text="Import", width=10, command=click_import)

btn_import500 = Button(window, text="Import Fortune 500", width = 15, command=be.importStockClicked)


lbl_searchText.grid(column=0, row=0)
btn_searchStock.grid(column=2, row=0)
cb_stockList.grid(column=1, row=0)
btn_import500.grid(column=3, row=2)
btn_graph.grid(column=3,row=0)
btn_predictGraph.grid(column=4,row=0)
lbl_importStatus.grid(column=4,row=2)

lbl_importName.grid(column=0,row=2)
entry_import.grid(column=1,row=2)
startData_lbl.grid(column=0, row=3)
endDate_lbl.grid(column=0, row=4)
btn_import.grid(column=2, row=2)
endCal.grid(column=2, row=4)
startCal.grid(column=2, row=3)
window.mainloop()