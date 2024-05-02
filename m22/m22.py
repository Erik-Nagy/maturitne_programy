pocetMien = 0
najdlhsieKrstne = 0
najdlhsiePriezvisko = 0
celeMena = []

with open("mena_zamestnancov.txt", "r") as subor:
    riadky = subor.readlines()
    pocetMien = int(len(riadky) / 2)
    krstneMena = riadky[:int(len(riadky) / 2)]
    priezviska = riadky[int(len(riadky) / 2):]

with open("vystup.txt", "w") as subor:
    for i in range(len(krstneMena)):
        if len(krstneMena[i].split()) > najdlhsieKrstne:
            najdlhsieKrstne = len(krstneMena[i].split())
        if len(priezviska[i].split()) > najdlhsiePriezvisko:
            najdlhsiePriezvisko = len(priezviska[i].split())
        subor.write(f"{krstneMena[i].strip()} {priezviska[i]}")

print(f"Pocet mien: {pocetMien}")
print(f"Dlzka najdlhsieho krstneho mena: {najdlhsieKrstne}")
print(f"Dlzka najdlhsieho priezviska: {najdlhsiePriezvisko}")