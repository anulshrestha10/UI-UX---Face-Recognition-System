import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, ttk


# Improved styling
def create_styled_widgets(root):
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="light gray")
    style.configure("TEntry", font=("Arial", 12), padding=5)
    style.configure("TButton", font=("Arial", 12), background="light blue", foreground="black")

    root.configure(background="light gray")

# Dummy database 
users = {"anul": "shrestha"}



def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")     
        root.destroy()  # Close the login window
        open_ui_interface(username)
        return username
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def signup():
    signup_window = tk.Toplevel(root, background="light gray")
    signup_window.title("Signup")
    create_styled_widgets(signup_window)  # Apply styles to widgets

    signup_username_label = ttk.Label(signup_window, text="Username:")
    signup_username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    signup_username_entry = ttk.Entry(signup_window)
    signup_username_entry.grid(row=0, column=1, padx=10, pady=5)

    signup_password_label = ttk.Label(signup_window, text="Password:")
    signup_password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    signup_password_entry = ttk.Entry(signup_window, show="*")
    signup_password_entry.grid(row=1, column=1, padx=10, pady=5)

    def confirm_signup():
        new_username = signup_username_entry.get()
        new_password = signup_password_entry.get()
        users[new_username] = new_password
        messagebox.showinfo("Signup Successful", "Account created successfully!")
        signup_window.destroy()

    signup_button = ttk.Button(signup_window, text="Signup", command=confirm_signup)
    signup_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")



# Create the main application window
root = tk.Tk()
root.title("Login")
create_styled_widgets(root)  # Apply styles to widgets

username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = ttk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

signup_button = ttk.Button(root, text="Signup", command=signup)
signup_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
# ...


def open_ui_interface(username):
    os.system(f'"{sys.executable}" UI.py')

root.mainloop()