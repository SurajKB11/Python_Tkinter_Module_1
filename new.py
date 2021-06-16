from Tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("Hello, People")
root.iconbitmap('@index.xbm')

my_img=ImageTk.PhotoImage(Image.open("index.png")) #image is in same location as .py file
my_label=Label(image=my_img)
my_label.pack()


button_quit=Button(root,text="Exit Program",command=root.quit)
button_quit.pack()

root.mainloop()
