import tkinter as tk
from roam_automation import run_roam  # Import your Selenium function

def execute_program():
    number = entry.get()
    try:
        n = int(number)  # Convert to integer for loop count
        result_label.config(text=f"Running {n} iterations...")
        root.update()  # Refresh UI before starting
        run_roam(n)  # Call Selenium automation
        result_label.config(text=f"Completed {n} iterations!")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")

root = tk.Tk()
root.title("AutoROAM")
root.geometry("300x200")

title_label = tk.Label(root, text="Enter Number of Iterations", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

execute_button = tk.Button(root, text="Execute", command=execute_program)
execute_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()