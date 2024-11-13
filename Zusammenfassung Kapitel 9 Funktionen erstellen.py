#Kapitel 9 Funktionen erstellen

#Allgemeine Form
# def begruessung():
#     print("Herzlich willkommen")
    
# begruessung()

###########
# #Mit Wert übergebe
# def begruessung(name):
#     print("Herzlich willkommen",name)
    
# name="Lukas"
# begruessung(name)
# #oder einfach
# begruessung("Lukas")
# # Mit zuvorriger abfrage des Nahmen
# eingabe=input("Gebe deinen Namen ein: ")
# begruessung(eingabe)

#####
# # Mehrere Werte übergeben
# def begruessung(name,zahl):
#     print("Herzlich willkommen",name)
#     print("die eingegebene Zahl: ",zahl)

# eingabe1=input("Wie ist dein Name? :")
# eingabe2=int(input("Gebe eine Zahl ein: "))

# begruessung(eingabe1, eingabe2)

# # Jede Übergabevariable muss einen wert enthalten. Man kann mittels volgender methode
# # einen Standardwert übergeben, der abgeändert werden kann
# def personendaten(name="unbekannt",wohnort="unbekannt",alter="unbekannt"):
#     print("Name: ",name)
#     print("Wohnort: ",wohnort)
#     print("alter: ",alter,"\n")

# personendaten()
# personendaten("Herbert Müller")
# personendaten("Herbert Müller","Darmstadt")
# personendaten("Herbert Müller","Darmstadt",70)
# personendaten(alter=70)

##############
# #Funktionen die einen Wert zurück geben mittels return
# #return beendet die Funktion automatisch
# def formel(x):
#     wert=2*x*x+4*x+8
#     return wert

# wert=formel(4)
# print(wert)

# #oder die Kürzere Variante
# def forel(x):
#     return 2*x*x+4*x+8

# print(formel(4))

#####
# #Merhere Werte zurück in form von Liste, Dictionary oder Tupel
# def formel(x):
#     wert1= 2*x**2+4*x+8
#     wert2= 7*x**2+3*x+3

# # Es ist wichtg, dass sich die Datei im Selben Ordner wie die Hauptfunktion befindet
# # anstensten muss zusätzlich der Pfadnahme mit aufgerufen werden
# import Bsp_Modulordner.Bsp_Unterfunktion
#     return[wert1,wert2]#Listen Form

# ergebnisse=formel(4)
# print("Ergebnis der ersten Formel",ergebnisse[0] )
# print("Ergebniss der zweiten Formel",ergebnisse[1])

# # Return beendet Funktion. Mit if else funktionen wahlweise returns erzeugen möglich
# def formel(x):
#     if x<50:
#         return 2*x**2+4*x+8
#     else:
#         return 7*x**2+3*x+3
    
# eingabe= int(input("Gebe eine Zahl ein: "))
# print(formel(eingabe))

##########
# # Funktion aus einer Anderen Datei laden mittels import-Befehl
# import Bsp_Unterfunktion #(Dateinname)
# eingabe=int(input("Gebe eine Zahl ein:"))
# print(Bsp_Unterfunktion.formel(eingabe))
# eingabe=int(input("Gib eine Zahl ein: "))
# print(Bsp_Modulordner.Bsp_Unterfunktion.formel(eingabe))

# # Datenpfad in schlagwort für kürzeren Text
# import Bsp_Modulordner.Bsp_Unterfunktion
# f= Bsp_Modulordner.Bsp_Unterfunktion.formel
# eingabe=int(input("Gebe deine Zahl ein: "))
# print(f(eingabe))

