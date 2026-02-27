import tkinter as tk
from frontend.admin_add_movie_gui import open_add_movie
from frontend.admin_add_show_gui import open_add_show
from frontend.admin_view_bookings_gui import open_view_bookings
from frontend.admin_view_revenue_gui import open_view_revenue

# Admin Dashboard

def open_admin_dashboard():

    window = tk.Toplevel()
    window.title("Admin Dashboard")
    window.geometry("700x500")

    sidebar = tk.Frame(window, bg="#3f72af", width=200)
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="Admin",
             bg="#3f72af",
             fg="white",
             font=("Arial", 16, "bold")).pack(pady=20)

    tk.Button(sidebar, text="Add Movie", width=20,
              command=open_add_movie).pack(pady=5)

    tk.Button(sidebar, text="Add Show", width=20,
              command=open_add_show).pack(pady=5)

    tk.Button(sidebar, text="View Bookings", width=20,
              command=open_view_bookings).pack(pady=5)

    tk.Button(sidebar, text="View Revenue", width=20,
              command=open_view_revenue).pack(pady=5)

    main_area = tk.Frame(window, bg="white")
    main_area.pack(side="right", expand=True, fill="both")

    tk.Label(main_area,
             text="Welcome to Admin Dashboard",
             font=("Arial", 20),
             bg="white").pack(pady=100)