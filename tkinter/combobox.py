import tkinter as tk
from tkinter import ttk


class Combobox:
    def __init__(self, root):
        self.root = root
        self.root.title("Wellcome to Uneti App")
        self.root.geometry('350x80')
    
        self.options=['DL16A1',['DL16A2'],['DL17A1'],['DL17A2'],['DL17A3']]
        
        self.teacher_label = tk.Label(root,text=('Teacher'))
        self.teacher_label.grid(row=0,column=0,padx=5,pady=5)
        
        self.teacher_textbox = tk.Text(root,height=1,width=20)
        self.teacher_textbox.grid(row=0,column=1,padx=5,pady=20)
        
        self.label = tk.Label(root,text=('class'))
        self.label.grid(row=1,column=0,padx=5,pady=5)
        
        self.Combobox = ttk.Combobox(root,values=self.options)
        self.Combobox.grid(row=1,column=1,padx=5,pady=5)
        
        self.Combobox.bind("<<ComboboxSelected>>",self.on_select)
        
    def on_select(self,event):
        selected_value = self.combobox.get()
        print("Selected:", selected_value)
root = tk.Tk()
app = Combobox(root)
root.mainloop()