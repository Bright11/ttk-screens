from tkinter import *



root=Tk()
root.geometry("1300x700")
root.title("Text slider")


sliderframe=Frame(root,relief=SUNKEN,padx=5, pady=5,borderwidth=20,bg="blue")
sliderframe.pack(fill=X, side=TOP)

label=Label(sliderframe, text="h",font="Helvetica, 25", bg="blue", fg="white",)
label.pack(pady=10)

txt="Welcome to Bright C Web Developer..."
count=0
text=""
def slider():
    global count,text 
    if count >=len(txt):
        count= -1
        text=""
        label.configure(text=text)
    else:
        text=text + txt[count]
        label.configure(text=text)
    count+=1
    label.after(100,slider,)
        

slider()
        



root.mainloop()