duperec=[('gadgets', 'p4', 'index.jpeg', 130.3, 1, 90), ('gadgets', 'p4', 'index.jpeg', 1200.59, 1, 25), ('appliances', 'p9', 'index.jpeg', 120.6, 1, 34), ('decor', 'pr1', 'index.jpeg', 40, 1, 120)]
duperec1=[]
duperec2=[]
duperec3=[]
for i in duperec:
        categ=i[0]
        duperec1=duperec1+[str(categ)]
print(duperec1)
