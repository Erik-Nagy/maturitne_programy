import tkinter
from random import *
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def doplnSlovo(event):
    global padajuceSlovo, koniec
    if event.char in slovo:
        for i in range(len(slovo)):
            if slovo[i] == event.char:
                padajuceSlovo = padajuceSlovo[:i] + event.char + padajuceSlovo[i+1:]
        if "*" not in padajuceSlovo:
            koniec = True

def pohyb():
    global y, koniec
    canvas.delete("all")
    canvas.create_text(x, y, text = padajuceSlovo, font = "Arial 20")
    y += 5
    if y >= 530:
        koniec = True
        canvas.create_text(250, 250, text = "Neuhadol si!", font = "Arial 50", fill="red")
    if not koniec:
        canvas.after(100, pohyb)

slovo = choice(("maturita", "slovo", "karma", "obesenec", "noha", "python", "meno", "mesto", "zviera", "vec", "hlava", "ramena", "kolena", "palce"))
padajuceSlovo = len(slovo) * "*"
x = randint(100, 400)
y = 0
koniec = False

pohyb()

canvas.bind_all('<Key>', doplnSlovo)

canvas.mainloop()



