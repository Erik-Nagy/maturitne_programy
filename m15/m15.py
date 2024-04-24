import tkinter
from random import * 
width=610
height=100
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

def tanier(pismeno, x, y):
    canvas.create_oval(x-25, y-25, x+25, y+25, fill='lightblue')
    canvas.create_text(x, y, text=pismeno, font='Arial 30')
    surTanierov.append(x)

def kresli_taniere():
    for i in range(len(taniere)):
        tanier(taniere[i], 60*i+35, 50)

def konecna_obrazovka():
    canvas.delete('all')
    canvas.create_text(305, 30, text='Gratulujem, vyhal si', font='Arial 20')
    if len(opakovaneTaniere)>0:
        canvas.create_text(305, 60, text=f'Opakovane taniere: {opakovaneTaniere}', font='Arial 20')

def klik(event):
    global opakovaneTaniere
    x = event.x
    y = event.y
    if y>=25 and y<=75:
        for i in range(len(surTanierov)):
            if x>=surTanierov[i]-25 and x<=surTanierov[i]+25:
                if taniere[i] == prasknutyTanier:
                    for j in range(len(kliknutia)):
                        if kliknutia[j]>1:
                            opakovaneTaniere+=taniere[j]
                    konecna_obrazovka()
                else:
                    kliknutia[i]+=1


taniere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
surTanierov = []
kliknutia = [0,0,0,0,0,0,0,0,0,0]
opakovaneTaniere=""
prasknutyTanier = choice(taniere)

kresli_taniere()
canvas.bind('<Button-1>', klik)
canvas.mainloop()