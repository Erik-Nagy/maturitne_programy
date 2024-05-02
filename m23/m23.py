import tkinter
from random import *
sirka = 700
vyska = 500
canvas = tkinter.Canvas(width=sirka, height=vyska, bg='lightblue')
canvas.pack()

def kresli_krajinu(event):
    canvas.delete('all')
    farby = ("green", "lightgreen", "darkgreen", "cyan", "olive", "blue", "lightblue", "darkblue")
    for i in range(10):
        canvas.create_polygon(generuj_udaje(), fill=choice(farby), outline="black")

def generuj_udaje():
    smer = choice((-1, 1))
    x = 0
    y = randint(200, 500)
    zlom = randint(100, 600)
    suradnice = [x, y]
    while x<sirka:
        if x < zlom:
            y += randint(0, 5)*smer
        else:
            y += randint(0, 5)*smer*-1
        x += 10
        suradnice.append(x)
        suradnice.append(y)
    suradnice = suradnice + [sirka, vyska, 0, 500]
    return suradnice

canvas.bind_all("<space>", kresli_krajinu)

canvas.mainloop()