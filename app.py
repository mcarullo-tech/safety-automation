import tkinter as tk

root = tk.Tk()

# Setting some window properties
root.title("AutoROAM")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to AutoROAM!", font=("Comic Sans", 15))
label.pack(expand=True)


root.mainloop()