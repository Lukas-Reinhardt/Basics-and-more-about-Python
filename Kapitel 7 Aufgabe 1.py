#Kapitel 7 Aufgabe 1 Preisabfrage

Bohrmaschine1=["Marke1",60,1001]
Bohrmaschine2=["Marke2",80,1002]
Bohrmaschine3=["Marke3",100,1003]

B_Liste = [Bohrmaschine1,Bohrmaschine2,Bohrmaschine3]

preis=float(input("Wieviel möchten Sie für die Bohrmaschine bezhalen: "))

if  preis >=100:   
    print(B_Liste[0][:])
    print(B_Liste[1][:])
    print(B_Liste[2][:])
elif (preis <100 and preis >=80):
    print(B_Liste[0][:])
    print(B_Liste[1][:])
elif (preis <80 and preis >60):
    print(B_Liste[0][:])
else :
    print("Wir haben keine Bohrmaschine in dieser Preisklasse")