# from tkinter import *
# from tkinter import messagebox
# import sqlite3
# from login_frontend import signup
# import runpy

# root = Tk()
# root.title("Login Page")
# root.geometry("925x500+300+200")
# root.configure(bg="#fff")
# root.resizable(True, True)
# root.state('zoomed')

# # Database setup
# conn = sqlite3.connect('user_data.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS users(
#         username TEXT,
#         password TEXT)''')
# conn.commit()
# conn.close()


# def back():
#     root.destroy()
#     runpy.run_path('signup_frontend.py')


# btn4 = Button(root, text="<<", width=4, bg="#57a1f8",
#               border=0, font='#fff', command=back)
# btn4.place(x=20, y=20)


# def enter(i):
#     btn4['background'] = "red"


# def leave(i):
#     btn4['background'] = "#57a1f8"


# btn4.bind('<Enter>', enter)
# btn4.bind('<Leave>', leave)

# #  dashboard function


# def open_dashboard(username):
#     root.withdraw()

#     screen = Toplevel(root)
#     screen.title("App")
#     screen.geometry("925x500+300+200")
#     screen.configure(bg="#fff")
#     screen.resizable(False, False)

#     def on_close():
#         screen.destroy()
#         root.deiconify()

#     screen.protocol("WM_DELETE_WINDOW", on_close)

#     # WELCOME LABEL
#     Label(screen, text=f'Welcome, {username}!', bg='#fff', fg='#57a1f8', font=(
#         'Microsoft YaHei UI Light', 30, 'bold')).pack(pady=30)

#     Label(screen, text='You have successfully logged in!', bg='#fff',
#           fg='black', font=('Microsoft YaHei UI Light', 15)).pack()

#     Button(screen, text='Logout', bg='#57a1f8', fg='white', border=0,
#            width=20, pady=7, cursor='hand2', command=on_close).pack(pady=20)

#     #### --------UPDATE PASSWORD-------####
#     Frame(screen, width=400, height=2, bg='#57a1f8').pack(pady=10)
#     Label(screen, text='Change Password', bg='#fff', fg='#57a1f8',
#           font=('Microsoft YaHei UI Light', 13, 'bold')).pack()

#     #### -------- PASSWORD ENTRY-------####
#     new_pass = Entry(screen, width=30, fg='black', border=0,
#                      bg='#f0f0f0', font=('Microsoft YaHei UI Light', 11))
#     new_pass.pack(pady=5)
#     new_pass.insert(0, 'New password')
#     new_pass.bind('<FocusIn>', lambda e: new_pass.delete(0, 'end'))
#     new_pass.bind('<FocusOut>', lambda e: new_pass.insert(0, 'New password')
#                   if new_pass.get() == ''else None)

#     #### -------Confirm new password entry--------####
#     confirm_pass = Entry(screen, width=30, fg='black', border=0,
#                          bg='#f0f0f0', font=('Microsoft YaHei UI Light', 11))
#     confirm_pass.pack(pady=5)
#     confirm_pass.insert(0, 'Confirm new password')
#     confirm_pass.bind('<FocusIn>', lambda e: confirm_pass.delete(0, 'end'))
#     confirm_pass.bind('<FocusOut>', lambda e: confirm_pass.insert(
#         0, 'Confirm New Password') if confirm_pass.get() == '' else None)

#     def update_password():
#         new = new_pass.get()
#         confirm = confirm_pass.get()

#         if not new or new == 'New Passsword':
#             messagebox.showerror('Error', 'Enter new passsword')
#             return
#         if not confirm or confirm == 'Confirm new passsword':
#             messagebox.showerror('Error', 'Confirm your passsword')
#             return
#         if new != confirm:
#             messagebox.showerror('Error', 'Passwords do not match!')
#             return
#         if len(new) < 6:
#             messagebox.showerror(
#                 'Error', 'Passwords must be at least 6 characters!')
#             return

