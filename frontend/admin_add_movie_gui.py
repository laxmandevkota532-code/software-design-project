import tkinter as tk
from tkinter import messagebox
from backend.admin_services import add_movie

# Add movie
def open_add_movie():

    window = tk.Toplevel()
    window.title("Add Movie")
    window.geometry("400x400")

    def handle_add_movie():
        title = name_entry.get()
        description = desc_entry.get()
        duration = duration_entry.get()
        genre = genre_entry.get()

        if not title or not description or not duration or not genre:
            messagebox.showerror("Error", "All fields are required")
            return

        add_movie(title, description, duration, genre)
        messagebox.showinfo("Success", "Movie Added Successfully")

        name_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
        genre_entry.delete(0, tk.END)

    tk.Label(window, text="Add Movie", font=("Arial", 18)).pack(pady=15)

    tk.Label(window, text="Movie Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Description").pack()
    desc_entry = tk.Entry(window)
    desc_entry.pack()

    tk.Label(window, text="Duration").pack()
    duration_entry = tk.Entry(window)
    duration_entry.pack()

    tk.Label(window, text="Genre").pack()
    genre_entry = tk.Entry(window)
    genre_entry.pack()

    tk.Button(window, text="Add Movie",
              command=handle_add_movie).pack(pady=15)