import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

with open("anketa.txt", "r") as subor:
    riadky = subor.readlines()
    otazka = riadky[0]
    ano, nie, neviem = map(int, riadky[1].split())
    celkovo = ano + nie + neviem

canvas.create_text(10, 10, text = otazka, anchor='nw')

canvas.create_text(10, 50, text = f"1) Ano - {ano}", anchor='nw')
canvas.create_text(10, 80, text = f"1) Nie - {nie}", anchor='nw')
canvas.create_text(10, 110, text = f"1) Neviem - {neviem}", anchor='nw')

canvas.mainloop()
