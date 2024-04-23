pocetHier=0
najdlhsiaHra=0
kommprimovaneHry=[]

with open("hada.txt", "r") as subor:
    hry = subor.readlines()
    pocetHier = len(hry)
    for hra in hry:
        if len(hra)>najdlhsiaHra:
            najdlhsiaHra=len(hra)
        poslednyKrok=""
        pocetPoslednehoSmeru=0
        kommprimovane=""
        for krok in hra.strip():
            if krok==poslednyKrok or poslednyKrok=="":
                poslednyKrok=krok
                pocetPoslednehoSmeru+=1
            else:
                kommprimovane=kommprimovane + poslednyKrok + " " + str(pocetPoslednehoSmeru) + " "
                poslednyKrok=krok
                pocetPoslednehoSmeru=1
        kommprimovane=kommprimovane + poslednyKrok + " " + str(pocetPoslednehoSmeru) + " "
        kommprimovaneHry.append(kommprimovane)

with open("hadaKomprim.txt", "w") as subor:
    for hra in kommprimovaneHry:
        subor.write(hra + "\n")

print(pocetHier)
print(najdlhsiaHra)

