import os
import tkinter as tk
from tkinter import messagebox, ttk

# Create the main application window
root = tk.Tk()
root.title("Home Screen")
root.geometry("500x350")  # Adjust the size for better layout

# Function placeholders
def add_user(): os.system('python add_faces.py')
def delete_user(): os.system('python delete_users.py')
def show_users(): os.system('python show_users.py')
def take_attendance(): os.system('python main.py')

# Improved styling
def apply_styling():
    style = ttk.Style()
    style.theme_use('clam')  # 'clam' theme tends to look better on most platforms

    # Button style
    style.configure('TButton', background="#333333", foreground="white",
                    font=('Arial', 12, 'bold'), padding=10, relief="flat",
                    borderwidth=0)
    style.map('TButton', background=[('active', '#666666')])  # Change color on hover

    # Frame style
    style.configure('TFrame', background="white")

    # Label style
    style.configure('TLabel', background="white", foreground="#333333",
                    font=('Arial', 14, 'bold'))

# Apply the custom styling
apply_styling()

# Main frame
main_frame = ttk.Frame(root, padding="30 20 30 20")
main_frame.pack(expand=True, fill='both')

# Welcome label
welcome_label = ttk.Label(main_frame, text="Welcome to the Home Screen", anchor="center")
welcome_label.pack(side='top', pady=10)

# Spacer to move the button section down
spacer = ttk.Label(main_frame, text="", background="white")
spacer.pack(pady=15)  # Adjust the pady value to move the button section down more or less

# Button creation function
def create_button(parent, text, command):
    return ttk.Button(parent, text=text, command=command)

# Buttons
add_button = create_button(main_frame, "Add User", add_user)
add_button.pack(fill="x", padx=10, pady=5)

delete_button = create_button(main_frame, "Delete User", delete_user)
delete_button.pack(fill="x", padx=10, pady=5)

show_button = create_button(main_frame, "Show Registered Users", show_users)
show_button.pack(fill="x", padx=10, pady=5)

attendance_button = create_button(main_frame, "Take Attendance", take_attendance)
attendance_button.pack(fill="x", padx=10, pady=5)

# Main application loop
root.mainloop()
