print("1. feladat")

vasarlasok = []
kosar = {}

with open("penztar.txt", 'r', encoding="utf-8") as fajl:
    for sor in fajl:
        if sor.strip() == 'F':
            vasarlasok.append(kosar)
            kosar = {}
        else:
            if sor.strip() not in kosar:
                kosar[sor.strip()] = 1
            else:
                kosar[sor.strip()] += 1

#print(vasarlasok) # tesztelés

print("2. feladat")
print(f'A fizetések száma: {len(vasarlasok)}')

print("3. feladat")
szamlalo = 0
for arucikk in vasarlasok[0]:
    szamlalo += vasarlasok[0][arucikk]
print(f'Az elso vasarlo {szamlalo} darab arucikket vásárolt')

print("4. feladat")
sorszam = int(input('Adja meg egy vásárlás sorszámát! '))
aru = input('Adja meg egy árucikk nevét! ')
darab = int(input('Adja meg a várásolt darabszámot! '))

print("5. feladat")
meg_nem = True
szamlalo = 0
utolso = 0

for index, kosar in enumerate(vasarlasok):
    for arucikk in kosar:
        if arucikk == aru and meg_nem:
            print(f'Az első vásárlás sorszáma: {index + 1}')
            meg_nem = False
        if arucikk == aru:
            szamlalo += 1
            utolso = index
print(f'Az utolsó vásárlás sorszáma: {utolso + 1}')
print(f'{szamlalo} vásárlás során vettek belőle.')

print("6. feladat")
def ertek(db):
    if db == 1:
        return 500
    elif db == 2:
        return 500 + 450
    else:
        return 500 + 450 + (db - 2) * 400

print(f'{darab} darab vételekor fizetendő: {ertek(darab)}')

print("7. feladat")
for arucikk in vasarlasok[sorszam-1]:
    print(f'{vasarlasok[sorszam-1][arucikk]} {arucikk}')

print("8. feladat")
with open('osszeg.txt', 'w', encoding="utf-8") as osszeg:
    for index, kosar in enumerate(vasarlasok):
        fizetendo = 0
        for arucikk in kosar:
            fizetendo += ertek(kosar[arucikk])
        print(f'{index + 1}: {fizetendo}', file=osszeg.txt)