#         ### ---------Update in database---------####
#         conn = sqlite3.connect('user_data.db')
#         c = conn.cursor()
#         c.execute('UPDATE users SET password=? WHERE username=?',
#                   (new, username))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo('Success', 'Passowrd updated successfully')
#         new_pass.delete(0, 'end')
#         confirm_pass.delete(0, 'end')

#     ### ---------DELETE ACCOUNT--------####

#     def delete_account():
#         confirm = messagebox.askyesno(
#             'Delete Account', f'Are you sure you want to delete account "{username}"?\nThis cannot be undone')
#         if confirm:
#             conn = sqlite3.connect('user_data.db')
#             c = conn.cursor()
#             c.execute('DELETE FROM users WHERE username=?', (username,))
#             conn.commit()
#             conn.close()
#             messagebox.showinfo('Deleted', 'Acoount deleted successfully')
#             screen.destroy()
#             root.deiconify()
#     Button(screen, width=25, pady=5, text='Delete Account',
#            bg='red', fg='white', border=0,
#            cursor='hand2', command=delete_account).pack(pady=5)
#     Button(screen, width=25, pady=5, text='Update Password',
#            bg='#57a1f8', fg='white', border=0,
#            cursor='hand2', command=update_password).pack(pady=5)
#     Frame(screen, width=400, height=2, bg='red').pack(pady=10)
#     Label(screen, text='Danger Zone', bg='#fff', fg='red',
#           font=('Microsoft YaHei UI Light', 13, 'bold')).pack()


# def sign_in():
#     conn = sqlite3.connect('user_data.db')
#     c = conn.cursor()

#     username = user.get()
#     password = code.get()

# # Validating
#     if not username or username == 'Username':
#         messagebox.showwarning('Input Error', 'Username is Required')
#         conn.close()
#         return
#     if not password or password == 'Password':
#         messagebox.showwarning('Input Error', 'Password is Required')
#         conn.close()
#         return

#     c.execute("SELECT * FROM users WHERE username=? AND password=?",
#               (username, password))
#     result = c.fetchone()
#     conn.close()

#     if result:
#         open_dashboard(username)
#     else:
#         messagebox.showerror('Error', 'Invalid username or password!')


# #### ---------UI-----------###
# img = PhotoImage(file="login.png")
# Label(root, image=img, bg="white").place(x=50, y=50)

# frame = Frame(root, width=350, height=350, bg="white")
# frame.place(x=480, y=70)

# heading = Label(frame, text='Log in', fg='#57a1f8', bg='white',
#                 font=('Microsoft YaHei UI Light', 23, 'bold'))
# heading.place(x=100, y=5)

# # ######## -------------------Username------------------########
# user = Entry(frame, width=25, fg='black', border=0,
#              bg='white', font=('Microsoft YaHei UI Light', 11))
# user.place(x=30, y=80)
# user.insert(0, 'Email or username')
# user.bind('<FocusIn>', lambda e: user.delete(0, 'end'))
# user.bind('<FocusOut>', lambda e: user.insert(0, ''))

# Frame(frame, width=295, height=2, bg='black').place(x=20, y=107)

# #### --------------Password--------------####
# code = Entry(frame, show='*', width=25, fg='black', border=0,
#              bg='white', font=('Microsoft YaHei UI Light', 11))
# code.place(x=30, y=150)
# code.insert(0, 'Password')
# code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
# code.bind('<FocusOut>', lambda e: code.insert(0, ''))
# Frame(frame, width=295, height=2, bg='black').place(x=20, y=177)


# def show_password():
#     if code.cget('show') == '*':
#         code.config(show='')
#     else:
#         code.config(show='*')


# check_button = Checkbutton(frame, text='show password', bg='white', fg='black',
#                            cursor='hand2', font=('Microsoft YaHei UI Light', 9), command=show_password)
# check_button.place(x=20, y=180)

# # ######## -------------------Button------------------########
# Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8',
#        fg='white', border=0, command=sign_in).place(x=35, y=210,)

# label = Label(frame, text="Don't have an account?", fg='black',
#               bg='white', font=('Microsoft YaHei UI Light', 9))
# label.place(x=35, y=250)

