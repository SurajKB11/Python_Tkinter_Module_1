import sqlite3

tenn=sqlite3.connect('products.db')
mouse=tenn.cursor()
mouse.execute("SELECT * FROM product")
records=mouse.fetchall()
duperec=records
duperec1=[]
    #allrec=list(records)
for i in duperec:
    categ=i[0]
    duperec1=duperec1+[str(i[0])]
    for j in duperec:
        if j[0]==categ:
            duperec.remove(j)
                
    
