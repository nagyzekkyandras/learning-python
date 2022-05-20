print("1. feladat")
# file beolvasas
adatok = []

with open("tavirathu13.txt", "r", encoding="utf-8") as metAdatok:
    for egySor in metAdatok:
        egySor = egySor.strip() # sorvegi \n miatt
        egySorLista = egySor.split(" ")
        telepules = egySorLista[0]
        ido = egySorLista[1]
        szelirany = egySorLista[2][0:3]
        szelero = egySorLista[2][3:]
        homerseklet = int(egySorLista[3])
        adatok.append([telepules,ido,szelirany,szelero,homerseklet])

# teszteles
#print(adatok)

print("2. feladat")
varos = input("Kérek egy várost: ")

# kivalasztas tetele
i = len(adatok) -1
while adatok[i][0] != varos:
    i -= 1

print(f"Az utolsó mérési adat a megadott településről {adatok[i][1][0:2]}:{adatok[i][1][2:]}-kor érkezett.")

print("3. feladat")

# maximum kivalasztas tetele
maxi = 0
# minimum kivalasztas tetele
mini = 0

for i in range(0, len(adatok)):
    if(adatok[i][4] < adatok[mini][4]):
        mini = i
    if(adatok[i][4] > adatok[maxi][4]):
        maxi = i

print(f"A legalacsonyabb homerseklet: {adatok[mini][0]} {adatok[mini][1][0:2]}:{adatok[mini][1][2:]} {adatok[mini][4]} fok.")
print(f"A legmagasabb homerseklet: {adatok[maxi][0]} {adatok[maxi][1][0:2]}:{adatok[maxi][1][2:]} {adatok[maxi][4]} fok.")

print("4. feladat")
# kivalogatas tetle
szelcsendLista = []
for egyAdat in adatok:
    if(egyAdat[2] == "000"):
        szelcsendLista.append(egyAdat)

if(len(szelcsendLista) > 0):
    for egyAdat in szelcsendLista:
        print(f"{egyAdat[0]} {egyAdat[1][0:2]}:{egyAdat[1][2:]}")
else:
    print("Nem volt szélcsend a mérések idején.")

print("5. feladat")
# kivalogatas
# szotar
telepulesAdatok = {}
for egyAdat in adatok:
    if(egyAdat[0] not in telepulesAdatok.keys()):
        telepulesAdatok[egyAdat[0]] = {"01": [0, 0],
                                       "07": [0, 0],
                                       "13": [0, 0],
                                       "19": [0, 0],
                                       "min": egyAdat[4],
                                       "max": egyAdat[4]}

for varos in telepulesAdatok.keys():
    for egyAdat in adatok:
        if(egyAdat[0] == varos and egyAdat[4] < telepulesAdatok[varos]["min"]):
            telepulesAdatok[varos]["min"] = egyAdat[4]

        if(egyAdat[0] == varos and egyAdat[4] > telepulesAdatok[varos]["max"]):
            telepulesAdatok[varos]["max"] = egyAdat[4]

for egyAdat in adatok:
    if(egyAdat[1][0:2] in telepulesAdatok[egyAdat[0]].keys()):
        telepulesAdatok[egyAdat[0]][egyAdat[1][0:2]][0] += egyAdat[4]
        telepulesAdatok[egyAdat[0]][egyAdat[1][0:2]][1] += 1

# teszteles
#print(telepulesAdatok)

def kozepHomerseklet(ertekek):
    values = list(ertekek.values())
#    print(values) # teszteles
    s = 0
    db = 0
    i = 0
    while i < 4 and values[i][1] != 0:
        s += values[i][0]
        db +=values[i][1]
        i += 1
    if(i < 4):
        return "NA"
    else:
        return s // db

def ingadozas(ertekek):
#    print(ertekek) # teszteles
    values = list(ertekek.values())
#    print(values) # teszteles
    return values[5] - values[4]

for key, values in telepulesAdatok.items():
    print(f"{varos} {kozepHomerseklet(values)}; hőmérséklet-ingadozás: {ingadozas(values)}")

print("6. feladat")
szelErosseg = {}
for egyTelepules in telepulesAdatok.keys():
    szelErosseg[egyTelepules] = []

for egyMeres in adatok:
    szelErosseg[egyMeres[0]].append([egyMeres[1], int(egyMeres[3])])

def szelero(meres):
    return "#"*int(meres)

#print(szelErosseg) # teszteles

for egyTelepules, szelMeres in szelErosseg.items():
    with open(egyTelepules+".txt", "w", encoding="utf-8") as telepules:
        telepules.write(f"{egyTelepules}\n")
        for egyMeres in szelMeres:
            telepules.write(f"{egyMeres[0]} {szelero(egyMeres[1])}\n")
            
