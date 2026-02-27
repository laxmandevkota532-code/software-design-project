import tkinter as tk
from tkinter import messagebox
from backend.user_service import (
    get_all_movies,
    search_movies,
    get_movie_by_id,
    get_shows_by_movie,
    create_booking,
    get_user_bookings
)


def open_user_app(user_id=1):

    #  Window Set up 

    window = tk.Tk()
    window.title("Movie Ticket Booking System")
    window.geometry("1100x650")
    window.configure(bg="#f8fafc")

#  Sidebar
#  
    sidebar = tk.Frame(window, bg="#1e293b", width=230)
    sidebar.pack(side="left", fill="y")

    tk.Label(
        sidebar,
        text="🎬 Movie Booking",
        bg="#1e293b",
        fg="white",
        font=("Arial", 18, "bold")
    ).pack(pady=30)

    #  Main Content 

    content = tk.Frame(window, bg="#f8fafc")
    content.pack(side="right", fill="both", expand=True)

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    #  Sidebar Button Helper 

    def sidebar_button(text, command):
        return tk.Button(
            sidebar,
            text=text,
            width=22,
            height=2,
            bg="#334155",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief="flat",
            command=command
        )

    # Dashboard 

    def show_dashboard():
        clear_content()

        tk.Label(
            content,
            text="Welcome, User!",
            font=("Arial", 24, "bold"),
            bg="#f8fafc"
        ).pack(pady=40)

        tk.Button(
            content,
            text="View All Movies",
            width=25,
            height=2,
            bg="#2563eb",
            fg="white",
            relief="flat",
            command=show_movies
        ).pack(pady=10)

        tk.Button(
            content,
            text="My Bookings",
            width=25,
            height=2,
            bg="#2563eb",
            fg="white",
            relief="flat",
            command=show_bookings
        ).pack(pady=10)

    #    Movie List 

    def show_movies():
        clear_content()

        tk.Label(
            content,
            text="Movies",
            font=("Arial", 20, "bold"),
            bg="#f8fafc"
        ).pack(pady=20)
     # Search Section

        search_frame = tk.Frame(content, bg="#f8fafc")
        search_frame.pack(pady=10)

        search_entry = tk.Entry(search_frame, width=40, font=("Arial", 11))
        search_entry.pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="Search",
            bg="#2563eb",
            fg="white",
            relief="flat",
            command=lambda: display_movies(
                search_movies(search_entry.get())
            )
        ).pack(side="left")

        display_movies(get_all_movies())

    def display_movies(movies):

        if not movies:
            tk.Label(content, text="No movies found.",
                     bg="#f8fafc").pack()
            return

        for movie in movies:
            movie_id, title, duration, genre = movie

            row = tk.Frame(
                content,
                bg="white",
                highlightbackground="#e5e7eb",
                highlightthickness=1
            )
            row.pack(fill="x", padx=80, pady=10)

            tk.Label(
                row,
                text=title,
                font=("Arial", 14, "bold"),
                bg="white"
            ).pack(anchor="w", padx=15, pady=(10, 0))

            tk.Label(
                row,
                text=f"{duration} mins • {genre}",
                bg="white",
                fg="gray"
            ).pack(anchor="w", padx=15)

            tk.Button(
                row,
                text="View Details",
                bg="#2563eb",
                fg="white",
                relief="flat",
                padx=15,
                command=lambda m_id=movie_id: show_details(m_id)
            ).pack(anchor="e", padx=15, pady=10)


    # Movie Detailsw

    def show_details(movie_id):
        clear_content()

        movie = get_movie_by_id(movie_id)

        if not movie:
            tk.Label(content, text="Movie not found",
                     bg="#f8fafc").pack()
            return

        id, title, description, duration, genre = movie


        tk.Label(
            content,
            text=title,
            font=("Arial", 22, "bold"),
            bg="#f8fafc"
        ).pack(pady=15)

        tk.Label(
            content,
            text=f"{duration} mins • {genre}",
            bg="#f8fafc"
        ).pack()

        tk.Label(
            content,
            text=description,
            wraplength=700,
            justify="left",
            bg="#f8fafc"
        ).pack(pady=15)

        tk.Label(
            content,
            text="Show Timings",
            font=("Arial", 16, "bold"),
            bg="#f8fafc"
        ).pack(pady=10)

        shows = get_shows_by_movie(movie_id)

        if not shows:
            tk.Label(content, text="No shows available.",
                     bg="#f8fafc").pack()
        else:
            for show in shows:
                show_id, show_time, price = show

                tk.Button(
                    content,
                    text=f"{show_time}  |  ${price}",
                    bg="#2563eb",
                    fg="white",
                    relief="flat",
                    width=25,
                    command=lambda s_id=show_id, p=price:
                        book_ticket(s_id, p)
                ).pack(pady=6)

        tk.Button(
            content,
            text="Back",
            command=show_movies
        ).pack(pady=20)

    # Book Ticket

    def book_ticket(show_id, price):
        seats = "A1"
        total = price

        create_booking(user_id, show_id, seats, total)

        messagebox.showinfo("Success", "Ticket Booked Successfully!")
        show_bookings()

    #  Booking History
    def show_bookings():
        clear_content()

        tk.Label(
            content,
            text="Booking History",
            font=("Arial", 20, "bold"),
            bg="#f8fafc"
        ).pack(pady=20)

        bookings = get_user_bookings(user_id)

        if not bookings:
            tk.Label(content, text="No bookings yet.",
                     bg="#f8fafc").pack()
            return

        for booking in bookings:
            booking_id, title, show_time, seats, total = booking

            row = tk.Frame(
                content,
                bg="white",
                highlightbackground="#e5e7eb",
                highlightthickness=1
            )
            row.pack(fill="x", padx=80, pady=8)

            tk.Label(
                row,
                text=f"{title} | {show_time} | Seats: {seats} | ${total}",
                bg="white"
            ).pack(padx=10, pady=10)

# Sidebar Buttons
    sidebar_button("Dashboard", show_dashboard).pack(pady=8)
    sidebar_button("All Movies", show_movies).pack(pady=8)
    sidebar_button("My Bookings", show_bookings).pack(pady=8)

    show_dashboard()
    window.mainloop()