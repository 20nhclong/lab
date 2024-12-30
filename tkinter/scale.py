import tkinter as tk
from tkinter import ttk

def on_scale_change(value):
    label.config(text=f"Giá trị: {value}")
    
    
root = tk.Tk()
root.title("Scale Example")
root.geometry("300x100")

scale = tk.Scale(root, from_=0, to=100, resolution=1,orient=tk.HORIZONTAL, length=200, command=on_scale_change)
scale.set(50) 
scale.pack()

label = ttk.Label(root, text="Giá trị: 50")
label.pack()

root.mainloop()