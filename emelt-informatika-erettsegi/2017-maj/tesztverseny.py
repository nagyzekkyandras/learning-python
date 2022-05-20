print("1. feladat")
# adatszerkezet kialakítása

adatok = []

with open("valaszok.txt", "r", encoding="utf-8") as valaszok:
    for i in valaszok:
        adatok.append(i.rstrip('\n'))

# tesztelés
#print(adatok)
#print(adatok[1])

print("2. feladat")
print("A vetélkedőn "+str(len(adatok)-1)+" versenyző indult.")

print("3. feladat")
azon=input("A versenyző azonosítója = ")

for i in range(1, len(adatok)):
    sor = adatok[i].split(" ")
    if(azon == sor[0]):
        print(sor[1])
        

print("4. feladat")
print(adatok[0])

megoldas=[]

for i in range(1, len(adatok)):
    sor = adatok[i].split(" ")
    if(azon == sor[0]):
        for j in range(0, 13):
            if(adatok[0][j] == sor[1][j]):
                megoldas.append("+")
            else:
                megoldas.append(" ")

for i in range(0, len(megoldas)):
    print(megoldas[i], end ="")
print(" ")
print("5. feladat")
sorsz=int(input("A feladat sorszáma = "))

helyes=0

for i in range(1, len(adatok)):
    sor = adatok[i].split(" ")
    if(adatok[0][sorsz-1] == sor[1][sorsz-1]):
        helyes=helyes+1

ossz=len(adatok)-1
szazalek=helyes/ossz*100

print("A feladatra "+str(helyes)+" fő, a versenyzők "+str('{0:.2f}'.format(szazalek))+"%-a adott helyes választ.")

print("6. feladat")

# 1-5 feladat 3 pont
# 6-10 feladat 4 pont
# 11-13 feladat 5 pont
# 14 feladat 6 pont

file=open("pontok.txt","w")

for i in range(1, len(adatok)):
    sor = adatok[i].split(" ")

    aktPont = 0
    for j in range(0,14):
        if(adatok[0][j] == sor[1][j]):
            if( j <= 4):
                aktPont=aktPont+3
            elif( j <= 9):
                aktPont=aktPont+4
            elif( j <= 12):
                aktPont=aktPont+5
            elif( j <= 13):
                aktPont=aktPont+6
    #print(sor[0]+" "+str(aktPont)+"\n") # tesztelés
    file.write(sor[0]+" "+str(aktPont)+"\n")
    aktPont=0
    
file.close()

print("7. feladat")
#todo
