from tkinter import *
from buttonEvents import clicked, loadStockClicked
from functools import partial
from pandastable import Table
from tkcalendar import Calendar, DateEntry


window = Tk()
window.geometry('600x400')
window.title("Python Stock Market")


lbl = Label(window, text="Search New Stock")
startData_lbl = Label(window, text="Pick Start Day")
endDate_lbl = Label(window, text="Pick End Date")

txt = Entry(window, width = 15)

startCal = DateEntry(window)
endCal = DateEntry(window)

clicked_w_args = partial(loadStockClicked, txt, startCal, endCal)
btn = Button(window, text="Search", width=10, command=clicked_w_args)

startData_lbl.grid(column=0, row=1)
endDate_lbl.grid(column=0, row=2)
endCal.grid(column=1, row=2)
startCal.grid(column=1, row=1)
lbl.grid(column=0, row=0)
btn.grid(column=1, row=0)
txt.grid(column=2, row=0)

window.mainloop()