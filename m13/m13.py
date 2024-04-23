with open("objednane_jedla.txt", "r") as subor:
    objednavky = subor.readlines()

jedla = {'c': 0, 'm': 0, 'z': 0, 'o': 0}
celkovyPocet = len(objednavky)
print("Celkovy pocet objednavok: " + str(celkovyPocet))

for i in range(len(objednavky)):
    jedla[objednavky[i].split()[1]]+=1

malo=""
for farba, pocet in jedla.items():
    print(f'Pocet objednavok jedla {farba}: {pocet}')
    if pocet<20:
        malo = malo + farba + ", "

malo = malo[:-2]

if malo != "":
    print('Málo objednávok majú tieto jedlá:', malo)
else:
    print('Všetky jedlá si objednalo aspoň 20 ľudí')

print(jedla)

        
