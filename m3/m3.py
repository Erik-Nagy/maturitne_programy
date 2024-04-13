import random

with open('poprehadzovany_text1_vstup.txt', 'r') as text:
    riadky = text.readlines()
    vystup = []
    for i in range(len(riadky)):
        vystup.append("")
    for i in range(len(riadky)):
        for slovo in riadky[i].split():
            prve_pismeno = slovo[0]
            posledne_pismeno = slovo[-1]
            pismena = list(slovo[1:-1])
            random.shuffle(pismena)
            nove_slovo = prve_pismeno + ''.join(pismena) + posledne_pismeno + " "
            vystup[i] = vystup[i] + nove_slovo

with open('poprehadzovany_text1.txt', 'w') as text:
    for riadok in vystup:
        print(riadok)
        text.write(riadok + "\n")