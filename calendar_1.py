import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def get_date():
    selected_date = cal.get_date()
    entry_date.delete(0, tk.END)  # Clear existing text
    entry_date.insert(0, selected_date)

root = tk.Tk()
root.title("Date Entry Example")

# Create a frame
formsframe = ttk.Frame(root)
formsframe.pack()


# Button to get the selected date
btn = ttk.Button(formsframe, text="Get Date", command=get_date)
btn.grid(row=10, column=1, padx=10, pady=10)  # Adjust row and column as needed

root.mainloop()
