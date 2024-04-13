import tkinter
width=500
height=500
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

def smer_s(event):
    global sx, sy
    if sx != 0 and sy != 1: 
        sx, sy = 0, -1

def smer_j(event):
    global sx, sy
    if sx != 0 and sy != -1: 
        sx, sy = 0, 1

def smer_v(event):
    global sx, sy
    if sx != -1 and sy != 0: 
        sx, sy = 1, 0

def smer_z(event):
    global sx, sy
    if sx != 1 and sy != 0: 
        sx, sy = -1, 0

def pohyb():
    global sx, sy
    if [had[len(had)-1][0]+sx, had[len(had)-1][1]+sy] not in had:
        had.append([had[len(had)-1][0]+sx, had[len(had)-1][1]+sy])
        canvas.delete("had")
        canvas.create_line(had, tags="had")
        canvas.update()
        canvas.after(10, pohyb)

sx, sy = 0, -1
had = [[250, 250]]
canvas.create_line(had[len(had)-1][0], had[len(had)-1][1], had[len(had)-1][0], had[len(had)-1][1]+sy, tags="had")


canvas.bind_all("w", smer_s)
canvas.bind_all("s", smer_j)
canvas.bind_all("d", smer_v)
canvas.bind_all("a", smer_z)

pohyb()

canvas.mainloop()



