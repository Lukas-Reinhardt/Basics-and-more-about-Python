#Erster Fersuch

# a=8
# b=7

# if a==5:
#     print("Der Wert ist 5")
# else:
#     print('Der Wert ist nicht 5 er ist ',a)
#     print('auserdem der wert für b ist',b)

# # Zirkus= "ein Zelt mit Zebras"
# print (Zirkus)


#Kpitel 5.3
# print ("geben Sie bitte eine Zahl ein: ")
# inhalt = input()                             
# inhalt = inhalt *2
# print ( "Doppelter Wert:",inhalt )

# print ("geben Sie bitte eine Zahl ein: ")
# inhalt = eval(input())                              #funktion eval ändert den Datentyp gewünscht um
# inhalt = inhalt *2                                  #Hacker können damit ins Programm jedoch eindringen
# print ( "Doppelter Wert:",inhalt )

# inhalt = eval(input("Gebe bitte eine Zahl ein: "))
# inhalt = inhalt*2
# print ("Doppelter Wert: ",inhalt)

#Kapitel 5.5
# inhalt = input("Gebe eine Zahl ein die Verdoppelt werden soll: ")
# inhalt = float(inhalt)*2                                #So ist es sicherer gegen Hacker
# print ("Doppelter Wert: ",inhalt)                       #Alternativ 
                                                          #int ganzzahl str. für zeichenkette oder 
                                                          #Bool (wahr nicht Wahr) 
#Großbuchstaben mit funktion upper()
# Beispieltext ="Das hier ist gleich groß"
# print (Beispieltext)        
# Beispieltext = Beispieltext.upper()
# print (Beispieltext)

#Datentyp Abfrage
a=3
print ("a entspricht dem Datentyp",type(a))
b=2.1
print ("b are from the Datatype: ",type(b))
c= "Examble a Word"
print ("c are from the Datatype",type(c))
d = True
print ("d are from the Datatype",type(d))