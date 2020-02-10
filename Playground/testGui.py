from tkinter import *


window = Tk()
window.geometry('350x200')
window.title("Welcome to LikeGeeks app")
lbl = Label(window, text="Hello")
btn = Button(window, text="Click Me", command=clicked)
txt = Entry(window, width = 10)

lbl.grid(column=0, row=0)
btn.grid(column=1, row=0)
txt.grid(column=2, row = 0)

window.mainloop()

