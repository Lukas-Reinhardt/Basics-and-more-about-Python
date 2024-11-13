# Kapitel 8 Schleifen

#while Bedingung:
#    Befehle werden ausgeführt, solange die Bedingung zutrifft
#Bsp.1
# n=0
# while n<=100:
#     print(n)
#     n=n+1
#Bsp.2
# weiter = "ja"
# while weiter == "ja":
#     zahl= int(input("Gib eine Zahl zum verdoppeln ein: "))
#     print("Doppelter wert von",zahl,"ist",zahl*2)
#     weiter= input("Möchten Sie vortfahren ? (ja/nein)")

#Listen ausgeben mit while Schleife ist unpraktisch
#Bsp. while vs for
# liste=[3,6,12,14,2]
# i=0
# while i<len(liste):
#     print(liste[i])
#     i+=1
    
# for inhalt in liste:
#     print(inhalt)

# dic = {"artikelnummer":10010,"leistung":850,"marke":"Bosch","preis":60}
# for inhalt in dic :
#     print(inhalt, dic[inhalt])
    
# #Wärte innerhalb einer Liste lassen sich nicht mit for schleife ändern, nur ausgeben
# #Es sei denn unter verwendung der funktion enumerate(). Gibt liste zurück die Tupel enthält

# liste=[3,6,12,14,2]
# print(liste)

# # for inhalt in liste:
# #     inalt=inhalt*2
# # print (liste)

# for inhalt in enumerate(liste):
#     liste[inhalt[0]] = inhalt[1]*2
# print (liste)

# # #for-Schleifen eigenen sich besonders unter vorgabe, wie of etwas wiederholt werden soll
# for n in range(100):          #Werte von 0-99
#     print(n)
# for n in range(100):
#     print(n+1)                  #Werte von 1-100
# for n in range(1,101):          #Werte von 1-100
#     print(n)
# for n in range(1,101,2):        #Werte von 1-100 in Schrittweite 2
#     print(n)
# for n in range(101,1,-2):       #Werte rückwärts in schrittweite 2
#     print(n)

# # # Der Befehl break
#Funktion geht durch bis sie an die stelle gekommen ist mit entsprechenden Wert
# liste=[12,8,16,24,1,2,3,4,5]
# wert=int(input("Welcher Wert soll gesucht werden?: "))
# for n in liste:
#     if n== wert:
#         print("Die Zahl wurde gefunden")
#         break
#     print(n)
# else:
#     print("die Zahl wurde nicht gefunden")

# # #der continue befehlt lässt die schleife von forne beginnen ohne den rest weiter zu bearbeiten
# liste=[12,8,16,24,0,2,3,4,5]
# wert=int(input("Durch welche werte soll dividiert werden?"))
# for n in liste:
#     if n==0:
#         print("Fehler: Zahlen dürfen nicht durch 0 geteilt werden")
#         continue                
#     print(wert/n)



