print("1. feladat")

adatok = []

with open("szavazatok.txt", 'r', encoding="utf-8") as fajl:
    for i in fajl:
        adatok.append(i.rstrip('\n'))

#print(adatok) # tesztelés

print("2. feladat")
print(f'A helyhatósági választáson {len(adatok)} képviselőjelölt indult.')

print("3. feladat")
vezeteknev = input("Adja meg a jelölt vezetéknevét: ")
utonev = input("Adja meg a jelölt utónevét: ")
neve = ""
szavazatok = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if str(sor[2]) == vezeteknev:
        if str(sor[3]) == utonev:
            szavazatok = int(sor[1])
            neve = sor[2]+" "+sor[3]

if neve == "":
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
else:
    print(f'{neve} - {szavazatok}')

print("4. feladat")
jogosult = 12345
szavazott = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    szavazott = int(szavazott)+int(sor[1])

print(f'A választáson {jogosult} állampolgár, a jogosultak {round(szavazott/jogosult*100, 2)}%-a vett részt.')

print("5. feladat")
partatlan = 0
gyep = 0
hep = 0
tisz = 0
zep = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if sor[4] == "-":
        partatlan = int(partatlan) + int(sor[1])

    if sor[4] == "GYEP":
        gyep = int(gyep) + int(sor[1])

    if sor[4] == "HEP":
        hep = int(hep) + int(sor[1])

    if sor[4] == "TISZ":
        tisz = int(tisz) + int(sor[1])

    if sor[4] == "ZEP":
        zep = int(zep) + int(sor[1])

print(f'Pártatlan szavazatok= {round(partatlan/szavazott*100, 2)}%')
print(f'GYEP szavazatok= {round(gyep/szavazott*100, 2)}%')
print(f'HEP szavazatok= {round(hep/szavazott*100, 2)}%')
print(f'TISZ szavazatok= {round(tisz/szavazott*100, 2)}%')
print(f'ZEP szavazatok= {round(zep/szavazott*100, 2)}%')

print("6. feladat")
legtobb = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[1]) > int(legtobb):
        legtobb = sor[1]


for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if sor[1] == legtobb:
        print(f'{sor[2]} {sor[3]} - {sor[4]}')

print("7. feladat")
elso = 0
masodik = 0
harmadik = 0
negyedik = 0
otodik = 0
hatodik = 0
hetedik = 0
nyolcadik = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[0]) == 1:
        if int(sor[1]) > int(elso):
            elso = int(sor[1])

    if int(sor[0]) == 2:
        if int(sor[1]) > int(masodik):
            masodik = int(sor[1])

    if int(sor[0]) == 3:
        if int(sor[1]) > int(harmadik):
            harmadik = int(sor[1])

    if int(sor[0]) == 4:
        if int(sor[1]) > int(negyedik):
            negyedik = int(sor[1])

    if int(sor[0]) == 5:
        if int(sor[1]) > int(otodik):
            otodik = int(sor[1])

    if int(sor[0]) == 6:
        if int(sor[1]) > int(hatodik):
            hatodik = int(sor[1])

    if int(sor[0]) == 7:
        if int(sor[1]) > int(hetedik):
            hetedik = int(sor[1])

    if int(sor[0]) == 8:
        if int(sor[1]) > int(nyolcadik):
            nyolcadik = int(sor[1])

file=open("kepviselok.txt", "w")
for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[0]) == 1 and int(sor[1]) == int(elso):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")
    if int(sor[0]) == 2 and int(sor[1]) == int(masodik):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")
    if int(sor[0]) == 3 and int(sor[1]) == int(harmadik):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")
    if int(sor[0]) == 4 and int(sor[1]) == int(negyedik):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")
    if int(sor[0]) == 5 and int(sor[1]) == int(otodik):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")
    if int(sor[0]) == 6 and int(sor[1]) == int(hatodik):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")
    if int(sor[0]) == 7 and int(sor[1]) == int(hetedik):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")
    if int(sor[0]) == 8 and int(sor[1]) == int(nyolcadik):
        print(f'{sor[0]} - {sor[1]} - {sor[2]} {sor[3]} - {sor[4]}')
        if sor[4] == "-":
            sor[4] == "független"
        file.write(sor[0]+" - "+sor[1]+" - "+sor[2]+" "+sor[3]+" - "+sor[4]+"\n")

file.close()
        
