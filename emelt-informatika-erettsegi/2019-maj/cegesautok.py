print("1. feladat")
adatok=[]
file=open("autok.txt")

for i in file:
    adatok.append(i.rstrip('\n'))

print("2. feladat")
rendszam=""
nap=""
for i in adatok:
    db=i.split(" ")
    if db[5]=="0": # kihajtás
        rendszam=db[2]
        nap=db[0]

print(nap+". nap rendszám: "+rendszam)

print("3. feladat")
nap=int(input("Nap: "))

for i in adatok:
    db=i.split(" ")
    if (int(db[0])==nap and db[5]=="0"):
        print(db[1]+" "+db[2]+" "+db[3]+" ki")
    if (int(db[0])==nap and db[5]=="1"):
        print(db[1]+" "+db[2]+" "+db[3]+" be")

print("4. feladat")
autokint=0

for i in adatok:
    db=i.split(" ")
    if db[5]=="0": #kihajtás
        autokint=autokint+1
    if db[5]=="1": # behajtás
        autokint=autokint-1
print("A hónap végén "+str(autokint)+" autót nem hoztak vissza.")

print("5. feladat")
for x in range(0,10):
    
    kezdokm=-1
    vegkm=-1
    rsz="CEG30"+str(x)

    for i in adatok:
        db=i.split(" ")
        
        if rsz==db[2]:
            if kezdokm==-1:
                kezdokm=int(db[4])
            vegkm=int(db[4])

    print(rsz+" "+str(vegkm-kezdokm))


print("6. feladat")
maxkm=0
maxid=0

szamlalo=0 #sorok száma (ki/be lépések száma)

for i in adatok:
    db=i.split(" ")
    if db[5]=="1": #behajtás, visszahozás
        for j in range(szamlalo-1,-1,-1):
            dbx=adatok[j].split(" ")
            if (dbx[5]=="0" and dbx[2]==db[2]):
                ut=int(db[4])-int(dbx[4])

                if ut>maxkm:
                    maxkm=ut
                    maxid=db[3]

                break

    szamlalo=szamlalo+1

print("Leghosszabb út: "+str(maxkm)+" km, személy: "+str(maxid))

print("7. feladat")
rendszam=input("Rendszám: ")
file=open(rendszam+"_menetlevel.txt","w")

for i in adatok:
    db=i.split(" ")
    if db[2]==rendszam:
        if db[5]=="0": #ki
            file.write(db[3]+"\t"+db[0]+". "+db[1]+"\t"+db[4]+" km")
            

        if db[5]=="1": #be
            file.write("\t"+db[0]+". "+db[1]+"\t"+db[4]+" km\n")

file.close()
print("\nMenetlevél kész")
