from tkinter import *
from buttonEvents import clicked, loadStockClicked
from functools import partial


window = Tk()
window.geometry('1000x1000')
window.title("Python Stock Market")



lbl = Label(window, text="Search New Stock")
txt = Entry(window, width = 10)

clicked_w_args = partial(loadStockClicked, txt, window)
btn = Button(window, text="Search", command=clicked_w_args)

lbl.grid(column=0, row=0)
btn.grid(column=1, row=0)
txt.grid(column=2, row=0)

window.mainloop()