print("1. feladat")

sorozat = []
gyujt = []

i = 1
with open('lista.txt', "r", encoding="utf-8") as in_file:
    szoveg = in_file.readline()
    for sor in szoveg:
        sor = sor.strip()
        if i % 5 == 0:
            gyujt.insert(i-1,sor)
            sorozat.append(gyujt)
            gyujt = []
            i += 1
        else:
            gyujt.insert((i-1),sor)
            i += 1

print(sorozat) # teszteleshez

print("2. feladat")
statisztika = {}
lattamar = {}
idot = {}

for sor in sorozat:
    nincs = sor[0]
    latta = sor[4]
    statisztika[nincs] = statisztika.get(nincs,0) + 1
    lattamar[latta] = lattamar.get(latta, 0) + 1
    idot[latta] = idot.get(latta, 0) + int(sor[3])

print('A listaban', len(sorozat)-statisztika[nincs],'db vetitesi datummal rendelkezo epizod van.')

print("3. feladat")
print('A listaban levo epizodok ',round(lattamar[latta]/len(sorozat)*100, 2),'%-át latta.') 

print("4. feladat")
print('Sorozatnezessel', idot[1]//(60*24),'napot',(idot[1]%(60*24))//60,'orat','es',(idot[1]%(60*24))//60//60,'percet töltött.')

print(idot[1])

print("5. feladat")
datum = input('Adj meg egy datumot éééé.hh.nn fomatumban!')
for sor in sorozat:
    if sor[0] <= datum and sor[-1] == '0':
        print(sor[2],"\t",sor[1])

print("6. feladat")

def hetnapja(ev, honap, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0,3,2,6,0,3,5,1,4,6,2,4]
    if honap < 3:
        ev -= 1
    hetnapja = napok[(ev + ev//4 - ev//100+ev//400 + honapok[honap-1] + nap) % 7]
    return hetnapja

print("7. feladat")
melyik_nap = input("Adj meg egy napot: ")
halmaz = set()
for sor in sorozat:
    if sor[0] != 'NI':
        osszeallit = hetnapja(int(sor[0][:4]), int(sor[0][5:7]), int(sor[0][8:]))
    if osszeallit == melyik_nap:
        halmaz.add(sor[1])
if len(halmaz) == 0:
    print('Az adott napon nem került adásba sorozat.')
else:
    for sor in sorted(halmaz):
        print(sor)

print("8. feladat")
hossz = {}
darab = {}

for sor in sorozat:
    egy_resz_hossza = int(sor[3])
    cim = sor[1]
    darab[cim] = darab.get(cim, 0) + 1
    hossz[cim] = hossz.get(cim, 0) + egy_resz_hossza
with open("summa.txt"):
    for index, sor in darab.item():
        for index2, sor2 in hossz.items():
            if index == index2:
                print(index, sor2, sor, file=out_file)
