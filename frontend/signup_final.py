import tkinter.font as font
from tkinter import *
from tkinter import messagebox
import sqlite3
from login_frontend import signup
import runpy

root = Tk()
root.title("Login Page")
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(True, True)

# Database setup
conn = sqlite3.connect('user_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT)''')
conn.commit()
conn.close()


root.update_idletasks()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# Original fixed sizes
img_width = 400
form_width = 350
form_height = 350
total_content_width = img_width + form_width + 60

# Center everything
start_x = (sw - total_content_width) // 2
start_y = (sh - form_height) // 2 - 30

a = Frame(root, width=sw, height=35, bg="#57a1f8")
a.place(x=0, y=0)
Label(a, font=("Comic Sans MS", 15, "bold"), bg="#57a1f8").place(x=36, y=0)
img = PhotoImage(file="login.png")

# Back feature


def back():
    root.destroy()
    runpy.run_path('signup_frontend.py')


btn4 = Button(root, text="<<", width=4, bg="#57a1f8",
              border=0, fg='#fff', command=back)
btn4.place(x=40, y=40)


def enter(i):
    btn4['background'] = "red"


def leave(i):
    btn4['background'] = "#57a1f8"


btn4.bind('<Enter>', enter)
btn4.bind('<Leave>', leave)


# -------- Admin Login Window --------
def open_admin_login():
    admin_win = Toplevel(root)
    admin_win.title("Admin Login")
    admin_win.geometry("400x300+{}+{}".format(sw // 2 - 200, sh // 2 - 150))
    admin_win.configure(bg="#fff")
    admin_win.resizable(False, False)
    admin_win.grab_set()

    Label(admin_win, text="Admin Login", fg="#57a1f8", bg="#fff",
          font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=120, y=20)

    admin_user = Entry(admin_win, width=28, fg='black', border=0,
                       bg='#fff', font=('Microsoft YaHei UI Light', 11))
    admin_user.place(x=50, y=90)
    admin_user.insert(0, 'Admin Username')
    admin_user.bind('<FocusIn>', lambda e: admin_user.delete(0, 'end'))
    admin_user.bind('<FocusOut>', lambda e: admin_user.insert(0, 'Admin Username')
                    if admin_user.get() == '' else None)
    Frame(admin_win, width=300, height=2, bg='black').place(x=50, y=115)

    admin_pass = Entry(admin_win, show='*', width=28, fg='black', border=0,
                       bg='#fff', font=('Microsoft YaHei UI Light', 11))
    admin_pass.place(x=50, y=140)
    admin_pass.insert(0, 'Admin Password')
    admin_pass.bind('<FocusIn>', lambda e: admin_pass.delete(0, 'end'))
    admin_pass.bind('<FocusOut>', lambda e: admin_pass.insert(0, 'Admin Password')
                    if admin_pass.get() == '' else None)
    Frame(admin_win, width=300, height=2, bg='black').place(x=50, y=165)

    def verify_admin():
        ADMIN_USERNAME = "admin"
        ADMIN_PASSWORD = "admin123"

        uname = admin_user.get()
        pword = admin_pass.get()

        if not uname or uname == 'Admin Username':
            messagebox.showwarning(
                'Input Error', 'Enter admin username', parent=admin_win)
            return
        if not pword or pword == 'Admin Password':
            messagebox.showwarning(
                'Input Error', 'Enter admin password', parent=admin_win)
            return

        if uname == ADMIN_USERNAME and pword == ADMIN_PASSWORD:
            admin_win.destroy()
            root.withdraw()
            open_admin_dashboard()
        else:
            messagebox.showerror(
                'Error', 'Invalid admin credentials!', parent=admin_win)

    Button(admin_win, width=30, pady=7, text='Login as Admin', bg='#57a1f8',
           fg='white', border=0, command=verify_admin).place(x=80, y=200)
    Button(admin_win, text='Cancel', bg='#eee', fg='black', border=0,
           width=10, cursor='hand2', command=admin_win.destroy).place(x=150, y=250)

# -------- Admin Dashboard --------


def open_admin_dashboard():
    import admin_dashboard
    admin_dashboard.launch(root)


def open_dashboard(username):
    root.withdraw()

    screen = Toplevel(root)
    screen.title("Dashboard")
    screen.state('zoomed')
    screen.configure(bg="#fff")
    screen.resizable(True, True)

    screen.update_idletasks()
    dsh = screen.winfo_screenheight()
    dsw = screen.winfo_screenwidth()

    def on_close():
        screen.destroy()
        root.deiconify()

    screen.protocol("WM_DELETE_WINDOW", on_close)

    Label(screen, text=f'Welcome, {username}!', bg='#fff', fg='#57a1f8',
          font=('Microsoft YaHei UI Light', int(dsh * 0.05), 'bold')).pack(pady=int(dsh * 0.05))

    Label(screen, text='You have successfully logged in!', bg='#fff',
          fg='black', font=('Microsoft YaHei UI Light', int(dsh * 0.025))).pack()

    Button(screen, text='Logout', bg='#57a1f8', fg='white', border=0,
           width=20, pady=7, cursor='hand2', command=on_close).pack(pady=int(dsh * 0.03))

# -------- Sign In --------


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

# Image - left side
img_label = Label(root, image=img, bg="white")
img_label.place(x=start_x, y=start_y)

# Frame - right side
frame_x = start_x + img_width + 60
frame_y = start_y

frame = Frame(root, width=form_width, height=form_height, bg="white")
frame.place(x=frame_x, y=frame_y)

# Heading
heading = Label(frame, text='Log in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Username entry
user = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', lambda e: user.delete(0, 'end'))
user.bind('<FocusOut>', lambda e: user.insert(
    0, 'Username') if user.get() == '' else None)
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


# Forgot password dashboard
def forgot_password_popup():
    root.update_idletasks()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    forgot_win = Toplevel(root)
    forgot_win.title("Forgot Password")
    forgot_win.configure(bg="#fff")
    forgot_win.resizable(False, False)
    forgot_win.geometry('400x500')

    # Heading
    Label(forgot_win, text="Forgot Password", fg='#57a1f8', bg='#fff',
          font=('Microsoft YaHei UI Light', 18, 'bold')).place(x=90, y=20)
    Label(forgot_win, text="Enter your username to reset your password",
          fg='#888', bg='#fff', font=('Microsoft YaHei UI Light', 9)).place(x=55, y=62)

    # Username field
    user_entry = Entry(forgot_win, width=32, fg='black', border=0,
                       bg='#fff', font=('Microsoft YaHei UI Light', 11))
    user_entry.place(x=50, y=95)
    user_entry.insert(0, 'Enter your username')
    user_entry.bind('<FocusIn>', lambda e: user_entry.delete(
        0, 'end') if user_entry.get() == 'Enter your username' else None)
    user_entry.bind('<FocusOut>', lambda e: user_entry.insert(
        0, 'Enter your username') if user_entry.get() == '' else None)
    Frame(forgot_win, width=320, height=2, bg='#57a1f8').place(x=50, y=122)

    # New password field
    new_entry = Entry(forgot_win, show='*', width=32, fg='black', border=0,
                      bg='#fff', font=('Microsoft YaHei UI Light', 11))
    new_entry.place(x=50, y=145)
    new_entry.insert(0, 'New password')
    new_entry.bind('<FocusIn>', lambda e: new_entry.delete(
        0, 'end') if new_entry.get() == 'New password' else None)
    new_entry.bind('<FocusOut>', lambda e: new_entry.insert(
        0, 'New password') if new_entry.get() == '' else None)
    Frame(forgot_win, width=320, height=2, bg='#57a1f8').place(x=50, y=172)

    # Confirm password field
    confirm_entry = Entry(forgot_win, show='*', width=32, fg='black', border=0,
                          bg='#fff', font=('Microsoft YaHei UI Light', 11))
    confirm_entry.place(x=50, y=195)
    confirm_entry.insert(0, 'Confirm new password')
    confirm_entry.bind('<FocusIn>', lambda e: confirm_entry.delete(
        0, 'end') if confirm_entry.get() == 'Confirm new password' else None)
    confirm_entry.bind('<FocusOut>', lambda e: confirm_entry.insert(
        0, 'Confirm new password') if confirm_entry.get() == '' else None)
    Frame(forgot_win, width=320, height=2, bg='#57a1f8').place(x=50, y=222)

    def reset_password():
        uname = user_entry.get().strip()
        new = new_entry.get()
        confirm = confirm_entry.get()

        if not uname or uname == 'Enter your username':
            messagebox.showerror(
                'Error', 'Please enter your username', parent=forgot_win)
            return
        if not new or new == 'New password':
            messagebox.showerror(
                'Error', 'Enter a new password', parent=forgot_win)
            return
        if not confirm or confirm == 'Confirm new password':
            messagebox.showerror(
                'Error', 'Please confirm your password', parent=forgot_win)
            return
        if new != confirm:
            messagebox.showerror(
                'Error', 'Passwords do not match!', parent=forgot_win)
            return
        if len(new) < 6:
            messagebox.showerror(
                'Error', 'Password must be at least 6 characters!', parent=forgot_win)
            return

        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=?', (uname,))
        result = c.fetchone()
        if not result:
            messagebox.showerror(
                'Error', f'No account found for "{uname}"', parent=forgot_win)
            conn.close()
            return

        c.execute('UPDATE users SET password=? WHERE username=?', (new, uname))
        conn.commit()
        conn.close()
        messagebox.showinfo(
            'Success', 'Password reset successfully!\nYou can now log in.', parent=forgot_win)
        forgot_win.destroy()

    def show_password():
        if new_entry.cget('show') == '*':
            new_entry.config(show='')
        else:
            new_entry.config(show='*')
    check_button = Checkbutton(forgot_win, text='Show password', bg='white', fg='black',
                               cursor='hand2', font=('Microsoft YaHei UI Light', 9),
                               command=show_password)
    check_button.place(x=20, y=230)

    # --Reset button
    Button(forgot_win, width=30, pady=9, text='Reset Password',
           bg='#57a1f8', fg='white', border=0, cursor='hand2',
           font=('Microsoft YaHei UI Light', 10, 'bold'),
           command=reset_password).place(x=50, y=260)

    # --Cancel button
    Button(forgot_win, width=15, text='Cancel', bg='#eee', fg='#555',
           border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 9),
           command=forgot_win.destroy).place(x=145, y=350)

# Forgot password button on login frame
Button(frame, text='Forgot password?', border=0, bg='white',
       fg='#57a1f8', cursor='hand2',
       font=('Microsoft YaHei UI Light', 9),
       command=forgot_password_popup).place(x=175, y=182)

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

# -------- Admin Toggle Button--------
admin_btn = Button(root, text="Admin Login", bg="#2c2c2c", fg="white",
                   border=0, padx=10, pady=5, cursor='hand2',
                   font=('Microsoft YaHei UI Light', 9, 'bold'),
                   command=open_admin_login)
admin_btn.place(x=sw - 130, y=40)


def admin_enter(e):
    admin_btn['background'] = '#57a1f8'


def admin_leave(e):
    admin_btn['background'] = '#2c2c2c'


admin_btn.bind('<Enter>', admin_enter)
admin_btn.bind('<Leave>', admin_leave)

root.mainloop()
