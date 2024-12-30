from tkinter import *

window = Tk()

label =Label(window,text=("Hello"),font=("arial bold",50))
label.pack()

window.title("Wellcome to Uneti")

label.grid(column = 0,row = 0)

window.geometry('500x100')

window.mainloop()
