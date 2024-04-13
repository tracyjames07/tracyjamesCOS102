import tkinter as tk
from tkinter import messagebox

def welcomeMessage(username):
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text = f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text = "This is Python GUI with Tkinter.")
    label_2.pack()

    root.mainloop()

def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "COS102":
        welcomeMessage(username)

    else:
        messagebox.showerror("Login", "Invalid username or password.")

root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

username_label = tk.Label(root, text = "Username: ")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text = "Password: ")
password_label.pack()
password_entry = tk.Entry(root, show = "*")
password_entry.pack()

submit_button = tk.Button(root, text = "Submit", command = submit)
submit_button.pack()

root.mainloop()