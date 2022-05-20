print("1. feladat")
sorokszama=15
soronkentiszekekszama=20

# fájlok beolvasása
foglaltsag=[]
foglaltsag=open("foglaltsag.txt")

kategoria=[]
kategoria=open("kategoria.txt")

foglaltsag=[line.rstrip('\n') for line in foglaltsag]

kategoria=[line.rstrip('\n') for line in kategoria]

# tesztalés
print("kategoria fájl:")
print(kategoria)
print("foglaltsag fájl:")
print(foglaltsag)

print("2. feladat")
# sor és szék sorszám bekérése majd megnézni hogy szabad-e

print("adja meg a sornak a számát:")
sor=input()
print("adja meg a széknek a számát:")
szek=input()

# tesztelés
#print("sor: "+sor+"\nszék: "+szek)
#print("kiválasztott sor kiiratása")
#print(foglaltsag[int(sor)-1])
#print(foglaltsag[int(sor)-1][int(szek)-1])

if(foglaltsag[int(sor)-1][int(szek)-1] == "x"):
    print("foglalt")
else:
    print("szabad")    

print("3. feladat")

foglalt=0
szabad=0
for i in range(0, sorokszama):
    for j in range(0, soronkentiszekekszama):
        if(foglaltsag[int(i)][int(j)] == "x"):
           foglalt=foglalt+1
        if(foglaltsag[int(i)][int(j)] == "o"): # ellenőrzés
           szabad=szabad+1

osszes=int(szabad)+int(foglalt)
print("Összes hely: "+str(osszes))
print("Az előadásra eddig "+str(foglalt)+" jegyet adtak el")
# ellenőrzés
print("Az előadásra eddig "+str(szabad)+" jegyet nem adtak el")

szazalek=(foglalt/osszes)*100
szazalekegeszben=int(szazalek)
print("ez összesen "+str(szazalekegeszben)+"% foglaltsag")

print("4. feladat")

elso=0
masodik=0
harmadik=0
negyedik=0
otodik=0

for i in range(0, sorokszama):
    for j in range(0, soronkentiszekekszama):
        if(kategoria[int(i)][int(j)] == "1"):
           elso=elso+1
        if(kategoria[int(i)][int(j)] == "2"):
           masodik=masodik+1
        if(kategoria[int(i)][int(j)] == "3"):
           harmadik=harmadik+1
        if(kategoria[int(i)][int(j)] == "4"):
           negyedik=negyedik+1
        if(kategoria[int(i)][int(j)] == "5"):
           otodik=otodik+1

print("1. kategória: "+str(elso)+"\n2. kategória: "+str(masodik)+"\n3. kategória: "+str(harmadik)+"\n4. kategória: "+str(negyedik)+"\n5. kategória: "+str(otodik))
osszkat=elso+masodik+harmadik+negyedik+otodik
print("Összesen kategóriűkból: "+str(osszkat))

legtobb=0
legtobbneve="egyiksem"

if(elso > legtobb):
    legtobb=elso
    legtobbneve="1."
    
if(masodik > legtobb):
    legtobb=masodik
    legtobbneve="2."

if(harmadik > legtobb):
    legtobb=harmadik
    legtobbneve="3."

if(negyedik > legtobb):
    legtobb=negyedik
    legtobbneve="4."

if(otodik > legtobb):
    legtobb=otodik
    legtobbneve="5."   

print("a legtöbb "+legtobbneve+" kategóriás hely: "+str(legtobb)+" darabbal")

print("5. feladat")

bevetel=0
bevetel=(elso*5000)+(masodik*4000)+(harmadik*3000)+(negyedik*2000)+(otodik*1500)
print("össz bevetel: "+str(bevetel))

print("6. feladat")

print("7. feladat")
file=open("szabad.txt","w")
for i in range(0, sorokszama):
    for j in range(0, soronkentiszekekszama):
        if(foglaltsag[int(i)][int(j)] == "o"):
            file.write(kategoria[int(i)][int(j)])
        else:
            file.write(foglaltsag[int(i)][int(j)])

        if(j == soronkentiszekekszama-1):
            file.write("\n")

file.close()




    


