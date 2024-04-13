with open('nastenka.txt', 'r') as nastenka:
    riadky = nastenka.readlines()

with open('zoznam.txt', 'w') as zoznam:
    pismena_v_slove={}
    pismena_celkovo={}
    for riadok in riadky:
        for znak in riadok.strip():
            if znak!=' ':
                if znak in pismena_v_slove:
                    pismena_v_slove[znak]+=1
                else:
                    pismena_v_slove[znak]=1

                if znak in pismena_celkovo:
                    pismena_celkovo[znak]+=1
                else:
                    pismena_celkovo[znak]=1
        for pismeno in pismena_v_slove:
            zoznam.write(f'{pismeno} {pismena_v_slove[pismeno]}\n')
        zoznam.write('\n')
        pismena_v_slove={}
    zoznam.write('\n')
    for pismeno in pismena_celkovo:
            zoznam.write(f'{pismeno} {pismena_celkovo[pismeno]}\n')

