import tkinter as tk
from tkinter import messagebox

cal_burn = []
burn_goal = 3000

def open_gym(parent=None):

    if parent:
        root = tk.Toplevel(parent)
    else:
        root = tk.Tk()

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")

    root.title("Calorie Tracker")

    tk.Label(root, text="CALORIE TRACKER", font=("Arial", 24, "bold")).place(x=550, y=50)

    tk.Label(root, text="Exercise Name").place(x=450, y=150)
    exercise_entry = tk.Entry(root, width=25)
    exercise_entry.place(x=600, y=150)

    tk.Label(root, text="Calories").place(x=450, y=200)
    calorie_entry = tk.Entry(root, width=25)
    calorie_entry.place(x=600, y=200)

    def add_exercise():
        name = exercise_entry.get()
        calorie = calorie_entry.get()

        if name == "" or calorie == "":
            messagebox.showwarning("Input Error", "Enter exercise and calories")
            return

        cal_burn.append(int(calorie))
        listbox.insert(tk.END, f"{name} - {calorie} cal")

        exercise_entry.delete(0, tk.END)
        calorie_entry.delete(0, tk.END)

        update_status()

    tk.Button(root, text="Add Exercise", width=15, command=add_exercise).place(x=600, y=250)

    goal_label = tk.Label(root, text=f"Goal = {burn_goal}")
    goal_label.place(x=600, y=300)

    total_label = tk.Label(root, text="Total = 0")
    total_label.place(x=600, y=330)

    progress_label = tk.Label(root, text="Progress = 0%")
    progress_label.place(x=600, y=360)

    def update_status():
        total = sum(cal_burn)
        progress = (total / burn_goal) * 100

        total_label.config(text=f"Total = {total}")
        progress_label.config(text=f"Progress = {int(progress)}%")

    listbox = tk.Listbox(root, width=50, height=15)
    listbox.place(x=500, y=420)

    if parent is None:
        root.mainloop()