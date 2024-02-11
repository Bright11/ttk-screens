import tkinter as tk
from tkinter import ttk

def center_window(window):
    window.update_idletasks()
    # width = window.winfo_width()
    # height = window.winfo_height()
    width=500
    height=300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    

root = tk.Tk()
# root background image

frame = ttk.Frame(root)

# Configure frame content...
# frame.grid(row=0, column=0) # If you want to grid the frame within another container.

# Center the frame on the screen
center_window(root)

root.mainloop()
