from tkinter import *
from PIL import ImageTk, Image

def resizer(e):
    global bg, resized_bg, new_bg
    # Open the image
    bg1 = Image.open("logo/me.jpg")
    # Resize the image
    resized_bg = bg1.resize((e.width, e.height))
    # Convert Image object into Tkinter PhotoImage object
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Update the background
    bg_label.config(image=new_bg)
    bg_label.image = new_bg  # Keep a reference to avoid garbage collection

window = Tk()
width = 500
height = 600
window.geometry(f"{width}x{height}")  # Make window size dynamic
window.title("Background Image")
# window.state("zoomed")
window.iconbitmap("logo/me.ico")

# Load the original image
bg = Image.open("logo/me.jpg")
# Resize the original image to fit the window
resized_bg = bg.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
# Convert Image object into Tkinter PhotoImage object
new_bg = ImageTk.PhotoImage(resized_bg)

# Add the image to the label
bg_label = Label(window, image=new_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the button
frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

btn = Button(frame, text="button", bg="red", fg="white", padx=20, pady=20)
btn.pack(padx=20, pady=20)

# Bind the resizing function to the window
window.bind('<Configure>', resizer)

window.mainloop()
