import tkinter as tk
from tkinter import messagebox
import sqlite3

# ------- database setup --------

conn = sqlite3.connect("cinema_seats.db")
c = conn.cursor()

# creating table
c.execute("""
CREATE TABLE IF NOT EXISTS seats (
    seat_id TEXT PRIMARY KEY,
    seat_type TEXT,
    status TEXT,
    price INTEGER
)
""")

# creating booking table
c.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seat_id TEXT,
    customer_name TEXT,
    price INTEGER
)
""")

conn.commit()

c.execute("SELECT COUNT(*) FROM seats")
count = c.fetchone()[0]

if count == 0:
    already_booked = ["A1", "A4", "B3", "B8", "C2", "C9", "D4", "D7", "E2", "F5", "G1", "H3"]

    for row in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
        for col in range(1, 11):
            seat_id = row + str(col)

            if row in ["A", "B", "C"]:
                seat_type = "vip"
                price = 700
            else:
                seat_type = "normal"
                price = 250

            if seat_id in already_booked:
                status = "booked"
            else:
                status = "available"

            c.execute("INSERT INTO seats VALUES (?, ?, ?, ?)", (seat_id, seat_type, status, price))

    conn.commit()
    print("Seats added to database!")


# -------- colors -----------

blue_dark = "#1565c0"
blue_light = "#e3f0ff"
white = "#ffffff"
red_color = "#e53935"
green_color = "#43a047"
gray_color = "#90a4ae"
text_color = "#0d2a4a"

selected_seats = []


# -------- functions --------

def seat_clicked(seat_id, seat_type, price, btn):
    if seat_id in selected_seats:
        selected_seats.remove(seat_id)
        if seat_type == "vip":
            btn.config(bg="#fff8e1", fg="#6d4c00")
        else:
            btn.config(bg="#ddeeff", fg="#0d3a6e")
        print(seat_id + " removed")
    else:
        selected_seats.append(seat_id)
        btn.config(bg=blue_dark, fg=white)
        print(seat_id + " selected")

    update_summary()  


def update_summary():
    selected_label.config(text="")
    total_label.config(text="")

    if len(selected_seats) == 0:
        selected_label.config(text="No seats selected yet")
        total_label.config(text="Total: Rs. 0")
        book_button.config(state="disabled", bg=gray_color)
        return

    total = 0
    seat_text = "Seats: "

    for seat in selected_seats:
        c.execute("SELECT price FROM seats WHERE seat_id = ?", (seat,))
        result = c.fetchone()
        if result:
            total = total + result[0]
        seat_text = seat_text + seat + "  "

    selected_label.config(text=seat_text)
    total_label.config(text="Total: Rs. " + str(total))
    book_button.config(state="normal", bg=green_color)

# run when book button is clicked
def book_now():
    name = name_entry.get()

    if name == "" or name == "Enter your name":
        messagebox.showwarning("Warning", "Please enter your name first!")
        return

    if len(selected_seats) == 0:
        messagebox.showwarning("Warning", "Please select at least one seat!")
        return

    total = 0
    for seat in selected_seats:
        c.execute("SELECT price FROM seats WHERE seat_id = ?", (seat,))
        result = c.fetchone()
        if result:
            total = total + result[0]

    seats_str = ", ".join(selected_seats)
    confirm = messagebox.askyesno(
        "Confirm Booking",
        "Name: " + name + "\nSeats: " + seats_str + "\nTotal: Rs. " + str(total) + "\n\nDo you want to confirm?"
    )

    if confirm == True:
        for seat in selected_seats:
            c.execute("SELECT price FROM seats WHERE seat_id = ?", (seat,))
            result = c.fetchone()
            seat_price = result[0]

            c.execute("UPDATE seats SET status = 'booked' WHERE seat_id = ?", (seat,))

            c.execute("INSERT INTO bookings (seat_id, customer_name, price) VALUES (?, ?, ?)",
                      (seat, name, seat_price))

        conn.commit()

        for seat in selected_seats:
            if seat in all_buttons:
                all_buttons[seat].config(bg=red_color, fg=white, text="X", state="disabled")

        selected_seats.clear()
        name_entry.delete(0, tk.END)
        update_summary()

        messagebox.showinfo("Success!", "Booking confirmed!\nThank you " + name + " !")

# View bookings
def view_bookings():
    booking_window = tk.Toplevel(window)
    booking_window.title("All Bookings")
    booking_window.geometry("500x400")
    booking_window.config(bg=white)

    tk.Label(booking_window, text="All Bookings", font=("Arial", 16, "bold"),
             bg=blue_dark, fg=white, pady=10).pack(fill="x")

    c.execute("SELECT id, seat_id, customer_name, price FROM bookings")
    all_bookings = c.fetchall()

    if len(all_bookings) == 0:
        tk.Label(booking_window, text="\nNo bookings found!", font=("Arial", 12),
                 bg=white, fg=gray_color).pack(pady=20)
        return

    frame2 = tk.Frame(booking_window, bg=white)
    frame2.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame2)
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(frame2, yscrollcommand=scrollbar.set, font=("Courier", 10),
                         bg=blue_light, fg=text_color, selectbackground=blue_dark,
                         height=15, relief="flat", bd=0)

    # heading
    listbox.insert(tk.END, "  ID    Seat    Customer Name      Price")
    listbox.insert(tk.END, "  " + "-" * 50)

    for booking in all_bookings:
        bid, seat_id, cname, price = booking
        line = f"  {bid:<5}  {seat_id:<6}  {cname:<22}  Rs.{price}"
        listbox.insert(tk.END, line)

    listbox.pack(fill="both", expand=True)
    scrollbar.config(command=listbox.yview)

    # Total amount for booking
    c.execute("SELECT SUM(price) FROM bookings")
    total_collected = c.fetchone()[0]
    if total_collected is None:
        total_collected = 0

    tk.Label(booking_window, text="Total Collected: Rs. " + str(total_collected),
             font=("Arial", 11, "bold"), bg=blue_light, fg=blue_dark, pady=8).pack(fill="x", padx=10, pady=5)


# --------- main window  ----------
window = tk.Tk()
window.title("Cinema Seat Booking System")
window.geometry("950x680")
window.config(bg=blue_light)
window.resizable(True, True)

# ---- title----
title_frame = tk.Frame(window, bg=blue_dark, pady=12)
title_frame.pack(fill="x")

tk.Label(title_frame, text="Cinema Seat Booking System",
         font=("Arial", 20, "bold"), bg=blue_dark, fg=white).pack(side="left", padx=20)

tk.Label(title_frame, text="Movie: Interstellar  |  7:30 PM  |  Hall 3",
         font=("Arial", 10), bg=blue_dark, fg="#90caf9").pack(side="left", padx=10)

tk.Button(title_frame, text="View Bookings", font=("Arial", 10),
          bg=white, fg=blue_dark, relief="flat", padx=10, pady=4,
          command=view_bookings, cursor="hand2").pack(side="right", padx=15)

# ---- legend ----
legend_frame = tk.Frame(window, bg=blue_light, pady=8)
legend_frame.pack(fill="x", padx=15)

tk.Label(legend_frame, text="Legend:  ", font=("Arial", 9, "bold"),
         bg=blue_light, fg=text_color).pack(side="left")

legend_items = [
    ("#fff8e1", "#6d4c00", "  VIP - Rs.700  "),
    ("#fff8e1", "#0d3a6e", "  Normal - Rs.250  "),
    (red_color,   white,   "  Booked  "),
    (blue_dark,   white,   "  Selected  "),
    (gray_color,  white,   "  Available  "),
]

for bg, fg, text2 in legend_items:
    tk.Label(legend_frame, text=text2, font=("Arial", 9),
             bg=bg, fg=fg, relief="solid", bd=1, padx=4, pady=3).pack(side="left", padx=4)

# ----- main area------
main_frame = tk.Frame(window, bg=blue_light)
main_frame.pack(fill="both", expand=True, padx=15, pady=5)

# ---- seat grid ----
seats_frame = tk.Frame(main_frame, bg=white, relief="solid", bd=1)
seats_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

# screen label
screen_label = tk.Label(seats_frame, text="- - - - - SCREEN - - - - -",
                        font=("Arial", 10, "bold"), bg=blue_dark, fg=white, pady=6)
screen_label.pack(fill="x", padx=20, pady=(15, 8))

all_buttons = {}

canvas = tk.Canvas(seats_frame, bg=white, highlightthickness=0)
scrollbar_y = tk.Scrollbar(seats_frame, orient="vertical", command=canvas.yview)
canvas.config(yscrollcommand=scrollbar_y.set)

scrollbar_y.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

inner_frame = tk.Frame(canvas, bg=white)
canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")


def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)


inner_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_configure)

def mouse_scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)

c.execute("SELECT seat_id, seat_type, status, price FROM seats ORDER BY seat_id")
all_seats_data = c.fetchall()

# grouping seats by rows
rows_data = {}
for seat in all_seats_data:
    seat_id, seat_type, status, price = seat
    row_letter = seat_id[0]
    if row_letter not in rows_data:
        rows_data[row_letter] = []
    rows_data[row_letter].append(seat)

vip_zone_label = tk.Label(inner_frame, text="VIP ZONE  (Rs. 700 per seat) ",
                           font=("Arial", 9, "bold"), bg="#fff8e1", fg="#6d4c00",
                           pady=5, padx=10)
vip_zone_label.pack(fill="x", pady=(8, 3), padx=10)

for row_letter in ["A", "B", "C"]:
    row_frame = tk.Frame(inner_frame, bg=white, pady=3)
    row_frame.pack(padx=10, fill="x")

    # row label
    tk.Label(row_frame, text="Row " + row_letter, width=6,
             font=("Arial", 8), bg=white, fg=gray_color).pack(side="left", padx=5)

    # seat buttons
    for seat in rows_data[row_letter]:
        seat_id, seat_type, status, price = seat
        col_num = int(seat_id[1:])

        if col_num == 6:
            tk.Label(row_frame, text="  ", bg=white).pack(side="left")

        if status == "booked":
            btn_bg = red_color
            btn_fg = white
            btn_text = "X"
            btn_state = "disabled"
        else:
            btn_bg = "#fff8e1"
            btn_fg = "#6d4c00"
            btn_text = str(col_num)
            btn_state = "normal"

        btn = tk.Button(row_frame, text=btn_text, width=3, height=1,
                        bg=btn_bg, fg=btn_fg, font=("Arial", 8, "bold"),
                        relief="flat", bd=0, state=btn_state,
                        cursor="hand2" if btn_state == "normal" else "arrow",
                        disabledforeground=white)
        btn.pack(side="left", padx=2)

        if btn_state == "normal":
            btn.config(command=lambda s=seat_id, t=seat_type, p=price, b=btn: seat_clicked(s, t, p, b))

            def on_enter(e, b=btn, t=seat_type):
                if b.cget("bg") != blue_dark:
                    b.config(bg="#ffecb3" if t == "vip" else "#bbddff")

            def on_leave(e, b=btn, t=seat_type, s=seat_id):
                if s not in selected_seats:
                    b.config(bg="#fff8e1" if t == "vip" else "#ddeeff")

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

        all_buttons[seat_id] = btn

# Normal zone
normal_zone_label = tk.Label(inner_frame, text="NORMAL ZONE  (Rs. 250 per seat)",  
                              font=("Arial", 9, "bold"), bg=blue_light, fg=blue_dark,
                              pady=5, padx=10)
normal_zone_label.pack(fill="x", pady=(12, 3), padx=10)

for row_letter in ["D", "E", "F", "G", "H", "I"]:
    row_frame = tk.Frame(inner_frame, bg=white, pady=3)
    row_frame.pack(padx=10, fill="x")

    tk.Label(row_frame, text="Row " + row_letter, width=6,
             font=("Arial", 8), bg=white, fg=gray_color).pack(side="left", padx=5)

    for seat in rows_data[row_letter]:
        seat_id, seat_type, status, price = seat
        col_num = int(seat_id[1:])

        if col_num == 6:
            tk.Label(row_frame, text="  ", bg=white).pack(side="left")

        if status == "booked":
            btn_bg = red_color
            btn_fg = white
            btn_text = "X"
            btn_state = "disabled"
        else:
            btn_bg = "#ddeeff"
            btn_fg = "#0d3a6e"
            btn_text = str(col_num)
            btn_state = "normal"

        btn = tk.Button(row_frame, text=btn_text, width=3, height=1,
                        bg=btn_bg, fg=btn_fg, font=("Arial", 8, "bold"),
                        relief="flat", bd=0, state=btn_state,
                        cursor="hand2" if btn_state == "normal" else "arrow",
                        disabledforeground=white)
        btn.pack(side="left", padx=2)

        if btn_state == "normal":
            btn.config(command=lambda s=seat_id, t=seat_type, p=price, b=btn: seat_clicked(s, t, p, b))

            def on_enter2(e, b=btn):
                if b.cget("bg") != blue_dark:
                    b.config(bg="#bbddff")

            def on_leave2(e, b=btn, s=seat_id):
                if s not in selected_seats:
                    b.config(bg="#ddeeff")

            btn.bind("<Enter>", on_enter2)
            btn.bind("<Leave>", on_leave2)

        all_buttons[seat_id] = btn


# ----  booking summary ----
sidebar = tk.Frame(main_frame, bg=white, width=230, relief="solid", bd=1)
sidebar.pack(side="right", fill="y")
sidebar.pack_propagate(False)

# title of sidebar
tk.Label(sidebar, text="Booking Summary", font=("Arial", 13, "bold"),
         bg=blue_dark, fg=white, pady=10).pack(fill="x")

# customer name
tk.Label(sidebar, text="Enter your Name:", font=("Arial", 10),
         bg=white, fg=text_color, anchor="w").pack(fill="x", padx=12, pady=(15, 3))

name_entry = tk.Entry(sidebar, font=("Arial", 10), relief="solid", bd=1,
                      bg=blue_light, fg=text_color, insertbackground=blue_dark)
name_entry.pack(fill="x", padx=12, ipady=5)

# divider line
tk.Frame(sidebar, bg=blue_light, height=2).pack(fill="x", padx=12, pady=12)

# selected seats display
tk.Label(sidebar, text="Selected Seats:", font=("Arial", 10, "bold"),
         bg=white, fg=text_color, anchor="w").pack(fill="x", padx=12)

selected_label = tk.Label(sidebar, text="No seats selected yet",
                           font=("Arial", 9), bg=white, fg=gray_color,
                           anchor="w", wraplength=200, justify="left")
selected_label.pack(fill="x", padx=12, pady=(5, 0))

# divider
tk.Frame(sidebar, bg=blue_light, height=2).pack(fill="x", padx=12, pady=12)

# total price
total_label = tk.Label(sidebar, text="Total: Rs. 0",
                        font=("Arial", 13, "bold"), bg=white, fg=blue_dark)
total_label.pack(padx=12, anchor="w")

tk.Label(sidebar, text="", bg=white).pack()

# book now button
book_button = tk.Button(sidebar, text="Book Now", font=("Arial", 12, "bold"),
                         bg=gray_color, fg=white, relief="flat", pady=10,
                         state="disabled", cursor="hand2", command=book_now)
book_button.pack(fill="x", padx=12)

# clear button
def clear_all():
    for seat in selected_seats[:]:
        if seat in all_buttons:
            btn = all_buttons[seat]
            c.execute("SELECT seat_type FROM seats WHERE seat_id = ?", (seat,))
            result = c.fetchone()
            if result:
                if result[0] == "vip":
                    btn.config(bg="#fff8e1", fg="#6d4c00")
                else:
                    btn.config(bg="#ddeeff", fg="#0d3a6e")
    selected_seats.clear()
    update_summary()

tk.Button(sidebar, text="Clear Selection", font=("Arial", 9),
          bg=white, fg=gray_color, relief="flat",
          cursor="hand2", command=clear_all).pack(pady=5)

tk.Frame(sidebar, bg=blue_light, height=2).pack(fill="x", padx=12, pady=10)

tk.Label(sidebar, text="ℹ️  Note:\nVIP seats have extra\nlegroom and snacks!",
         font=("Arial", 8), bg=blue_light, fg=blue_dark,
         padx=8, pady=8, justify="left").pack(fill="x", padx=12)

# ---- status ----
status_bar = tk.Frame(window, bg=blue_dark, pady=4)
status_bar.pack(fill="x", side="bottom")

tk.Label(status_bar, text="Movie Ticket Booking System",
         font=("Arial", 8), bg=blue_dark, fg="#90caf9").pack()

window.mainloop()
conn.close()