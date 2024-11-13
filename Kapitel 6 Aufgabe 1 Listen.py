#Kapitel 6 Aufgabe 1 Liste Bücher und ausgeben

# Buch1 = {"Titel":"TitelBuch1", "Autor":"AutorBuch1","Artikelnummer":1001,"Preis":12}
# Buch2 = {"Titel":"TitelBuch2", "Autor":"AutorBuch2","Artikelnummer":1002,"Preis":13}
# Buch3 = {"Titel":"TitelBuch3", "Autor":"AutorBuch3","Artikelnummer":1003,"Preis":14}

# Buchliste= [Buch1, Buch2, Buch3]
# print(Buchliste[0],"\n")
# print(Buchliste[1],"\n")
# print(Buchliste[2],"\n")

# print(Buch1["Titel"])
# print(Buch1["Autor"])
# print(Buch1["Artikelnummer"])
# print(Buch1["Preis"],"\n")

# print(Buchliste[0]["Titel"], Buchliste[0]["Autor"])
# print(Buchliste[1]["Titel"], Buchliste[1]["Autor"])

# Buch1 = ["TitelBuch1", "AutorBuch1", 1001, 12]
# Buch2 = ["TitelBuch2", "AutorBuch2", 1002, 13]
# Buch3 = ["TitelBuch3", "AutorBuch3", 1003, 14]

# Buchliste= [Buch1, Buch2, Buch3]
# print(Buchliste[0][:],"\n",Buchliste[1][:],"\n",Buchliste[2][:])

#Kapitel 6 Aufgabe 2 Eine Datenstruktur Speichern

#Speichern mit Tuple

Buch1= "Buchtitel1","Autor1",1001,12
Buch2= "Buchtitel2","Autor2",1002,13
Buch3= "Buchtitel3","Autor3",1003,14

print(Buch1[0],"\n",Buch1[1],"\n",Buch1[2],"\n",Buch1[3])
print(Buch1,"\n",Buch2,"\n",Buch3)
Buchliste= Buch1+Buch2+Buch3#Liste wird verlängert
print(Buchliste[0:6])
Buchliste=(Buch1, Buch2, Buch3)#Liste bekommt eine zusätzliche Dimension
print(Buchliste[0][:])
print(Buchliste[1][:])
print(Buchliste[2][:])