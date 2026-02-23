from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Sign Up")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)


#### --------- Signup Function -----------####
def signup():
    name = username.get()
    password = code.get()
    confirm_password = confirm_code.get()

#### --------Validation-------####
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

    # Save to database
    try:
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO users VALUES (?, ?)', (name, password))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Account created successfully!')
        on_close()
    except sqlite3.IntegrityError:
        messagebox.showerror('Error', 'Username already exists!')


def sign():
    root.destroy()
    root.deiconify()


root.protocol('WM_DELETE_WINDOW', sign)

#### -------------------Heading UI-------------####
img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

#### -------------------Username-------------####
username = Entry(frame, width=25, fg='black', border=0,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
username.place(x=30, y=80)
username.insert(0, ' Email or username')
username.bind('<FocusIn>', lambda e: username.delete(0, 'end'))
username.bind('<FocusOut>', lambda e: username.insert(
    0, 'Username') if username.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#### -------------------Password-------------####
code = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
code.bind('<FocusOut>', lambda e: code.insert(
    0, 'Password') if code.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=180)

#### -------------------Confirm Password-------------####
confirm_code = Entry(frame, width=25, fg='black', border=0,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind('<FocusIn>', lambda e: confirm_code.delete(0, 'end'))
confirm_code.bind('<FocusOut>', lambda e: confirm_code.insert(
    0, 'Confirm Password') if confirm_code.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

#### ---------------Button & Already have account-----------------####
Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8',
       fg='white', border=0, command=signup).place(x=35, y=290)
label = Label(frame, text='Already have an account?', fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 10))
label.place(x=35, y=350)

sign_in = Button(frame, width=6, text='Log in', border=0,
                 bg='white', fg='#57a1f8', cursor='hand2', command=sign)
sign_in.place(x=200, y=350)

root.mainloop()
