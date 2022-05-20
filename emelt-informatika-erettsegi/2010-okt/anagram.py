print("1. feladat")

szoveg = input("Adja meg a szöveget: ")
print(f'A beírt szöveg: {szoveg}, hossza: {len(szoveg)}')

print("2. feladat")
szavakLista = []

with open("szotar.txt", "r") as szList:
    for egySzo in szList:
        szavakLista.append(egySzo.strip("\n"))

#print(szavakLista)

print("3. feladat")
# megoldás A
def rendezMinKiv(szo):
    szo = list(szo)
    for i in range(len(szo)-1):
        minIndex = i
        for j in range(i+1, len(szo)):
            if szo[j] < szo[minIndex]:
                minIndex = j
        csere = szo[i]
        szo[i] = szo[minIndex]
        szo[minIndex] = csere
        # szo[i], szo[minIndex] = szo[minIndex], szo[i] # egy soros megoldás

    return ''.join(szo)
# megoldás B
def rendez(szo):
    return ''.join(sorted(szo))

beturendes = []
for egySzo in szavakLista:
    beturendes.append(rendez(egySzo))

#print(beturendes)
with open("abc.txt", "w") as abc:
    for egySzo in beturendes:
        abc.write(egySzo+"\n")

print("4. feladat")
eSzo = input("Kérem az 1. szót: ")
mSzo = input("Kérem a 2. szót: ")

if rendez(eSzo) == rendez(mSzo):
    print("Anagramma")
else:
    print("Nem anagramma")

print("5. feladat")
aSzo = input("Kérek egy szót: ")
tarolo = []
for egySzo in szavakLista:
    if rendez(aSzo) == rendez(egySzo):
        tarolo.append(egySzo)

if len(tarolo) == 0:
    print("Nincs a szótárban anagramma!")
else:
    for egySzo in tarolo:
        print(egySzo)

    print('\n'.join(tarolo))

print("6. feladat")
# magoldas A
maxHossz = len(szavakLista[0])
for egySzo in szavakLista:
    if len(egySzo) > maxHossz:
        maxHossz = len(egySzo)
# megoldas B
maxHossz = max(map(len, szavakLista))

#print(maxHossz)
maxHosszuak = []
for egySzo in beturendes:
    if len(egySzo) == maxHossz and egySzo not in maxHosszuak:
        maxHosszuak.append(egySzo)

for egySzo in maxHosszuak:
    for joSzo in szavakLista:
        if rendez(joSzo) == egySzo:
            print(joSzo)

#print(maxHosszuak)
print("7. feladat ")
# todo
