import tkinter
canvas = tkinter.Canvas(width=800, height=300)
canvas.pack()

vyraz = input()
uroven = 0
farby = ["red", "purple", "yellow", "blue", "pink", "green", "brown"]

for i in range(len(vyraz)):
    if vyraz[i] == "(":
        canvas.create_text(10+i*20, 50, text=vyraz[i], font="Arial 20", fill=farby[uroven])
        uroven += 1
    elif vyraz[i] == ")":
        uroven -= 1
        canvas.create_text(10+i*20, 50, text=vyraz[i], font="Arial 20", fill=farby[uroven])
    else:
        canvas.create_text(10+i*20, 50, text=vyraz[i], font="Arial 20")
    if uroven < 0:
        break
    
if uroven != 0:
    canvas.delete("all")
    canvas.create_text(400, 100, text="Uzatvorkovanie je nespravne", font="Arial 20") 
else:
    canvas.create_text(400, 100, text="Uzatvorkovanie je spravne", font="Arial 20") 

canvas.mainloop()