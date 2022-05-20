# kezdet 17:45
# adat szerkezet
# nap (1-7) | fuvarszám (1-40) | km (max 30)

print('1. feladat')

adatok = []

with open('tavok.txt', 'r', encoding='utf-8') as file:
    for i in file:
        adatok.append(i.rstrip('\n'))

#print(adatok) # tesztelés

print('2. feladat')
sor = adatok[0].split(" ")
print(f'A hét első útja {sor[2]}km volt.')

print('3. feladat')
sor = adatok[-1].split(" ")
print(f'A hét utolsó útja {sor[2]}km volt.')

print('4. feladat')

hetfo = 0
kedd = 0
szerda = 0
csutortok = 0
pentek = 0
szombat = 0
vasarnap = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[0]) == 1:
        hetfo = hetfo + 1

    if int(sor[0]) == 2:
        kedd = kedd + 1

    if int(sor[0]) == 3:
        szerda = szerda + 1

    if int(sor[0]) == 4:
        csutortok = csutortok + 1

    if int(sor[0]) == 5:
        pentek = pentek + 1

    if int(sor[0]) == 6:
        szombat = szombat + 1

    if int(sor[0]) == 7:
        vasarnap = vasarnap + 1

#print(f' {hetfo} {kedd} {szerda} {csutortok} {pentek} {szombat} {vasarnap}')
    
if int(hetfo) == 0:
    print('A futár 1.nap tart szabadnapot')

if int(kedd) == 0:
    print('A futár 2.nap tart szabadnapot')

if int(szerda) == 0:
    print('A futár 3.nap tart szabadnapot')

if int(csutortok) == 0:
    print('A futár 4.nap tart szabadnapot')

if int(pentek) == 0:
    print('A futár 5.nap tart szabadnapot')

if int(szombat) == 0:
    print('A futár 6.nap tart szabadnapot')

if int(vasarnap) == 0:
    print('A futár 7.nap tart szabadnapot')

print('5. feladat')
legnagyobb = 0
nap = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if legnagyobb < int(sor[1]):
        legnagyobb = int(sor[1])
        nap = int(sor[0])

print(f'A legtöbb fuvar a {nap}-on volt. ({legnagyobb}db)')

print('6. feladat')
hetfo = 0
kedd = 0
szerda = 0
csutortok = 0
pentek = 0
szombat = 0
vasarnap = 0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[0]) == 1:
        hetfo = hetfo + int(sor[2])

    if int(sor[0]) == 2:
        kedd = kedd + int(sor[2])

    if int(sor[0]) == 3:
        szerda = szerda + int(sor[2])

    if int(sor[0]) == 4:
        csutortok = csutortok +int(sor[2])

    if int(sor[0]) == 5:
        pentek = pentek + int(sor[2])

    if int(sor[0]) == 6:
        szombat = szombat + int(sor[2])

    if int(sor[0]) == 7:
        vasarnap = vasarnap + int(sor[2])

print(f'1. nap: {hetfo}')
print(f'2. nap: {kedd}')
print(f'3. nap: {szerda}')
print(f'4. nap: {csutortok}')
print(f'5. nap: {pentek}')
print(f'6. nap: {szombat}')
print(f'7. nap: {vasarnap}')


print('7. feladat')
km = int(input("Adja meg a távolságot km-ben: "))
if km < 3:
    print(f'{km}km után 500ft jár.')
elif km < 6:
    print(f'{km}km után 700ft jár.')
elif km < 11:
    print(f'{km}km után 900ft jár.')
elif km < 21:
    print(f'{km}km után 1400ft jár.')
elif km < 31:
    print(f'{km}km után 2000ft jár.')
else:
    print("túl nagy a szám")

print('8. feladat')
# todo megfelelő sorbarendezés
file=open("dijazas.txt", "w")
for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[2]) < 3:
        file.write(sor[0]+". nap "+sor[1]+". út: 500 Ft\n")
    elif int(sor[2]) < 6:
        file.write(sor[0]+". nap "+sor[1]+". út: 700 Ft\n")
    elif int(sor[2]) < 11:
        file.write(sor[0]+". nap "+sor[1]+". út: 900 Ft\n")
    elif int(sor[2]) < 21:
        file.write(sor[0]+". nap "+sor[1]+". út: 1400 Ft\n")
    elif int(sor[2]) < 31:
        file.write(sor[0]+". nap "+sor[1]+". út: 2000 Ft\n")

file.close()
print('9. feladat')
penz=0

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[2]) < 3:
        penz = penz + 500
    elif int(sor[2]) < 6:
        penz = penz + 700
    elif int(sor[2]) < 11:
        penz = penz + 900
    elif int(sor[2]) < 21:
        penz = penz + 1400
    elif int(sor[2]) < 31:
        penz = penz + 2000
    
print(f'A heti bevétel: {penz}ft volt.')

















