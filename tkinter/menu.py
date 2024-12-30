import tkinter as tk
def select1():
    print("Bạn đã chọn menu con 'New'!")
    
def select2():
    print("Bạn đã chọn menu con 'Open'!")
    
def select3():
    print("Bạn đã chọn menu con 'Cut'!")

def select4():
    print("Bạn đã chọn menu con 'Copy'!")

def select5():
    print("Bạn đã chọn menu con 'Paste'!")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Menu Example")
root.geometry('300x80')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=select1)
file_menu.add_command(label="Open", command=select2)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=select3)
edit_menu.add_command(label="Copy", command=select4)
edit_menu.add_command(label="Paste", command=select5)

root.mainloop()

