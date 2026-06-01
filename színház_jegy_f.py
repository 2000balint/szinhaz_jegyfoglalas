adatbazis=[]
with open("adatbazis.txt","rt",encoding="utf-8")as f:
    fejlec=f.readline()
    for sor in f:
        sor_adatok=sor.strip().split(";")
        if len(sor_adatok)==3:
            adatbazis.append(sor_adatok)

szindarab=input("Mit szeretnél nézni?\n"
"-> Pál utcai fiúk\n"
"-> Dzsungel könyve\n"
"-> A diktátor\n"
"-> Frankenstein\n"
)

print(f"\nA {szindarab} időpontjai:")
print("-" * 40)
 
for eloadas in adatbazis:
    nap=eloadas[0]
    idopont=eloadas[1]
    cim=eloadas[2]
    
    if szindarab in cim:
        print(f"-> {nap}-{idopont}-kor")
print()
mikor=input("Mikor szeretnéd nézni? ")
print("-" * 40)
print("Szuper! Következő lépés a helyfoglalás.")

with open("helyfoglalas.txt", "rt", encoding="utf-8") as f:
        fejlec=f.readline()
        tartalom = f.read().split()
 
        nezoter = [x for x in tartalom]
 
        for y in range(0, len(nezoter), 21):
            print(" ".join(nezoter[y:y+21]))

sor = int(input("Add meg a sort: "))
szek = int(input("Add meg a széket: "))

index = (sor - 1) * 21 + (szek - 1)

if 0 <= index < len(nezoter):
    if nezoter[index] != "X":
        nezoter[index] = "X"
        print("A helyet lefoglaltad!")
    else:
        print("Ez a hely már foglalt!")
else:
    print("Nincs ilyen hely a nézőtéren!")
with open("helyfoglalas.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(nezoter))