# sign_up = Button(frame, width=6, text='Sign up', border=2, bg='white', fg='#57a1f8',
#                  cursor='hand2', font=('Microsoft YaHei UI Light', 9), command=lambda: signup(root))
# sign_up.place(x=200, y=250)


# root.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3
from login_frontend import signup
from PIL import ImageTk, Image
import runpy
import tkinter.font as font


root = Tk()
root.title("Login Page")
root.state('zoomed')  # Full screen (maximized)
root.configure(bg="#fff")
root.resizable(True, True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Title bar
a = Frame(root, width=screen_width, height=35, bg="#57a1f8").place(x=0, y=0)
title = Label(a, text="Seenima", font=("Comic Sans MS",
              15, "bold"), bg="#57a1f8").place(x=36, y=0)
buttonFont = font.Font(size=14)
buttonFont1 = font.Font(size=13)

# Database setup
conn = sqlite3.connect('user_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT)''')
conn.commit()
conn.close()


def back():
    root.destroy()
    runpy.run_path('signup_frontend.py')


btn4 = Button(root, text="<<", width=4, bg="#57a1f8",
              border=0, font='#fff', command=back)
btn4.place(x=20, y=0)


def enter(i):
    btn4['background'] = "red"


def leave(i):
    btn4['background'] = "#57a1f8"


btn4.bind('<Enter>', enter)
btn4.bind('<Leave>', leave)


# Dashboard function
def open_dashboard(username):
    root.withdraw()

    screen = Toplevel(root)
    screen.title("App")
    screen.state('zoomed')
    screen.configure(bg="#fff")
    screen.resizable(True, True)

    def on_close():
        screen.destroy()
        root.deiconify()

    screen.protocol("WM_DELETE_WINDOW", on_close)

    screen.update_idletasks()
    sh = screen.winfo_screenheight()
    sw = screen.winfo_screenwidth()

    # WELCOME LABEL
    Label(screen, text=f'Welcome, {username}!', bg='#fff', fg='#57a1f8',
          font=('Microsoft YaHei UI Light', int(sh * 0.05), 'bold')).pack(pady=int(sh * 0.05))

    Label(screen, text='You have successfully logged in!', bg='#fff',
          fg='black', font=('Microsoft YaHei UI Light', int(sh * 0.025))).pack()

    Button(screen, text='Logout', bg='#57a1f8', fg='white', border=0,
           width=20, pady=7, cursor='hand2', command=on_close).pack(pady=int(sh * 0.03))

    Frame(screen, width=int(sw * 0.4), height=2,
          bg='#57a1f8').pack(pady=int(sh * 0.015))

    Label(screen, text='Change Password', bg='#fff', fg='#57a1f8',
          font=('Microsoft YaHei UI Light', int(sh * 0.02), 'bold')).pack()

    new_pass = Entry(screen, width=30, fg='black', border=0,
                     bg='#f0f0f0', font=('Microsoft YaHei UI Light', int(sh * 0.02)))
    new_pass.pack(pady=int(sh * 0.01))
    new_pass.insert(0, 'New password')
    new_pass.bind('<FocusIn>', lambda e: new_pass.delete(0, 'end'))
    new_pass.bind('<FocusOut>', lambda e: new_pass.insert(0, 'New password')
                  if new_pass.get() == '' else None)

    confirm_pass = Entry(screen, width=30, fg='black', border=0,
                         bg='#f0f0f0', font=('Microsoft YaHei UI Light', int(sh * 0.02)))
    confirm_pass.pack(pady=int(sh * 0.01))
    confirm_pass.insert(0, 'Confirm new password')
    confirm_pass.bind('<FocusIn>', lambda e: confirm_pass.delete(0, 'end'))
    confirm_pass.bind('<FocusOut>', lambda e: confirm_pass.insert(
        0, 'Confirm New Password') if confirm_pass.get() == '' else None)

    def update_password():
        new = new_pass.get()
        confirm = confirm_pass.get()

        if not new or new == 'New Password':
            messagebox.showerror('Error', 'Enter new password')
            return
        if not confirm or confirm == 'Confirm new password':
            messagebox.showerror('Error', 'Confirm your password')
            return
        if new != confirm:
            messagebox.showerror('Error', 'Passwords do not match!')
            return
        if len(new) < 6:
            messagebox.showerror(
                'Error', 'Password must be at least 6 characters!')
            return

        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute('UPDATE users SET password=? WHERE username=?',
                  (new, username))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Password updated successfully')
        new_pass.delete(0, 'end')
        confirm_pass.delete(0, 'end')

    def delete_account():
        confirm = messagebox.askyesno(
            'Delete Account', f'Are you sure you want to delete account "{username}"?\nThis cannot be undone')
        if confirm:
            conn = sqlite3.connect('user_data.db')
            c = conn.cursor()
            c.execute('DELETE FROM users WHERE username=?', (username,))
            conn.commit()
            conn.close()
            messagebox.showinfo('Deleted', 'Account deleted successfully')
            screen.destroy()
            root.deiconify()

    Button(screen, width=25, pady=5, text='Update Password',
           bg='#57a1f8', fg='white', border=0,
           cursor='hand2', command=update_password).pack(pady=int(sh * 0.01))

    Frame(screen, width=int(sw * 0.4), height=2,
          bg='red').pack(pady=int(sh * 0.015))

    Label(screen, text='Danger Zone', bg='#fff', fg='red',
          font=('Microsoft YaHei UI Light', int(sh * 0.02), 'bold')).pack()

    Button(screen, width=25, pady=5, text='Delete Account',
           bg='red', fg='white', border=0,
           cursor='hand2', command=delete_account).pack(pady=int(sh * 0.01))


def sign_in():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()

    username = user.get()
    password = code.get()

    if not username or username == 'Email or username':
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


#### --------- UI -----------###

# Get screen size after zoomed
root.update_idletasks()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# Original fixed sizes
img_width = 400    # approximate width of login.png area
form_width = 350
form_height = 350

# Total content width = image area + form area
total_content_width = img_width + form_width + 60  # 60px gap

# Center everything horizontally and vertically
start_x = (sw - total_content_width) // 2
start_y = (sh - form_height) // 2 - 30  # slight upward offset looks better

# Image - left side, vertically centered
img = PhotoImage(file="login.png")
img_label = Label(root, image=img, bg="white")
img_label.place(x=start_x, y=start_y)

# Frame - right side, same original size (350x350)
frame_x = start_x + img_width + 60
frame_y = start_y

frame = Frame(root, width=form_width, height=form_height, bg="white")
frame.place(x=frame_x, y=frame_y)

# ---- All original fixed positions inside the frame are unchanged ---- #

heading = Label(frame, text='Log in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Username entry
user = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Email or username')
user.bind('<FocusIn>', lambda e: user.delete(0, 'end'))
user.bind('<FocusOut>', lambda e: user.insert(
    0, 'Email or username') if user.get() == '' else None)

Frame(frame, width=295, height=2, bg='black').place(x=20, y=107)

# Password entry
code = Entry(frame, show='*', width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
code.bind('<FocusOut>', lambda e: code.insert(
    0, 'Password') if code.get() == '' else None)

Frame(frame, width=295, height=2, bg='black').place(x=20, y=177)


def show_password():
    if code.cget('show') == '*':
        code.config(show='')
    else:
        code.config(show='*')


check_button = Checkbutton(frame, text='Show password', bg='white', fg='black',
                           cursor='hand2', font=('Microsoft YaHei UI Light', 9),
                           command=show_password)
check_button.place(x=20, y=180)

# Login button
Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8',
       fg='white', border=0, command=sign_in).place(x=35, y=210)

# Sign up
label = Label(frame, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=35, y=250)

sign_up = Button(frame, width=6, text='Sign up', border=2, bg='white', fg='#57a1f8',
                 cursor='hand2', font=('Microsoft YaHei UI Light', 9),
                 command=lambda: signup(root))
sign_up.place(x=200, y=250)


root.mainloop()
