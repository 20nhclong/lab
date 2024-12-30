import tkinter as tk
from tkinter import Spinbox

def on_spinbox_changed():
    value = spinbox.get()
    label2.config(text="Giá trị đã chọn: " + value)

root = tk.Tk()
root.title("SpinBox Example")
root.geometry('300x80')

spinbox = Spinbox(root, from_=1, to=10, increment=1, width=10)

spinbox.grid(row=0, column=3)
label1 = tk.Label(root, text=" Chọn giá trị:", anchor="e")
label1.grid(row=0, column=0, padx=5, pady=5)
label2 = tk.Label(root, text="Giá trị đã chọn là:", width=20,anchor="e")
label2.grid(row=1, column=2, padx=5, pady=5, columnspan=2)
button = tk.Button(root, text="Kết quả", width=5,command=on_spinbox_changed)
button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

root.mainloop()
