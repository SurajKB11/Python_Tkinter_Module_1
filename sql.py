from Tkinter import *
import sqlite3

root=Tk()
root.title("sqlite3")

conn=sqlite3.connect('address_book.db')

cu=conn.cursor()
'''
cu.execute("""CREATE TABLE addresses (
               first_name text,
               last_name text,
               address text,
               city text,
               state text,
               zipcode integer
          )""")
 '''      

f=Entry(root,width=30)
l=Entry(root,width=30)
a=Entry(root,width=30)
c=Entry(root,width=30)
s=Entry(root,width=30)
z=Entry(root,width=30)

d=Entry(root,width=30)

f.grid(row=0,column=1)
l.grid(row=1,column=1)
a.grid(row=2,column=1)
c.grid(row=3,column=1)
s.grid(row=4,column=1)
z.grid(row=5,column=1)

d.grid(row=9,column=1)

fl=Label(root,text="first name")
fl.grid(row=0,column=0,sticky="w")
ll=Label(root,text="last name")
ll.grid(row=1,column=0,sticky="w")
al=Label(root,text="address")
al.grid(row=2,column=0,sticky="w")
cl=Label(root,text="city")
cl.grid(row=3,column=0,sticky="w")
sl=Label(root,text="state")
sl.grid(row=4,column=0,sticky="w")
zl=Label(root,text="zipcode")
zl.grid(row=5,column=0,sticky="w")

dl=Label(root,text="id number")
dl.grid(row=9,column=0)
        
def delet():
    conn=sqlite3.connect('address_book.db')
    cu=conn.cursor()
    cu.execute("DELETE from addresses WHERE oid="+d.get())
    d.delete(0,END)
    conn.commit()
    conn.close()

def query():
    k=13
    conn=sqlite3.connect('address_book.db')
    cu=conn.cursor()
    cu.execute("SELECT *,oid FROM addresses")
    records=cu.fetchall()
    print(records)
    for i in records:
        (Label(root,text=str(i))).grid(row=k,column=0,columnspan=2)
        k=k+1
    conn.commit()
    conn.close()

def submit():
    conn=sqlite3.connect('address_book.db')
    cu=conn.cursor()

    conn.execute("""INSERT INTO addresses VALUES(:first_name,:last_name,:address,:city,:state,:zipcode)""",
    {
                   'first_name':f.get(),
                   'last_name':l.get(),
                   'address':a.get(),
                   'city':c.get(),
                   'state':s.get(),
                   'zipcode':z.get()})

    conn.commit()
    conn.close()
    
    f.delete(0,END)
    l.delete(0,END)
    a.delete(0,END)
    c.delete(0,END)
    s.delete(0,END)
    z.delete(0,END)  
    

submit=Button(root,text="submit",command=submit)
submit.grid(row=6,column=0,columnspan=2,pady=10)

qb=Button(root,text="show records",command=query)
qb.grid(row=7,column=0,columnspan=2)

dbtn=Button(root,text="delete record",command=delet)
dbtn.grid(row=12,column=0,columnspan=2,pady=10)

conn.commit()

conn.close()

root.mainloop()
