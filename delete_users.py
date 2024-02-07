import os
import pickle
import tkinter as tk
from tkinter import Listbox, Toplevel, messagebox, simpledialog, ttk

import numpy as np


def load_data():
    with open('data/names.pkl', 'rb') as f:
        labels = pickle.load(f)
    with open('data/faces_data.pkl', 'rb') as f:
        faces_data = pickle.load(f)
    return labels, faces_data

def save_data(labels, faces_data):
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(labels, f)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)

def delete_user(user_name):
    labels, faces_data = load_data()
    try:
        indices_to_delete = [i for i, name in enumerate(labels) if name == user_name]
        if indices_to_delete:
            labels = [label for i, label in enumerate(labels) if i not in indices_to_delete]
            faces_data = np.delete(faces_data, indices_to_delete, axis=0)
            save_data(labels, faces_data)
            messagebox.showinfo("Success", f"User '{user_name}' deleted successfully.")
        else:
            messagebox.showwarning("Not Found", f"User '{user_name}' not found in the dataset.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    user_entry.delete(0, tk.END)  # Clear the entry field after deletion

def show_users():
    labels, _ = load_data()
    users_window = Toplevel(root)
    users_window.title("Registered Users")
    users_window.geometry("200x300")
    listbox = Listbox(users_window)
    listbox.pack(fill=tk.BOTH, expand=True)
    for user in labels:
        listbox.insert(tk.END, user)

# GUI setup
root = tk.Tk()
root.title("Delete User")
root.geometry("400x250")

# Styling
root.configure(bg='#f0f0f0')
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=6)
style.configure("TEntry", font=("Arial", 12), padding=6)

# User deletion input
user_label = ttk.Label(root, text="User Name:", font=("Arial", 12, "bold"))
user_label.pack(pady=(20, 0))

user_entry = ttk.Entry(root, font=("Arial", 12))
user_entry.pack(pady=5)

delete_button = ttk.Button(root, text="Delete User", command=lambda: delete_user(user_entry.get()))
delete_button.pack(pady=(10, 20))

# Show Users Button
show_button = ttk.Button(root, text="Show Users", command=show_users)
show_button.pack(pady=10)

root.mainloop()
