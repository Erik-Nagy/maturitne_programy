import tkinter
from random import * 
width=500
height=225
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

def klik(event):
    x=event.x
    y=event.y
    farba = ""
    kod = entry1.get()
    if y >= 50 and y <= 175 and kod:
        if x >= 0 and x <= 125:
            farba="z"
        elif x >= 125 and x <= 250:
            farba="c"
        elif x >= 250 and x <= 375:
            farba="m"
        elif x >= 375 and x <= 500:
            farba="o"
        with open("vyber_jedla.txt", "a") as subor:
            subor.write(kod + " " + farba + "\n")

canvas.create_text(250, 25, text="VÝBER JEDLA", font="Arial 20", fill="red")
canvas.create_text(250, 210, text="kód študenta:", font="Arial 14")
canvas.create_rectangle(0, 50, 125, 175, fill="green", width=0)
canvas.create_rectangle(125, 50, 250, 175, fill="red", width=0)
canvas.create_rectangle(250, 50, 375, 175, fill="blue", width=0)
canvas.create_rectangle(375, 50, 500, 175, fill="orange", width=0)

entry1 = tkinter.Entry()
entry1.pack()
canvas.bind("<Button-1>", klik)

canvas.mainloop()