from Tkinter import *
from PIL import Image,ImageTk
root=Tk()
r=IntVar()
r.set("0")
def clicked(value):
    l=Label(root,text=value)
    l.grid_forget()
    l.grid(row=2,column=0)

Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda: clicked(r.get())).grid(row=0,column=0)
Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: clicked(r.get())).grid(row=1,column=0)

l=Label(root,text=r.get())
l.grid(row=2,column=0)
root.mainloop()
