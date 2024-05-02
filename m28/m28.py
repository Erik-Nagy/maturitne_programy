import tkinter
from random import *
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def nova_hra():
    global x, y, pismeno
    if y < 500:
        x = randint(50, 450)
        y = 0
        pismeno = choice(pismena)
        kresli()

def kresli():
    canvas.delete("all")
    canvas.create_oval(x-10, y-20, x+10, y+20)
    if y >= 500/3*2:
        canvas.create_text(x, y, text=pismeno)

def pohyb():
    global y
    y += 5
    kresli()
    if y < 500:
        canvas.after(100, pohyb)

def uhadni(event):
    if event.char == pismeno:
        nova_hra()

pismena = "qwertyuiopasdfghjklzxcvbnm"
pismeno = ""
x = 0
y = 0

canvas.bind_all("<Key>", uhadni)

nova_hra()
pohyb()

canvas.mainloop()
