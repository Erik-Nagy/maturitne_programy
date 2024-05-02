zoznamKrajin = {}
vitazy = []
maximum = 0

with open("skok_do_dialky.txt", "r") as subor:
    riadky = subor.readlines()

for i in range(len(riadky)):
    riadok = riadky[i].split()
    if riadok[1] in zoznamKrajin:
        zoznamKrajin[riadok[1]] += 1
    else:
        zoznamKrajin[riadok[1]] = 1
    for cislo in riadok[2:]:
        if int(cislo) > maximum:
            maximum = int(cislo)
            vitazy = [riadok[0]]
        elif int(cislo) == maximum:
            vitazy.append(riadok[0])

print("Krajiny a pocet sutaziacich:")
for krajina in zoznamKrajin:
    print(f'{krajina} {zoznamKrajin[krajina]}')
print()

if len(vitazy) == 1:
    print("Vitaz:")
else:
    print("Vitazy:")
for meno in vitazy:
    print(meno)
