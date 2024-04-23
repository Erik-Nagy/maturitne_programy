import tkinter
from random import * 
width=500
height=50
canvas = tkinter.Canvas(width=width, height=height, bg="black")
canvas.pack()

with open("zastavky.txt", "r") as subor:
    zastavky = subor.readlines()

def kresliPismena(sur, pismena):
    canvas.delete('zastavka')
    for i in range(len(pismena)):
        canvas.create_text(sur[i], 25, text=pismena[i], font='Arial 20', fill='red', tags='zastavka')
    canvas.update()

def prepniZastavku(event):
    global zastavka, zastavkaCislo, prepnutaZastavka
    if zastavkaCislo < len(zastavky)-1:
        zastavkaCislo+=1
        zastavka = zastavky[zastavkaCislo].strip()
        prepnutaZastavka = True

def animacia():
    global zastavka, pismenaX, prepnutaZastavka
    if not prepnutaZastavka and zastavkaCislo != -1:
        kresliPismena(pismenaX, zastavka)
        for i in range(len(pismenaX)):
            if pismenaX[i]==20:
                pismenaX[i]=480
            else:
                pismenaX[i]-=20
    else:
        pismenaX = []
        for i in range(len(zastavka)):
            pismenaX.append(100+i*20)
        prepnutaZastavka = False
    canvas.after(300, animacia)


zastavkaCislo = -1
zastavka = zastavky[0].strip()
print(zastavky)
pismenaX = []
for i in range(len(zastavka)):
    pismenaX.append(100+i*20)
prepnutaZastavka = False
zastavky[len(zastavky)-1] = zastavky[len(zastavky)-1] + "VYSTUPTE!!!"
kresliPismena(pismenaX, zastavka)

animacia()

canvas.bind_all("<Return>", prepniZastavku)

canvas.mainloop()