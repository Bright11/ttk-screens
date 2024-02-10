from tkinter import *
from PIL import ImageTk, Image

root = Tk()
width = 1600
height = 700
root.geometry(f"{width}x{height}")  # Make window size dynamic
root.title("Background app")


# button image
#  compound="left"
btnimg=Image.open("icons/icons8-restart-48.png").resize((20,20))
btnimg_btn=ImageTk.PhotoImage(btnimg)

btn=Button(root, text="click me  ",image=btnimg_btn, compound="right")
btn.pack()


btn1=Button(root, text="  click me 2",image=btnimg_btn, compound="left")
btn1.pack()

root.mainloop()
