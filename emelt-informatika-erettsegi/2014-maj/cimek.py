print("1. feladat")
# file beolvasás
adatok=[]
file=open("ip.txt")

adatok=[line.rstrip('\n') for line in file]

print(adatok) # teszteléshez

print("2. feladat")
# összes adat
print("Ennyi adat van "+str(len(adatok))+" összesen")

print("3. feladat")
# legkissebb cím
print("a legalacsonyabb tárolt IP-cím:")
print(min(adatok))

print("4. feladat")
# csoportosítás

# dokumentációs címek
dc=0

for i in range(0, len(adatok)):
    sordb=adatok[i].split(':')

    if(sordb[0] == "2001"):
        if(sordb[1] == "0db8"):
#            print(sordb[0]+":"+sordb[1]) # tesztelés
            dc=dc+1

print("Dokumentációs cím: "+str(dc))

# Globális egyedi címek
gc=0

for i in range(0, len(adatok)):
    sordb=adatok[i].split(':')

    if(sordb[0] == "2001"):
        if("0e" in sordb[1]):
#            print(sordb[0]+":"+sordb[1]) # tesztelés
            gc=gc+1

print("Globális egyedi cím:"+str(gc))

# helyi egyedi címek
fc=0

for i in range(0, len(adatok)):
    sordb=adatok[i].split(':')

    if("fc" in sordb[0]):
#        print(sordb[0]) # tesztelés
        fc=fc+1

print("Helyi egyedi cím:"+str(fc))

print("5. feladat")
# fileba írás
file2=open("sok.txt","w")

for i in range(0, len(adatok)):
#    print(i) # sorszám tesztelése
#    print(adatok[i].count('0')) # 0-k darabszámának kiiratása
    nullakszama=adatok[i].count('0')
    if(int(nullakszama) > 17):
#        print(str(i+1)+" "+str(adatok[i]))) # teszteléshez
        file2.write(str(i+1)+" "+str(adatok[i]+"\n"))
file2.close()

print("6. feladat")
# rövidítés

print("adjon meg egy számot:")
sorszam = input()
#print("a szám amit megadott: "+sorszam) # tesztelés
for i in range(0, len(adatok)):
    if(int(sorszam) == i+1):
        print("sorszám: "+str(sorszam)+", "+str(adatok[i]))

#for i in range(0, len(adatok)):
        sordb=adatok[i].split(':')
        for j in range(0, 8):
            if(sordb[j] == "0000"):
                sordb[j]="0"
#                print(sordb[j])
#            else:
#                print(sordb[j])
        print("rövidítése:\n"+str(sordb[0])+":"+str(sordb[1])+":"+str(sordb[2])+":"+str(sordb[3])+":"+str(sordb[4])+":"+str(sordb[5])+":"+str(sordb[6])+":"+str(sordb[7]))

print("7. feladat")
        













