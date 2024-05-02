import tkinter
from random import *
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def vykonaj_prikaz():
    global smer, x, y
    prikaz = entry1.get()
    if prikaz == "vlavo":
        if smer == 3:
            smer = 0
        else:
            smer += 1
    if prikaz == "vpravo":
        if smer == 0:
            smer = 3
        else:
            smer -= 1
    if prikaz.split()[0] == "ciara":
        d = int(prikaz.split()[1])
        canvas.create_line(x, y, x+d*smery[smer][0], y+d*smery[smer][1])
        x = x+d*smery[smer][0]
        y = y+d*smery[smer][1]

smery = ((0, -1), (-1, 0), (0, 1), (1,0))
smer = 0
x, y = 250, 250

button1 = tkinter.Button(text="Vykonaj!", command=vykonaj_prikaz)
button1.pack()

entry1 = tkinter.Entry()
entry1.pack()

canvas.mainloop()