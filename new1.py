from Tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Hello World")
root.iconbitmap("@/home/suraj/Desktop/INTERNSHIP/index.xbm")

def open():
    global image
    top=Toplevel()
    image=ImageTk.PhotoImage(Image.open("/home/suraj/Desktop/INTERNSHIP/index.jpeg"))
    l=Label(top,image=image)
    l.pack()
    #declaring image as global is important for some reason or we won't get the image in the second window
    Button(top,text="close this window",command=top.destroy).pack()

Button(root,text="open second window",command=open).pack()

root.mainloop()
