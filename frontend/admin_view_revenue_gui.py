import tkinter as tk
from backend.admin_services import get_total_revenue


# View rEvenue

def open_view_revenue():

    window = tk.Toplevel()
    window.title("Total Revenue")
    window.geometry("400x200")

    total = get_total_revenue()

    tk.Label(
        window,
        text=f"Total Revenue: Rs. {total}",
        font=("Arial", 18, "bold")
    ).pack(pady=50)