import tkinter as tk
from backend.admin_services import get_all_bookings

# View Bookings

def open_view_bookings():

    window = tk.Toplevel()
    window.title("All Bookings")
    window.geometry("600x400")

    tk.Label(window, text="All Bookings",
             font=("Arial", 16, "bold")).pack(pady=10)

    bookings = get_all_bookings()

    listbox = tk.Listbox(window, width=80)
    listbox.pack(pady=10)

    if not bookings:
        listbox.insert(tk.END, "No bookings yet.")
        return

    for b in bookings:
        booking_id, movie, date, time, price = b
        row = f"ID:{booking_id} | {movie} | {date} {time} | Rs.{price}"
        listbox.insert(tk.END, row)