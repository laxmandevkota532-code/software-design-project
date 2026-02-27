from tkinter import *
from tkinter import messagebox
import sqlite3
import runpy
import tkinter.font as font

root = Tk()
root.title("Sign Up")
root.configure(bg="#fff")
root.resizable(True, True)
root.state('zoomed')

root.update_idletasks()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

img_width = 400
form_width = 350
form_height = 390

total_content_width = img_width + form_width + 60
start_x = (sw - total_content_width) // 2
start_y = (sh - form_height) // 2 - 30

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Title bar
a = Frame(root, width=screen_width, height=35, bg="#57a1f8").place(x=0, y=0)
title = Label(a, font=("Comic Sans MS",
              15, "bold"), bg="#57a1f8").place(x=36, y=0)
img = PhotoImage(file="logo.png")
Label(root, image=img, bg="white").place(x=50, y=50)
buttonFont = font.Font(size=14)
buttonFont1 = font.Font(size=13)


#### --------- Signup Function -----------####
def signup():
    name = username.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if not name or name == 'Username':
        messagebox.showerror('Error', 'Username is required!')
        return
    if not password or password == 'Password':
        messagebox.showerror('Error', 'Password is required!')
        return
    if password != confirm_password:
        messagebox.showerror('Error', 'Password do not match!')
        return
    if len(password) < 6:
        messagebox.showerror('Error', 'Password must be at least 6 characters')
        return

    try:
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users(
            username TEXT UNIQUE,
            password TEXT)''')
        c.execute('INSERT INTO users VALUES (?, ?)', (name, password))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Account created successfully!')
        go_to_login()
    except sqlite3.IntegrityError:
        messagebox.showerror('Error', 'Username already exists!')


def go_to_login():
    root.destroy()
    runpy.run_path('.py')


root.protocol('WM_DELETE_WINDOW', go_to_login)

#### --------- Back button ---------####
btn4 = Button(root, text="<<", width=4, bg="#57a1f8",
              border=0, fg='#fff', command=go_to_login)
btn4.place(x=20, y=40)
btn4.bind('<Enter>', lambda e: btn4.config(bg='red'))
btn4.bind('<Leave>', lambda e: btn4.config(bg='#57a1f8'))

#### --------- UI ---------####
img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=start_x, y=start_y)

frame = Frame(root, width=form_width, height=form_height, bg='#fff')
frame.place(x=start_x + img_width + 60, y=start_y)

heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

#### -------------------Username-------------####
username = Entry(frame, width=25, fg='black', border=0,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
username.place(x=30, y=80)
username.insert(0, 'Email or username')
username.bind('<FocusIn>', lambda e: username.delete(0, 'end'))
username.bind('<FocusOut>', lambda e: username.insert(0, 'Email or username')
              if username.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#### -------------------Password-------------####
code = Entry(frame, show='*', width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
code.bind('<FocusOut>', lambda e: code.insert(0, 'Password')
          if code.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#### -------------------Confirm Password-------------####
confirm_code = Entry(frame, show='*', width=25, fg='black', border=0,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind('<FocusIn>', lambda e: confirm_code.delete(0, 'end'))
confirm_code.bind('<FocusOut>', lambda e: confirm_code.insert(0, 'Confirm Password')
                  if confirm_code.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

#### --------- Show Password ---------####


def show_password():
    if code.cget('show') == '*':
        code.config(show='')
        confirm_code.config(show='')
    else:
        code.config(show='*')
        confirm_code.config(show='*')


Checkbutton(frame, text='Show password', bg='white', fg='black',
            cursor='hand2', font=('Microsoft YaHei UI Light', 9),
            command=show_password).place(x=20, y=252)

#### ---------------Button & Already have account-----------------####
Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8',
       fg='white', border=0, command=signup).place(x=35, y=295)

Label(frame, text='Already have an account?', fg='black',
      bg='white', font=('Microsoft YaHei UI Light', 10)).place(x=35, y=350)

Button(frame, width=6, text='Log in', border=0,
       bg='white', fg='#57a1f8', cursor='hand2',
       command=go_to_login).place(x=210, y=350)

root.mainloop()
