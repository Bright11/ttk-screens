from tkinter import *

root = Tk()
root.geometry("1300x700")
root.title("Calculator")

# Top frame for the title
top_frame = Frame(root, bg="blue", height=100, width=1300, relief=SUNKEN)
top_frame.grid(row=0, column=0, sticky="ew")

# Second frame for main content
second_frame = Frame(root, width=1300, height=400, bg="red", relief=SUNKEN)
second_frame.grid(row=1, column=0, sticky="nsew")
second_frame.columnconfigure(1, weight=1)  # Set column 1 to expand with window size

# Left frame for menu buttons
left_frame = Frame(second_frame, width=700, height=300, bg="pink")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Right frame for calculator display and buttons
right_frame = Frame(second_frame, width=550, height=300, bg="green")
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")



right_frame2 = Frame(second_frame, width=550, height=300, bg="blue")
right_frame2.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")


# Label for calculator display
display_label = Label(right_frame, text="Calculator", font=("Arial", 20), bg="white", fg="black")
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Label aligned to the right
right_aligned_label = Label(right_frame, text="Right Aligned", bg="yellow")
right_aligned_label.grid(row=1, column=3, padx=(0, 10), pady=10, sticky="e")  # Adjusted padx to leave space on the left

# Buttons for calculator

# Menu buttons
home_btn = Button(left_frame, text="Home", padx=10, pady=10, width=10)
home_btn.grid(row=0, column=0, padx=10, pady=10)

sales_btn = Button(left_frame, text="Sales", padx=10, pady=10, width=10)
sales_btn.grid(row=1, column=0, padx=10, pady=10)

neworder_btn = Button(left_frame, text="New Order", padx=10, pady=10, width=10)
neworder_btn.grid(row=2, column=0, padx=10, pady=10)

delivery_btn = Button(left_frame, text="Delivery", padx=10, pady=10, width=10)
delivery_btn.grid(row=3, column=0, padx=10, pady=10)

logout_btn = Button(left_frame, text="Logout", padx=10, pady=10, width=10)
logout_btn.grid(row=4, column=0, padx=10, pady=10)

root.mainloop()
