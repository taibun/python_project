import tkinter as tk
from tkinter import messagebox

study_sessions = []
STUDY_GOAL = 300  

def open_reading(parent=None):

    if parent:
        root = tk.Toplevel(parent)
    else:
        root = tk.Tk()

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")

    root.title("Reading Tracker")

    tk.Label(root, text="READING TRACKER", font=("Arial", 24, "bold")).place(x=550, y=50)

    tk.Label(root, text="Subject").place(x=450, y=150)
    subject_entry = tk.Entry(root, width=25)
    subject_entry.place(x=600, y=150)

    tk.Label(root, text="Study Time (min)").place(x=450, y=200)
    time_entry = tk.Entry(root, width=25)
    time_entry.place(x=600, y=200)

    def add_session():
        subject = subject_entry.get()
        time = time_entry.get()

        if subject == "" or time == "":
            messagebox.showwarning("Input Error", "Enter subject and time")
            return

        study_sessions.append(int(time))
        listbox.insert(tk.END, f"{subject} - {time} min")


        subject_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

        update_status()
 
    tk.Button(root, text="Add Session", width=15, command=add_session).place(x=600, y=250)

    goal_label = tk.Label(root, text=f"Goal = {STUDY_GOAL} min")
    goal_label.place(x=600, y=330)

    total_label = tk.Label(root, text="Total = 0 min")
    total_label.place(x=600, y=360)

    progress_label = tk.Label(root, text="Progress = 0%")
    progress_label.place(x=600, y=390)

    def update_status():
        total = sum(study_sessions)
        progress = (total / STUDY_GOAL) * 100

        total_label.config(text=f"Total = {total} min")
        progress_label.config(text=f"Progress = {int(progress)}%")

    listbox = tk.Listbox(root, width=50, height=15)
    listbox.place(x=500, y=430)

    if parent is None:
        root.mainloop()