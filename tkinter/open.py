import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    
def open_folder():
    folder_path = filedialog.askdirectory()
    print("Selected folder:", folder_path)
    
root = tk.Tk()
root.title('Demo mở file, thư mục.')
root.geometry('300x80')
open_file=tk.Button(root,text="Open File", command=open_file)
open_file.pack(padx=5,pady=5)
open_folder=tk.Button(root, text="Open Folder", command=open_folder)
open_folder.pack(padx=5, pady=5)

root.mainloop()