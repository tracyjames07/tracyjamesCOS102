import csv
import tkinter as tk
from tkinter import messagebox

def load_csv(datapath):
    dataset = []
    with open(datapath, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataset.append(row)
    return dataset

datapath = 'C:\Users\there\OneDrive\Desktop\tracyjamesCOS102\Week_5\GIG-logistics.csv'
datasheet = load_csv(datapath)

def checkUser(arr, surname, firstname, department):
    found = False
    for elements in arr:
        if (elements[1:] == [surname, firstname, department]):
            found = True
            break
    if (found == True):
        messagebox.showinfo("Welcome {firstname}")
        displayothermembers(arr, department)
    else:
        messagebox.showinfo("This employee is nonexixstent.")

def displayothermembers(arr, deparment):
    membersArr = []
    for values in arr:
        if (values[3] == deparment):
            members = f"Firstname: {values[1]} Surname: {values[2]} Department: {values[3]} \n"
            membersArr.append(members)
    messagebox.showinfo("Members", membersArr)

def button_click():
    results = messagebox.askyesno("Confirmation. Do you want to submit?")
    if results: 
        userInput()

def userInput():
    surname = surname_entry.get()
    firstname = firstname_entry.get()
    department = department_entry.get()
    messagebox.showinfo("Data obtained successfully.")
    messagebox.showinfo("Assessing validity...")
    checkUser(datasheet, surname, firstname, department)

root = tk.Tk()
root.title("Validation Page")
root.geometry("300x200")

surname_label = tk.Label(root, text = "Enter your surname: ")
surname_label.pack()
surname_entry = tk.Entry(root)
surname_entry.pack()

firstname_label = tk.Label(root, text = "Enter your firstname: ")
firstname_label.pack()
firstname_entry = tk.Entry(root)
firstname_entry.pack()

department_label = tk.Label(root, text = "Enter your department: ")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

submit_button = tk.Button(root, text = "Submit", command = button_click)
submit_button.pack()

root.mainloop()