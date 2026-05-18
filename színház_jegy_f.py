adatbazis=[]
with open("adatbazis.txt","rt",encoding="utf-8")as f:
    fejlec = f.readline()
    for sor in f:
        sor_adatok = sor.strip().split(";")
        if len(sor_adatok) == 3:
            adatbazis.append(sor_adatok)
print(adatbazis)

szindarab=input("Mit szeretnél nézni? ")

print(f"\nA(z) {szindarab} időpontjai:")
print("-" * 40)
 
for eloadas in adatbazis:
    nap=eloadas[0]
    idopont=eloadas[1]
    cim=eloadas[2]
    
    if szindarab.lower() in cim.lower():
        print(f"-> {nap}-{idopont}-kor")