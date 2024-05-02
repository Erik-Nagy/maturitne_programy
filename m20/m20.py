meno = "Jozo"
poplatok = 150

with open("kataster.txt", "r") as subor:
    riadky = subor.readlines()

if poplatok == 70:
    riadky.append(meno)
    riadky.append(poplatok)
else:
    for i in range(len(riadky)):
        if riadky[i].strip()=="70":
            riadky = riadky[:i-1] + [meno] + [str(poplatok)] + riadky[i-1:]
            break

with open("kataster_nove.txt", "w") as subor:
    for riadok in riadky:
        subor.write(riadok.strip()+"\n")