import pickle
import tkinter as tk
from tkinter import messagebox, ttk


def load_and_show_users():
    try:
        with open('data/names.pkl', 'rb') as f:
            registered_users = pickle.load(f)
        # Clear the Listbox before inserting new items
        users_listbox.delete(0, tk.END)
        for user in registered_users:
            users_listbox.insert(tk.END, user)
    except FileNotFoundError:
        messagebox.showerror("Error", "The data file was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Registered Users")
root.geometry("400x300")

# Styling for the Listbox
listbox_font = ("Arial", 12)

# Users Listbox and Scrollbar setup
users_frame = ttk.Frame(root)
users_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a scrollbar and attach it to users_frame
scrollbar = ttk.Scrollbar(users_frame, orient="vertical")
users_listbox = tk.Listbox(users_frame, height=10, width=50, yscrollcommand=scrollbar.set, font=listbox_font)
scrollbar.config(command=users_listbox.yview)

# Pack the Listbox and Scrollbar into the frame
users_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

button_style = ttk.Style()
button_style.configure('Large.TButton', font=('Arial', 16, 'bold'), padding=10)

show_button = ttk.Button(root, text="Load and Show Users", style='Large.TButton', command=load_and_show_users)
show_button.pack(pady=20)

root.mainloop()
