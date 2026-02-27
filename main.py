import tkinter as tk
from frontend.admin_dashboard_gui import open_admin_dashboard
from frontend.user_app import open_user_app   # make sure this function exists

def open_admin():
    open_admin_dashboard()

def open_user():
    open_user_app()

root = tk.Tk()
root.title("System Panel")
root.geometry("300x200")

tk.Label(root, text="Select Panel", font=("Arial", 14)).pack(pady=20)

tk.Button(root, text="Admin Panel", width=20, command=open_admin).pack(pady=10)
tk.Button(root, text="User Panel", width=20, command=open_user).pack(pady=10)

root.mainloop()