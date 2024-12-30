import tkinter as tk
class TextEditorApp:
    def __init__(self, win):
        self.win = win 
        self.win.title("ScrollText Example")
        self.win.geometry('280x120')

        self.win.configure(background="#CCFFFF")
        self.frame1 = tk.Frame(self.win, width=100, height=40,bg='#BB0000', borderwidth=1, relief='sunken')

        self.scrollbar = tk.Scrollbar(self.frame1)
        
        self.editArea = tk.Text(self.frame1, width=30, height=3,wrap="word", yscrollcommand=self.scrollbar.set,borderwidth=0, highlightthickness=0)

        self.scrollbar.config(command=self.editArea.yview)

        self.scrollbar.pack(side="right", fill="y")

        self.editArea.pack(side="left", fill="both", expand=True)

        self.frame1.place(x=10, y=30)
        
    def run(self):
        self.win.mainloop()
        
if __name__ == "__main__":
    win=tk.Tk()
    app = TextEditorApp(win)
    app.run()