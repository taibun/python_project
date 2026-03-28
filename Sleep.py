import tkinter as tk
from tkinter import messagebox
import Sleep

sleeps = []
SLEEP_GOAL = 8  

def open_sleep(parent=None):

    if parent:
        root = tk.Toplevel(parent)
    else:
        root = tk.Tk()

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")

    root.title("Sleep Tracker")

    tk.Label(root, text="SLEEP TRACKER", font=("Arial", 24, "bold")).place(x=550, y=50)

    tk.Label(root, text="Sleep Type").place(x=450, y=150)
    sleep_entry = tk.Entry(root, width=25)
    sleep_entry.place(x=600, y=150)

    tk.Label(root, text="Hours Slept").place(x=450, y=200)
    hour_entry = tk.Entry(root, width=25)
    hour_entry.place(x=600, y=200)

    def add_sleep():
        name = sleep_entry.get()
        hours = hour_entry.get()

        if name == "" or hours == "":
            messagebox.showwarning("Input Error", "Enter sleep type and hours")
            return

        sleeps.append(float(hours))
        listbox.insert(tk.END, f"{name} - {hours} hrs")

        sleep_entry.delete(0, tk.END)
        hour_entry.delete(0, tk.END)

        update_status()

    tk.Button(root, text="Add Sleep", width=15, command=add_sleep).place(x=600, y=250)

    goal_label = tk.Label(root, text=f"Goal = {SLEEP_GOAL} hrs")
    goal_label.place(x=600, y=300)

    total_label = tk.Label(root, text="Total = 0 hrs")
    total_label.place(x=600, y=330)

    progress_label = tk.Label(root, text="Progress = 0%")
    progress_label.place(x=600, y=360)

    def update_status():
        total = sum(sleeps)
        progress = (total / SLEEP_GOAL) * 100

        total_label.config(text=f"Total = {total} hrs")
        progress_label.config(text=f"Progress = {int(progress)}%")

    listbox = tk.Listbox(root, width=50, height=15)
    listbox.place(x=500, y=420)

    if parent is None:
        root.mainloop()