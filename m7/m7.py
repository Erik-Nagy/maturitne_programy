import tkinter
from random import * 
width=500
height=500
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

with open('GMA.txt', 'r') as subor:
    riadky = subor.readlines()
    velkostX = riadky[0].split()[0]
    velkostY = riadky[0].split()[1]
    x=0
    y=0
    for i in range(len(riadky[1].split())):
        if x==int(velkostX):
            x=0
            y+=1
        if riadky[1].split()[i] == "0":
            canvas.create_rectangle(20*x, 20*y, 20*x+20, 20*y+20, fill="black")
        else:
            canvas.create_rectangle(20*x, 20*y, 20*x+20, 20*y+20, fill="white")
        x+=1

with open('KOMPRIM.txt', 'w') as subor:
    subor.write(velkostX + " " + velkostY + "\n")
    komprimovane = ""
    prve = riadky[1].split()[0]
    farba=prve
    hodnota=0
    for i in range(len(riadky[1].split())):
        if riadky[1].split()[i] == farba:
            hodnota+=1
        else:
            komprimovane=komprimovane+str(hodnota)+" "
            hodnota=1
            if farba == "0":
                farba="1"
            else:
                farba="0"
    komprimovane=komprimovane+str(hodnota)+" "
    subor.write(prve+" "+komprimovane)     


canvas.mainloop()