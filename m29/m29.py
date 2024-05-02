import tkinter
from random import *
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def oznac(event):
    global vyhral
    if not koniec:
        x = event.x
        y = event.y
        if x > 100 and x < 300 and int((y - 100) / 10) == spravny:
            canvas.create_text(250, 200, text="Vyhral si!", font="Arial 30")
            vyhral = True

def casovac():
    global s, koniec
    s -= 1
    canvas.delete("cas")
    canvas.create_text(350, 125, text=s, font="Arial 30", fill="red", tags="cas")
    if s < 0:
        koniec = True
        canvas.delete("all")
    elif not vyhral:
        canvas.after(1000, casovac)

farby = ("green", "red", "grey", "blue", "yellow")
spravny = randint(0, 4)
s = 21
koniec = False
vyhral = False

for i in range(5):
    canvas.create_rectangle(100, 100+i*10, 300, 110+i*10, fill=farby[i])
canvas.create_text(250, 50, text="Pyrotechnik", font="Arial 20", fill="blue")
canvas.create_text(250, 80, text="označ správny káblik", font="Arial 15")

canvas.bind("<Button-1>", oznac)

casovac()

canvas.mainloop()