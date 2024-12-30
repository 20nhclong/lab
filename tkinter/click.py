from tkinter import *

window = Tk()

label =Label(window,text=("Hello"))
label.pack()

window.title("Wellcome to Uneti")

label.grid(column = 0,row = 0)

window.geometry('500x100')

def click():
    label.configure(text=("click"))
    
btn = Button(window,text=("click me"),bg='green',fg='red',command=click)

btn.grid(column=5,row=0)    


window.mainloop()
