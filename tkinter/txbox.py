import tkinter as tk

class UnetiApp:
    def __init__(self, root):
        self.root = root
        
        self.root.title("Welcome to Uneti app")
        self.root.geometry('500x100')
        
        self.lbl1 = tk.Label(root, text="Giảng viên:")
        self.lbl1.grid(column=0, row=0)
        self.txt1 = tk.Entry(root, width=30)
        self.txt1.grid(column=1, row=0)
        self.txt1.focus()
        
        self.lbl2 = tk.Label(root, text="Bộ môn:")
        self.lbl2.grid(column=0, row=2)
        self.txt2 = tk.Entry(root, width=30)
        self.txt2.grid(column=1, row=2)
        self.txt2.focus()
        
        self.lbl3 = tk.Label(root, text="HP giảng dạy:")
        self.lbl3.grid(column=0, row=3)
        self.txt3 = tk.Entry(root, width=30)
        self.txt3.grid(column=1, row=3)
        self.txt3.focus()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = UnetiApp(root)
    root.mainloop()