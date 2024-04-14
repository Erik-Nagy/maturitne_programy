import tkinter
from random import * 
width=500
height=500
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

def zmenZonu():
    global zona
    if zona:
        zona=False
        canvas.delete("zona")
    else:
        zona=True
        canvas.create_rectangle(200, 200, 300, 300, tags="zona")

def kresliMuchy():
    canvas.delete("mucha")
    for i in range(len(muchy)):
        canvas.create_rectangle(muchy[i][0]-1, muchy[i][1]-1, muchy[i][0]+1, muchy[i][1]+1, tags="mucha", fill="black")
    canvas.update()

def pohyb():
    global muchy
    for i in range(len(muchy)):
        if zona:
            if muchy[i][0] <= 201:
                posunX=choice((0, 2))
            elif muchy[i][0] >= 301:
                posunX=choice((-2, 0))
            else:
                posunX=choice((-2, 0, 2))

            if muchy[i][1] <= 201:
                posunY=choice((0, 2))
            elif muchy[i][1] >= 301:
                posunY=choice((-2, 0))
            else:
                posunY=choice((-2, 0, 2))
        else:
            posunX=choice((-2, 0, 2))
            posunY=choice((-2, 0, 2))
        muchy[i]=[muchy[i][0]+posunX, muchy[i][1]+posunY]
    kresliMuchy()
    canvas.after(10, pohyb)

zona=True
muchy=[]
for i in range(20):
    muchy.append([randint(201, 299), randint(201, 299)])

canvas.create_rectangle(200, 200, 300, 300, tags="zona")

button1 = tkinter.Button(text="VON", command=zmenZonu)
button1.pack()

pohyb()

canvas.mainloop()