import tkinter as tk

class ListBoxExample:
    def __init__(self, root):
        self.root = root
        self.root.title("ListBox Example")
        self.root.geometry('300x250')
        
        self.create_widgets()

    def create_widgets(self):
        self.lbl = tk.Label(root, text="Học phần:")
        self.lbl.pack()   
        
        hoc_phan=['ĐSTT','Giải tích','Xác suất TK', 'Lập trình R','Lập trình Python',
                  'Toán RR', 'Cơ sở DL','Cấu trúc DL &GT', 'Thống kê', 'SQL']
        
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.listbox.pack()
        
        for i in hoc_phan:
            self.listbox.insert(tk.END, f"{i}")
            self.select_button = tk.Button(self.root, text="Select",command=self.on_select)
            self.select_button.pack(pady=10)
        
        def on_select(self):
            selected_items = [self.listbox.get(index) for index in
            self.listbox.curselection()]
            print("Selected Items:", selected_items)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ListBoxExample(root)
    root.mainloop()
        
        