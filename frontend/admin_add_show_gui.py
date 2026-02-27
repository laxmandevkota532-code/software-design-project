import tkinter as tk
from tkinter import messagebox
from backend.admin_services import add_show, get_all_movies

# Show 

def open_add_show():

    window = tk.Toplevel()
    window.title("Add Show")
    window.geometry("400x400")

    movies = get_all_movies()

    if not movies:
        messagebox.showerror("Error", "No movies available. Add movie first.")
        return

    movie_dict = {m[1]: m[0] for m in movies}
    movie_names = list(movie_dict.keys())

    selected_movie = tk.StringVar(window)
    selected_movie.set(movie_names[0])

    tk.Label(window, text="Select Movie").pack()
    tk.OptionMenu(window, selected_movie, *movie_names).pack()

    tk.Label(window, text="Show Date (YYYY-MM-DD)").pack()
    date_entry = tk.Entry(window)
    date_entry.pack()

    tk.Label(window, text="Show Time (HH:MM)").pack()
    time_entry = tk.Entry(window)
    time_entry.pack()

    tk.Label(window, text="Ticket Price").pack()
    price_entry = tk.Entry(window)
    price_entry.pack()

    def handle_add_show():
        movie_id = movie_dict[selected_movie.get()]
        show_date = date_entry.get()
        show_time = time_entry.get()
        price = price_entry.get()

        if not show_date or not show_time or not price:
            messagebox.showerror("Error", "All fields required")
            return

        add_show(movie_id, show_date, show_time, float(price))
        messagebox.showinfo("Success", "Show Added Successfully")

        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    tk.Button(window, text="Add Show",
              command=handle_add_show).pack(pady=20)