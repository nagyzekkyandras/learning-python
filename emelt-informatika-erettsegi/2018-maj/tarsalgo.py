print("1. feladat")
file=open("ajto.txt")
adatok=[]

for i in file:
    adatok.append(i.rstrip('\n'))


print("2. feladat")
print("Az első belépő: "+adatok[0].split(' ')[2])

h=len(adatok)

for i in range(h-1,0,-1):
    if adatok[i].split(' ')[3]=="ki":
        print("Az utolsó kilépő: "+adatok[i].split(' ')[2])
        break

print("3. feladat")
file2=open("athaladas.txt","w")

athaladasok=[]
for i in range(0,101,1):
    athaladasok.append(0)

for i in adatok:
    szemaz=int(i.split(' ')[2])
    athaladasok[szemaz]=athaladasok[szemaz]+1

for i in range(0,101,1):
    if athaladasok[i]!=0:
        #print(str(i)+" "+str(athaladasok[i]))
        file2.write(str(i)+" "+str(athaladasok[i])+"\n")
file2.close()

print("4. feladat")
print("A végén a társalgóban voltak: ")
for i in range(0,101,1):
    if athaladasok[i]%2==1: #ptl
        print(str(i)+" ",end="")
print()


print("5. feladat")
emax=0
ora="9"
perc="0"
bent=0

for i in adatok:
    if i.split(" ")[3]=="be":
        bent=bent+1
    if i.split(" ")[3]=="ki":
        bent=bent-1

    if bent>emax:
        emax=bent
        ora=i.split(" ")[0]
        perc=i.split(" ")[1]

print("Például "+ora+":"+perc+"-kor voltak a legtöbben a társalgóban.")

print("6. feladat")
azon=int(input("Adja meg a személy azonosítóját! "))

print("7. feladat")
for i in adatok:
    if i.split(" ")[2]==str(azon):
        print(i.split(" ")[0]+":"+i.split(" ")[1],end="")
        if i.split(" ")[3]=="be":
            print("-",end="")
        if i.split(" ")[3]=="ki":
            print()

print("8. feladat")
osszp=0
beperc=0
allapot=""

for i in adatok:
    if i.split(" ")[2]==str(azon):
        #print(i.split(" ")[0]+":"+i.split(" ")[1],end="")
        if i.split(" ")[3]=="be":
            #print("-",end="")

            beperc=int(i.split(" ")[0])*60+int(i.split(" ")[1])
            allapot="be"
        if i.split(" ")[3]=="ki":
            #print()
            kiperc=int(i.split(" ")[0])*60+int(i.split(" ")[1])
            osszp=osszp+(kiperc-beperc)
            allapot="ki"

if allapot=="be":
    kiperc=int(15)*60+int(00)
    osszp=osszp+(kiperc-beperc)
    print("A(z) "+str(azon)+". személy összesen "+str(osszp)+" percet volt bent, a megfigyelés végén a társalgóban volt. ")   



if allapot=="ki":
    print("A(z) "+str(azon)+". személy összesen "+str(osszp)+" percet volt bent, a megfigyelés végén nem volt a társalgóban. ")
