import tkinter as tk
from tkinter import messagebox

def button_click():

    messagebox.showinfo("Info", "Welcome to COS 102 GUI App!\n")

    result = messagebox.askyesno("Confirmation.", "Do you want to continue?")

root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

label = tk.Label(root, text = "Hello Friend. \n")
label.pack()

button = tk.Button(root, text = "Click Me!", command = button_click)
button.pack()

button.config(fg = "Red", bg = "Yellow")

root.mainloop()