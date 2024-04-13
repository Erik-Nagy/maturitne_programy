import tkinter
width=500
height=500
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

noty=["c", "d", "e", "f", "g", "a", "h"]

with open('noty.txt', 'r') as subor:
    vstupneNoty=subor.readline()

def osnova(n):
    for i in range(5):
        canvas.create_line(20, n*100+i*10+20, width-20, n*100+i*10+20)

def nota(n, m, d):
    s=noty.index(d)
    canvas.create_oval(m*25+30-6, n*100+70-s*5-4, m*25+30+6, n*100+70-s*5+4)

b=0
n=0
osnova(0)
for i in range(len(vstupneNoty)):
    nota(n, b, vstupneNoty[i])
    b+=1
    if b>=18 and i!=len(vstupneNoty)-1:
        n+=1
        osnova(n)
        b=0
    


canvas.mainloop()