pocetLudi = 0
maxKapacita = 0

pocetZastavok = 0
nazvyZastavok = []
preplneneZastavky = []
najvyssiPocet = 0

with open("bus_vytazenost.txt", "r") as subor:
    riadky = subor.readlines()
    pocetZastavok = len(riadky) - 1
    maxKapacita = int(riadky[0])

for i in range(1, len(riadky)):
    riadok = riadky[i].split()
    pocetLudi += int(riadok[0])
    pocetLudi -= int(riadok[1])
    if len(riadok) == 3:
        zastavka = riadok[2]
    else:
        zastavka = riadok[2] + " " + riadok[3]
    nazvyZastavok.append(zastavka)
    if pocetLudi > maxKapacita:
        preplneneZastavky.append(zastavka)
        if pocetLudi > najvyssiPocet:
            najvyssiPocet = pocetLudi

print(f'Počet zastávok na trase Autobusu: {pocetZastavok}')
print()

print("Nazvy zastavok:")
for zastavka in nazvyZastavok:
    print(zastavka)
print()

if len(preplneneZastavky) > 0:
    print("Preplnene zastavky:")
    for zastavka in preplneneZastavky:
        print(zastavka)
    print()
    print(f'Najvyssi pocet ludi nad ramec kapacity: {najvyssiPocet}')

