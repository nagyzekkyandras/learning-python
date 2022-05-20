print('1. feladat')
adatok = []
with open('kep.txt', 'r', encoding='utf-8') as file:
    for i in file:
        adatok.append(i.rstrip('\n'))

#print(adatok) # tesztelés

print('2. feladat')
jo = 0
red = int(input("adja meg a piros kódját: "))
green = int(input("adja meg a zöld kódját: "))
blue = int(input("adja meg a kék kódját: "))

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[0]) == red:
        if int(sor[1]) == green:
            if int(sor[2]) == blue:
                jo = jo + 1

if jo != 0:
    print(f'a megadott színkód szerepel a képen')
else:
    print(f'a megadott színkód nem szerepel a képen')

print('3. feladat')
point_red = 0
point_green = 0
point_blue = 0
point35x8 = 34 * 50 + 8
row = 34*50

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if i == point35x8:
        point_red = int(sor[0])
        point_green = int(sor[1])
        point_blue = int(sor[2])

    if i > 34*50 and i <= 35*50: # 35. sor
        if int(sor[0]) == point_red:
            if int(sor[1]) == point_green:
                if int(sor[2]) == point_blue:
                    print(f' sor: {i//50} Oszlop: {i%50}')

    if i%50 == 8: # 8. oszlop
        if int(sor[0]) == point_red and int(sor[1]) == point_green and int(sor[2]) == point_blue:
            print(f' sor: {i//50} Oszlop: {i%50}')

print('4. feladat')
voros=0
zold=0
kek=0
legtobb=0
neve=""

for i in range(0, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[0]) == 255 and int(sor[1]) == 0 and int(sor[2]) == 0:
        voros = voros + 1

    if int(sor[0]) == 0 and int(sor[1]) == 255 and int(sor[2]) == 0:
        zold = zold + 1

    if int(sor[0]) == 0 and int(sor[1]) == 0 and int(sor[2]) == 255:
        kek = kek + 1

if voros > legtobb:
    legtobb = voros
    neve="vörös"
if zold > legtobb:
    legtobb = zold
    neve="zöld"
if kek > legtobb:
    legtobb = kek
    neve="kék"

print(f'legtöbb: {neve}')

print('4. feladat')
print('5. feladat')
file=open("keretes.txt", "w")

for i in range(1, len(adatok)):
    sor = adatok[i].split(" ")

    if i < 151:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    elif i > 2350:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    elif i%50 == 1:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    elif i%50 == 2:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    elif i%50 == 3:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    elif i%50 == 48:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    elif i%50 == 49:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    elif i%50 == 0:
        sor[0]=0
        sor[1]=0
        sor[2]=0
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")
    else:
        file.write(str(sor[0])+" "+str(sor[1])+" "+str(sor[2])+"\n")

file.close()
print('7. feladat')
kezd=0
veg=0
vane=0

for i in range(1, len(adatok)):
    sor = adatok[i].split(" ")

    if int(sor[0]) == 255 and int(sor[1]) == 255 and int(sor[2]) == 0:
        if int(vane) == 0:
            vane = vane + 1
            kezd = i
        else:
            veg = i
            vane = vane + 1

print(f'Kezd: {kezd//50}, {kezd%50}')
print(f'Vége: {veg//50}, {veg%50}')
print(f'Képpontok száma: {vane}')
