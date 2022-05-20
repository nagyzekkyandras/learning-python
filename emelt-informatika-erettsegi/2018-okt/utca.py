print("1. feladat")
file=open("kerites.txt")
adatok=[]
ps=[]
ptl=[]


for i in file:
    adatok.append(i.rstrip('\n'))
    db=i.rstrip('\n').split(' ')
    if db[0]=="0":
        ps.append(i.rstrip('\n'))
    if db[0]=="1":
        ptl.append(i.rstrip('\n'))

print("2. feladat")
print("Az eladott telkek száma: "+str(len(adatok)))

print("3. feladat")

db=adatok[-1].split(" ")
if db[0]=="0":
    print("A páros oldalon adták el az utolsó telket.")
    print("Az utolsó telek házszáma: "+ str(len(ps)*2))
if db[0]=="1":
    print("A páratlan oldalon adták el az utolsó telket.")
    print("Az utolsó telek házszáma: "+str(len(ptl)*2-1))

print("4. feladat")
# : # --> ezeknél nem kell kiírni, csak akkor ha színek

elozoszin=""
hazszam=-1
for i in ptl:
    db=i.split(" ")
    db[2] # mostani szín
    if (elozoszin==db[2] and db[2]!=":" and db[2]!="#" and elozoszin!=":" and elozoszin!="#"):
        print("A szomszédossal egyezik a kerítés színe: "+str(hazszam))
        
        break
    hazszam=hazszam+2
    elozoszin=db[2]
    
print("5. feladat")
hsz=int(input("Adjon meg egy házszámot! "))
szin1=""
szin2=""

if hsz%2==0: #ps
    index=int(hsz/2)
    
    print("A kerítés színe / állapota: "+ps[index-1].split(" ")[2])
    szin1=ps[index-2].split(" ")[2]
    szin2=ps[index].split(" ")[2]

    
if hsz%2==1: #ptl
    index=int(hsz/2)
   
    print("A kerítés színe / állapota: "+ptl[index].split(" ")[2])
    szin1=ptl[index-1].split(" ")[2]
    szin2=ptl[index+1].split(" ")[2]



szinek=set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if (szin1!=":" and szin1!="#"):
    szinek.remove(szin1)
if (szin2!=":" and szin2!="#"):
    szinek.remove(szin2)
print("Egy lehetséges festési szín: " +szinek.pop())

print("6. feladat")

file2=open("utcakep.txt","w")

for i in ptl:
    
    hossz=int(i.split(" ")[1])
    for x in range(0,hossz,1):
        #print(,end="")
        file2.write(i.split(" ")[2])

file2.write("\n")

hazszam=1
for i in ptl:
    file2.write(str(hazszam))
    #print(hazszam,end="")
    hossz=int(i.split(" ")[1])-1
    
    
    if hazszam>9:
        hossz=hossz-1
        
    if hazszam>99:
        hossz=hossz-1
        
    
    for x in range(0,hossz,1):
        
        file2.write(" ")
    hazszam=hazszam+2


file2.close()
