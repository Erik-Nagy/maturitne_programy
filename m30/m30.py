import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

with open("anketa.txt", "r") as subor:
    riadky = subor.readlines()
    otazka = riadky[0]
    odpovedePocty = []
    for i in range(len(riadky[1].split())):
        odpovedePocty.append(int(riadky[1].split()[i]))
    celkovo = sum(odpovedePocty)


def kresli():
    canvas.delete("all")
    canvas.create_text(10, 10, text = otazka, anchor='nw')
    for i in range(3):
        canvas.create_text(10, 50+i*30, text = f"{i+1}) {odpovede[i]} - {odpovedePocty[i]}", anchor='nw')
        if i == odpovedePocty.index(max(odpovedePocty)):
            farba = "green"
        else:
            farba = "red"
        canvas.create_rectangle(120, 50+i*30, 120+odpovedePocty[i]/celkovo*100, 70+i*30, fill=farba)

def dopln(event):
    global celkovo
    x = event.x
    y = event.y
    for i in range(3):
        if x>5 and x<20 and y>50+i*30 and y<60+i*30:
            print(i)
            celkovo = sum(odpovedePocty)
            odpovedePocty[i] += 1
            kresli()
    with open("anketa.txt", "w") as subor:
        subor.write(otazka)
        for i in range(3):
            subor.write(f"{odpovedePocty[i]} ")

odpovede = ("Ano", "Nie", "Neviem")

canvas.bind("<Button-1>", dopln)

kresli()
canvas.mainloop()
