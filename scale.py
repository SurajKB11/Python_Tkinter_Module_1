from Tkinter import *
from PIL import ImageTk,Image

root=Tk()

f=LabelFrame(root,text="printscreen")
f.grid(row=1,column=0)                               
i=0
def printit():
    global i
    (Label(f,text="hi")).grid(row=i,column=0)
    i=i+1

b=Button(root,text="click_me",command=printit)
b.grid(row=0,column=0)

vscale=Scale(root,from_=0,to=200)
vscale.grid(row=1,column=1)

root.mainloop()
