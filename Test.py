import tkinter as tk
from tkinter import messagebox
import os
import subprocess

USER_FILE = "users.txt"  # File to store user credentials

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if validate_credentials(username, password):
        messagebox.showinfo("Login Successful", "Redirecting to Application")
        login_window.destroy()
        subprocess.Popen(["python", "FingerVein.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")


# Function to handle registration
def register():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    if username and password:
        if save_credentials(username, password):
            messagebox.showinfo("Registration Successful", "You can now log in.")
            register_window.destroy()
        else:
            messagebox.showerror("Registration Failed", "Username already exists.")
    else:
        messagebox.showerror("Registration Failed", "Please fill in all fields.")

# Function to validate credentials
def validate_credentials(username, password):
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if stored_username == username and stored_password == password:
                    return True
    return False

# Function to save credentials
def save_credentials(username, password):
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(",")
                if stored_username == username:
                    return False  # Username already exists
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")
    return True

# Function to open the registration window
def open_register_window():
    global register_window, reg_username_entry, reg_password_entry
    register_window = tk.Toplevel(login_window)
    register_window.title("Register")
    register_window.geometry("400x300")

    tk.Label(register_window, text="Register", font=('Times', 20, 'bold')).pack(pady=10)

    tk.Label(register_window, text="Username:", font=('Times', 14)).pack(pady=5)
    reg_username_entry = tk.Entry(register_window, font=('Times', 14))
    reg_username_entry.pack(pady=5)

    tk.Label(register_window, text="Password:", font=('Times', 14)).pack(pady=5)
    reg_password_entry = tk.Entry(register_window, show="*", font=('Times', 14))
    reg_password_entry.pack(pady=5)

    register_button = tk.Button(register_window, text="Register", font=('Times', 14), command=register)
    register_button.pack(pady=10)

# Function to open the login window
def open_login_window():
    global login_window, username_entry, password_entry
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x300")

    tk.Label(login_window, text="Login", font=('Times', 20, 'bold')).pack(pady=10)

    tk.Label(login_window, text="Username:", font=('Times', 14)).pack(pady=5)
    username_entry = tk.Entry(login_window, font=('Times', 14))
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:", font=('Times', 14)).pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", font=('Times', 14))
    password_entry.pack(pady=5)

    login_button = tk.Button(login_window, text="Login", font=('Times', 14), command=login)
    login_button.pack(pady=10)

    register_button = tk.Button(login_window, text="Register", font=('Times', 14), command=open_register_window)
    register_button.pack(pady=5)

    login_window.mainloop()

# Entry point: Create login window
if __name__ == "__main__":
    open_login_window()
