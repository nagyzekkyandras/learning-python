print("1. feladat")

adatok = []

with open('jarmu.txt', 'r', encoding='utf-8') as fajl:
    for i in fajl:
        adatok.append(i.rstrip('\n'))

#print(adatok) # tesztelés

print("2. feladat")

maximum = 0
minimum = 100

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")
    if int(sor[0]) > int(maximum):
        maximum = sor[0]
    if int(sor[0]) < int(minimum):
        minimum = sor[0]

hossza = int(maximum) - int(minimum)
print(f'A kezdés időpontja {minimum} óra volt és a vég időpontja {maximum} volt. Munka ideje: {hossza} óra volt.')

print("3. feladat")

aktual = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")
    if int(sor[0] != aktual):
        aktual=sor[0]
        print(f'{int(sor[0])} óra: {sor[3]}')
    
print("4. feladat")

busz = 0
kamion = 0
motor = 0
auto = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")
    if sor[3][0] == "B":
        busz=busz+1
    elif sor[3][0] == "K":
        kamion=kamion+1
    elif sor[3][0] == "M":
        motor=motor+1
    else:
        auto=auto+1

print(f'Busz: {busz} db \namion: {kamion} db \nMotor: {motor} db \nAuto: {auto} db')

print("5. feladat")
# to do

print("6. feladat")
rendszam=input("Adjon meg egy rendszámot: ")
#print(f'A rendszam: {rendszam}') # tesztelés
#print(len(rendszam)) # tesztelés
#print(rendszam[0]) # tesztelés
jo = 0
for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if str(sor[3][0]) == str(rendszam[0]) or str(rendszam[0]) == "*":
        if str(sor[3][1]) == str(rendszam[1]) or str(rendszam[1]) == "*":
            if str(sor[3][2]) == str(rendszam[2]) or str(rendszam[2]) == "*":
                if str(sor[3][3]) == str(rendszam[3]) or str(rendszam[3]) == "*":
                    if str(sor[3][4]) == str(rendszam[4]) or str(rendszam[4]) == "*":
                        if str(sor[3][5]) == str(rendszam[5]) or str(rendszam[5]) == "*":
                            if str(sor[3][6]) == str(rendszam[6]) or str(rendszam[6]) == "*":
                                print(sor[3])

print("7. feladat")

ellenorzes = 0
file=open("vizsgalt.txt","w")

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")
    
    if int(sor[0])*60*60+int(sor[1])*60+int(sor[2]) - ellenorzes > 300:
        file.write(sor[0]+":"+sor[1]+":"+sor[2]+" - "+sor[3]+"\n")
        #print(f'{sor[0]}:{sor[1]}:{sor[2]} - {sor[3]}') # tesztelés
        ellenorzes = int(sor[0])*60*60+int(sor[1])*60+int(sor[2])

file.close()
    
