tabulka = {0:" ", 1:"ABC", 2:"DEF", 3:"GHI", 4:"JKL", 5:"MNO", 6:"PQR", 7:"STU", 8:"VWX", 9:"YZ"}
pocty = [0] * 10

text = input()

for znak in text:
    for n in tabulka:
        if znak in tabulka[n]:
            print(str(n) * (tabulka[n].find(znak)+1), end = " ")
            pocty[n] += tabulka[n].find(znak)+1
print()

maxHodnota = max(pocty)
print('Najčastejšie zvolené políčka:')
for i in range(10):
    if pocty[i] == maxHodnota:
        print(i, end=' ')

    