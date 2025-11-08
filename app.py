import tkinter as tk
from tkinter import ttk
import threading
from roam_automation import run_roam

def execute_program():
    try:
        n = int(entry.get())
        result_label.config(text=f"Running {n} iterations...")
        progress_bar["maximum"] = n
        progress_bar["value"] = 0

        # Run in a separate thread
        thread = threading.Thread(target=run_with_progress, args=(n,))
        thread.start()
    except ValueError:
        result_label.config(text="Please enter a valid integer.")

def run_with_progress(n):
    def update_progress(value):
        progress_bar["value"] = value
        root.update_idletasks()

    run_roam(n, progress_callback=update_progress)
    result_label.config(text=f"Completed {n} iterations!")

# GUI Setup
root = tk.Tk()
root.title("AutoROAM")
root.geometry("350x250")

title_label = tk.Label(root, text="Enter Number of Iterations", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

execute_button = tk.Button(root, text="Execute", command=execute_program)
execute_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=250, mode="determinate")
progress_bar.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()