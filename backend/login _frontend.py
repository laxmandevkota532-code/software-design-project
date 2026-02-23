# from tkinter import *
# from tkinter import messagebox
# import sqlite3
# from signup_frontend import signup

# root = Tk()
# root.title("Login Page")
# root.geometry("925x500+300+200")
# root.configure(bg="#fff")
# root.resizable(False, False)

# conn = sqlite3.connect('user_data.db')
# c = conn.cursor()
# c.execute('''Create table if not exists users(
#         username TEXT,
#         password TEXT)''')
# conn.commit()
# conn.close()


# def sign_in():
#     conn = sqlite3.connect('user_data.db')
#     c = conn.cursor()

#     username = user.get()
#     password = code.get()
#     c.execute("SELECT * FROM users WHERE username=? AND password=?",
#               (username, password))
#     result = c.fetchone()
#     if result:
#         screen = Toplevel(root)
#         screen.title("App")
#         screen.geometry("925x500+300+200")
#         screen.configure(bg="#fff")

#         Label(screen, text='Welcome!', bg='#fff', font=(
#             'Calibri(body)', 20, 'bold')).pack(expand=True)
#         # screen.mainloop()
#     if not user.get():
#         messagebox.showwarning('Input Error', 'Username is Required')
#         return
#     if not code.get():
#         messagebox.showwarning('Input Error', 'Password is Required')
#         return


# img = PhotoImage(file="login.png")
# Label(root, image=img, bg="white").place(x=50, y=50)


# frame = Frame(root, width=350, height=350, bg="white")
# frame.place(x=480, y=70)

# heading = Label(root, text='Log in', fg='#57a1f8', bg='white',
#                 font=('Microsoft YaHei UI Light', 23, 'bold'))
# heading.place(x=500, y=80)

# ######## -------------------Username------------------########
# def on_enter(e):
#     user.delete(0, 'end')


# def on_leave(e):
#     name = user.get()
#     if name == '':
#         user.insert(0, 'Username')


# user = Entry(frame, width=25, fg='black', border=0,
#              bg='white', font=('Microsoft YaHei UI Light', 11))
# user.place(x=30, y=80)
# user.insert(0, 'Username')
# user.bind('<FocusIn>', on_enter)
# user.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=20, y=107)

# ########### -------------------Password------------------########
# code = Entry(frame, width=25, fg='black', border=0,
#              bg='white', font=('Microsoft YaHei UI Light', 11))
# code.place(x=30, y=150)
# code.insert(0, 'Password')
# code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
# code.bind('<FocusOut>', lambda e: code.insert(0, 'Password'))

# Frame(frame, width=295, height=2, bg='black').place(x=20, y=177)

# ######## -------------------Button------------------########
# Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8',
#        fg='white', border=0, command=sign_in).place(x=35, y=204)

# label = Label(frame, text="Don't have an account?", fg='black',
#               bg='white', font=('Microsoft YaHei UI Light', 9))
# label.place(x=35, y=250)

# sign_up = Button(frame, width=6, text='Sign up', border=2, bg='white',
#                  fg='#57a1f8', cursor='hand2', font=('Microsoft YaHei UI Light', 9)
#                  ,command=lambda: signup(root))
# sign_up.place(x=200, y=250)
# root.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3
from signup_frontend import signup

root = Tk()
root.title("Login Page")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

# Database setup
conn = sqlite3.connect('user_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT)''')
conn.commit()
conn.close()


#  dashboard function
def open_dashboard(username):
    root.withdraw()

    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("925x500+300+200")
    screen.configure(bg="#fff")
    screen.resizable(False, False)

    def on_close():
        screen.destroy()
        root.deiconify()

    screen.protocol("WM_DELETE_WINDOW", on_close)

    Label(screen, text=f'Welcome, {username}!', bg='#fff', fg='#57a1f8', font=(
        'Microsoft YaHei UI Light', 30, 'bold')).pack(pady=80)

    Label(screen, text='You have successfully logged in!', bg='#fff',
          fg='black', font=('Microsoft YaHei UI Light', 15)).pack()

    Button(screen, text='Logout', bg='#57a1f8', fg='white', border=0,
           width=20, pady=7, cursor='hand2', command=on_close).pack(pady=40)


def sign_in():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    username = user.get()
    password = code.get()

# Validating
    if not username or username == 'Username':
        messagebox.showwarning('Input Error', 'Username is Required')
        conn.close()
        return
    if not password or password == 'Password':
        messagebox.showwarning('Input Error', 'Password is Required')
        conn.close()
        return

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        open_dashboard(username)
    else:
        messagebox.showerror('Error', 'Invalid username or password!')


#### ---------UI-----------###
img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Log in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# ######## -------------------Username------------------########


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Email or username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=20, y=107)

#### --------------Password--------------####
code = Entry(frame, show='*', width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
code.bind('<FocusOut>', lambda e: code.insert(0, 'Password'))
Frame(frame, width=295, height=2, bg='black').place(x=20, y=177)


def show_password():
    if code.cget('show') == '*':
        code.config(show='')
    else:
        code.config(show='*')


check_button = Checkbutton(frame, text='show password', bg='white', fg='black',
                           cursor='hand2', font=('Microsoft YaHei UI Light', 9), command=show_password)
check_button.place(x=20, y=180)

# ######## -------------------Button------------------########
Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8',
       fg='white', border=0, command=sign_in).place(x=35, y=210,)

label = Label(frame, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=35, y=250)

sign_up = Button(frame, width=6, text='Sign up', border=2, bg='white', fg='#57a1f8',
                 cursor='hand2', font=('Microsoft YaHei UI Light', 9), command=lambda: signup(root))
sign_up.place(x=200, y=250)

root.mainloop()
