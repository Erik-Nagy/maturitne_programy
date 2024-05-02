from random import *
from math import *
import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def stlac(event):
    global px, py
    if event.char == "w":
        px, py = 0, -2
    elif event.char == "a":
        px, py = -2, 0
    elif event.char == "s":
        px, py = 0, 2
    elif event.char == "d":
        px, py = 2, 0

def pohyb():
    global zx, zy
    zx += px
    zy += py
    canvas.move(zrut, px, py)
    for i in range(len(jedlo)):
        if sqrt((jedlo[i][0] - zx) ** 2 + (jedlo[i][1] - zy) ** 2) <= 2 * r:
            canvas.delete(jedlo[i][2])
            jedlo.pop(i)
            break
    if len(jedlo) > 0:
        canvas.after(50, pohyb)
    else:
        canvas.create_text(250, 250, text='Všetky jabĺčka sú zjedené!',font='Arial 30')

N=5
r=20
jedlo=[]
zx, zy = r, r
px, py = 2, 0
zrut=canvas.create_oval(zx-r, zy-r, zx+r, zy+r, fill="blue", width=0)

for i in range(N):
    x, y=randint(r * 3, 500-r), randint(r * 3, 500-r)
    jedlo.append([x, y, canvas.create_oval(x-r, y-r, x+r, y+r, fill="red", width=0)])

canvas.bind_all('<Key>', stlac)

pohyb()

canvas.mainloop()