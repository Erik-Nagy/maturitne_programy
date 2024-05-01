import tkinter, random
canvas = tkinter.Canvas(width=700, height=800)
canvas.pack()
    
def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def kresli():
    canvas.delete("all")
    canvas.create_line(650, 0, 650, 800, width=3)
    for i in range(len(lodicky)):
        lodicka(lodicky[i], i*50+40)

def hra():
    global start
    for i in range(len(lodicky)):
        lodicky[i]+=random.randint(1, 10)
        if lodicky[i]>650:
            start=False
            vyherna_lodicka=i+1
    kresli()
    if start:
        canvas.after(50, hra)
    else:
        canvas.create_text(350, 400, font="Arial 20", text=f"Vyhrala lodicka {vyherna_lodicka}")

def zacni(event):
    global start
    if not start:
        start=True
    hra()

lodicky = []
for i in range(15):
    lodicky.append(30)
start=False

kresli()
canvas.bind("<Button-1>", zacni)

canvas.mainloop()