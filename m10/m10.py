import tkinter
from random import * 
width=800
height=500
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

def bunka(x, y, pismeno, hlavne, prazdna):
    if hlavne:
        canvas.create_rectangle(x-10, y-10, x+10, y+10, fill="gray")
    else:
        canvas.create_rectangle(x-10, y-10, x+10, y+10, fill="white")
    if not prazdna:
        canvas.create_text(x, y, text=pismeno, font="Arail 10")

def riadok(n, poradieHlavneho, slovo, prazdna):
    poradieHlavneho-=1
    if prazdna:
        x=200
    else:
        x=600
    for i in range(len(slovo)):
        if i==poradieHlavneho:
            bunka(x+20*i-20*poradieHlavneho, 20+n*20, slovo[i], True, prazdna)
        else:
            bunka(x+20*i-20*poradieHlavneho, 20+n*20, slovo[i], False, prazdna)

def krizovka(slova, prazdna):
    for i in range(len(slova)):
        riadok(i, int(slova[i].split()[0]), slova[i].split()[1], prazdna)

with open("krizovka.txt", "r") as subor:
    riadky=subor.readlines()
    krizovka(riadky, True)
    krizovka(riadky, False)

canvas.mainloop()