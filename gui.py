import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("400x300")
root.title("Login Page")

def login():
    username = Textbox1.get()
    password = Textbox2.get()

    if username == "vaskor" and password == "12345":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Incorrect Username or Password")

Label1 = tkinter.Label(root, text="Enter username")
Label1.place(x=50, y=50)

Textbox1 = tkinter.Entry(root)
Textbox1.place(x=180, y=50)

Label2 = tkinter.Label(root, text="Enter password")
Label2.place(x=50, y=100)

Textbox2 = tkinter.Entry(root, show="*")   
Textbox2.place(x=180, y=100)

LoginButton = tkinter.Button(root, text="Login", command=login)
LoginButton.place(x=180, y=150)

root.mainloop()