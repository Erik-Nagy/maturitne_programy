with open('vyslednaznamka.txt', 'r') as vyslednaznamka:
    znamky = {}
    koncorocneznamky = {}
    riadky = vyslednaznamka.readlines()
    for riadok in riadky:
        riadok = riadok.split()
        pocetznamok=0
        sucetznamok=0
        for i in riadok[2:]:
            pocetznamok+=1
            sucetznamok+=int(i)
        priemer=sucetznamok/pocetznamok
        koncorocnaznamka=int(round(priemer))
        koncorocneznamky[riadok[1]+' '+riadok[0]] = koncorocnaznamka
    print(koncorocneznamky)

with open('koncorocnaznamka.txt', 'w') as koncorocnaznamka:
    for meno in koncorocneznamky:
        koncorocnaznamka.write(meno + ' ')
        koncorocnaznamka.write(str(koncorocneznamky[meno]) + '\n')

