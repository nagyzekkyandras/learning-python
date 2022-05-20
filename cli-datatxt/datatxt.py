#!/usr/bin/python

print('1. feladat')
adatok = []
file = open("machine.txt")
adatok=[line.rstrip('\n') for line in file]

print('2. feladat')
print(len(adatok))

print('3. feladat')
nemvm = 0
vm = 0
for i in range(0, len(adatok)):
    sordb=adatok[i].split(' ')
    if(sordb[2] == '-'):
        nemvm=nemvm+1
    else:
        vm=vm+1

print("nem vm:"+str(nemvm))
print("vm:"+str(vm))

print('4. feladat')
for i in range(0, len(adatok)):
    sordb=adatok[i].split(' ')
    print(sordb)

print('5. feladatok')

lista=[]
for i in range(0, len(adatok)):
    lista.append(0)

print("vm-ek:")
for i in range(0, len(adatok)):
    sordb=adatok[i].split(' ')
    if(sordb[2] != '-'):
        print(sordb)

print("\nhw-ek:")
for i in range(0, len(adatok)):
    sordb=adatok[i].split(' ')
    if(sordb[2] == '-'):
        print(sordb)