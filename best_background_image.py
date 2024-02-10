from tkinter import *
from PIL import ImageTk, Image

root = Tk()
width = 1600
height = 700
root.geometry(f"{width}x{height}")  # Make window size dynamic
root.title("Background app")

# Load the image
original_image = Image.open("logo/me.jpg").resize((width, height))
# Resize the image to fit the window

image_path = ImageTk.PhotoImage(original_image)


# bg_image = Label(root, image=image_path)
# bg_image.place(relwidth=1, relheight=1)

# button image
# compound="right"
btnimg=Image.open("logo/me.jpg").resize((20,20))
btnimg_btn=ImageTk.PhotoImage(btnimg)
btn=Button(root, text="  click me",image=btnimg_btn, compound="left")
btn.pack()

btn1=Button(root, text="  click me 2",image=btnimg_btn, compound="right")
btn1.pack()

root.mainloop()
