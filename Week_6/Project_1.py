import tkinter as tk
from tkinter import messagebox

def button_click():

    messagebox.showinfo("Simi Services", "Welcome to 'Simi Services! \nYour number one delivery service, nationwide!")
    
root = tk.Tk()
root.title("Simi Services")
root.geometry("500x200")
root.config(bg = "Orange")

label = tk.Label(root, text = "Welcome, esteemed customer. \nPlease input the weight of your package, and the location of your delivery.")
label.pack()
label.config(fg = "Black", bg = "Orange")


weight = tk.Label(root, text = "Weight (kg)")
weight.pack()
weight.config(fg = "Black", bg = "Orange")
weight_input = tk.Entry(root)
weight_input.pack()

location = tk.Label(root, text = "Location")
location.pack()
location.config(fg = "Black", bg = "Orange")
location_input = tk.Entry(root)
location_input.pack()

def details():
    weight = int(weight_input.get())
    location = location_input.get()

    if weight >= 10 and location == "Ibeju-Lekki":
        messagebox.showinfo("Price", "Your delivery fee is N5,000.")
    elif weight < 10 and location == "Ibeju-Lekki":
        messagebox.showinfo("Price", "Your delivery fee is N3,500.")
    elif weight >= 10 and location == "Epe":
        messagebox.showinfo("Price", "Your delivery fee is N10,000.")
    elif weight < 10 and location == "Epe":
        messagebox.showinfo("Price", "Your delivery fee is N5,000.")
    else:
        messagebox.showerror("Notice", "Unfortunately, your location is not yet availabe for our services.")

proceed = tk.Button(root, text = "Proceed", command = details)
proceed.pack()

root.mainloop()