import random

pocetStudentov = int(input("Pocet studentov:"))
pocetOtazok = int(input("Pocet otazok:"))

while pocetStudentov>pocetOtazok:
    print("Pocet studentov nesmie byt vyssi ako pocet otazok")
    pocetStudentov = int(input("Pocet studentov:"))
    pocetOtazok = int(input("Pocet otazok:"))

otazky = list(range(1, pocetOtazok+1))
studenti = list(range(1, pocetStudentov+1))

otazkyParne = otazky[1::2]
otazkyNeparne = otazky[::2]
random.shuffle(otazkyParne)
random.shuffle(otazkyNeparne)
otazky = []
for i in range(len(otazkyParne)):
    otazky = otazky + [otazkyParne[i], otazkyNeparne[i]]
if len(otazkyNeparne) > len(otazkyParne):
    otazky.append(otazkyNeparne[-1])

# random.shuffle(otazky)
random.shuffle(studenti)

for i in range(len(studenti)):
    print(f'{i+1}. student: {studenti[i]}, otazka: {otazky[i]}')



