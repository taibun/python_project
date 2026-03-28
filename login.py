import tkinter
from tkinter import messagebox

login_page = tkinter.Tk()
login_page.geometry("400x300")
login_page.title("Login Page")

def login():
    username = Textbox1.get()
    password = Textbox2.get()

    if username == "python" and password == "12345":
        messagebox.showinfo("Login", "Login Successful")
        login_page.destroy()
        import dashboard
        dashboard.open_dashboard()
        
    else:
        messagebox.showerror("Login", "Incorrect Username or Password")

Label1 = tkinter.Label(login_page, text="Enter username")
Label1.place(x=50, y=50)

Textbox1 = tkinter.Entry(login_page)
Textbox1.place(x=180, y=50)

Label2 = tkinter.Label(login_page, text="Enter password")
Label2.place(x=50, y=100)

Textbox2 = tkinter.Entry(login_page, show="*")   
Textbox2.place(x=180, y=100)

LoginButton = tkinter.Button(login_page, text="Login", command=login)
LoginButton.place(x=180, y=150)

login_page.mainloop()