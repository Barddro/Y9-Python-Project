#Imports#
from tkinter import*
from tkinter.colorchooser import*

#Window Config#
root=Tk()
root.title="Palettizer"
root.resizable(width=False, height=False)

colorlist=[]

#Function Defs#

def getColor1():
    color = askcolor()
    col_1.configure(background=color[1])
    l1.configure(text=color[1], background=color[1])
    colorlist.append(color)
    print(color)

def getColor2():
    color = askcolor()
    col_2.configure(background=color[1])
    l2.configure(text=color[1], background=color[1])
    colorlist.append(color)
    print(color)

def getColor3():
    color = askcolor()
    col_3.configure(background=color[1])
    l3.configure(text=color[1], background=color[1])
    colorlist.append(color)
    print(color)

def getColor4():
    color = askcolor()
    col_4.configure(background=color[1])
    l4.configure(text=color[1], background=color[1])
    colorlist.append(color)
    print(color)

def sv():
    for i in colorlist:
        print(i)
    f=open("Palette.txt", "w")
    f.write(str(colorlist))
    print("Colors Saved!")
    f.close()
    
    
# Topbar#
topbar=Frame(root, width=1200, height=70, bg="#e3e3e3")
topbar.grid(row=0, column=0, columnspan=4)
topbar.grid_propagate(0)

c1=Canvas(topbar, height=10, width=1200, bg="#bfbfbf", highlightthickness=0)
c1.grid()

save=Button(topbar, bg="#e3e3e3", text="Save", command=sv)
save.grid()

#Colour Bars#
col_1=Frame(root, height=700, width=300, bg="#bfbfbf")
col_1.grid(column=0, row=1)
col_1.grid_propagate(0)

col_2=Frame(root, height=700, width=300, bg="#bfbfbf")
col_2.grid(column=1, row=1)
col_2.grid_propagate(0)

col_3=Frame(root, height=700, width=300, bg="#bfbfbf")
col_3.grid(column=2, row=1)
col_3.grid_propagate(0)

col_4=Frame(root, height=700, width=300, bg="#bfbfbf")
col_4.grid(column=3, row=1)
col_4.grid_propagate(0)

#Buttons#

b1=Button(col_1, text='Select Color', command=getColor1)
b1.grid()

b2=Button(col_2, text='Select Color', command=getColor2)
b2.grid()

b3=Button(col_3, text='Select Color', command=getColor3)
b3.grid()

b4=Button(col_4, text='Select Color', command=getColor4)
b4.grid()

#Labels

l1=Label(col_1, text="HEX Code Here!", bg="#bfbfbf")
l1.grid()

l2=Label(col_2, text="HEX Code Here!", bg="#bfbfbf")
l2.grid()

l3=Label(col_3, text="HEX Code Here!", bg="#bfbfbf")
l3.grid()

l4=Label(col_4, text="HEX Code Here!", bg="#bfbfbf")
l4.grid()


root.mainloop()
