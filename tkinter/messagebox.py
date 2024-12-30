from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Welcome to KHƯD app")
window.geometry('350x200')

def clicked():
    messagebox.showinfo('BM Toán ứng dụng', 'Đây là messageBox cc!')
    
btn = Button(window,text='Bấm vào đây', command=clicked)
btn.grid(column=0,row=0)

window.mainloop()