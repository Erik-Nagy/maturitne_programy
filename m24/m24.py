import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def kresli():
    canvas.delete("all")
    if preklop:
        for i in range(vyska):
            for j, cislo in enumerate(reversed(obrazok[i])):
                if cislo==1:
                    canvas.create_rectangle(xz+j*strana, yz+i*strana, xz+j*strana+strana, yz+i*strana+strana, fill="black", width=0)
    else:
        for i in range(vyska):
            for j in range(sirka):
                if obrazok[i][j]==1:
                    canvas.create_rectangle(xz+j*strana, yz+i*strana, xz+j*strana+strana, yz+i*strana+strana, fill="black", width=0)
    canvas.update()

def preklopit():
    global preklop
    if preklop:
        preklop = False
    else:
        preklop = True
    kresli()

with open("preklopenie_obrazka.txt", "r") as subor:
    riadky = subor.readlines()

sirka, vyska = map(int, riadky[0].split())

obrazok = []
for i in range(1, vyska+1):
    obrazok.append(list(map(int, riadky[i].split())))

celkovyPocet=sirka*vyska
preklop=True
strana=20
xz=250-strana*sirka/2
yz=250-strana*vyska/2

pocetJednotiek=0
for i in range(vyska):
    for j in range(sirka):
        if obrazok[i][j]==1:
            pocetJednotiek+=1

kresli()

print(f"Obrazok ma {celkovyPocet} pixelov")
print(f"V popise obrazka je {pocetJednotiek} jednotiek")

button1 = tkinter.Button(text="Preklop", command=preklopit)
button1.pack()

canvas.mainloop()