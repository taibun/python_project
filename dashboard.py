import tkinter as tk
from tkinter import messagebox
import food  

root = tk.Tk()
root.title("Dashboard")
root.geometry("400x400")    

title = tk.Label(root, text="DASHBOARD", font=("Arial", 18, "bold"))
title.place(x=130, y=30)

def open_dashboard():
    def open_food_page():
        food.open_food(root)
    def gym():
        messagebox.showinfo("gym","Gym clicked")
    def reading():
        messagebox.showinfo("reading","Reading clicked")
    def eating():
        messagebox.showinfo("eating","Eating clicked")
    def sleeping():
        messagebox.showinfo("sleeping","Sleeping clicked")
    
    btn1 = tk.Button(root, text="Food", width=15, command=open_food_page)
    btn1.place(x=140, y=100)
    
    btn2 = tk.Button(root, text="Gym", width=15, command=gym)
    btn2.place(x=140, y=140)
    btn3 = tk.Button(root, text="Reading", width=15, command=reading)
    btn3.place(x=140, y=180)
    btn4 = tk.Button(root, text="Eating", width=15, command=eating)
    btn4.place(x=140, y=220)
    btn5 = tk.Button(root, text="Sleeping", width=15, command=sleeping)
    btn5.place(x=140, y=260)

open_dashboard()
root.mainloop()