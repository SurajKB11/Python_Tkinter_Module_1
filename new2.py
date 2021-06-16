
import Tkinter as tk

from Tkinter import *
from PIL import Image,ImageTk

root=Tk()

frame = Frame(root, bd=2, relief=SUNKEN)

img1=ImageTk.PhotoImage(Image.open("index.png"))

#frame.grid_rowconfigure(0, weight=3)
#frame.grid_columnconfigure(0, weight=3)

(Label(frame,image=img1)).grid(row=0,column=0)
(Label(frame,image=img1)).grid(row=1,column=0)
(Label(frame,image=img1)).grid(row=2,column=0)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=2, sticky=N+S)

canvas = Canvas(frame,yscrollcommand=yscrollbar.set)

canvas.grid(row=0, column=0, sticky=N+S+E+W)

yscrollbar.config(command=canvas.yview)

frame.grid(row=0,column=0)

 
root.mainloop()
