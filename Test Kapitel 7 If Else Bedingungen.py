#Kapitel 7 If-Abfrage
# if Bedingung:
#     Befehl 1
#     Befehl 2
#     Befehl n
# Befehle, die unnabhängig von der Bedingung sind



#Beispiel einfache if else abfrage
# a = int(input("Gebe die Zahl 5 ein: "))
# if a==5:
#     print("Die Eingabe ist richtig")
# else:
#     print("Die Eingabe ist falsch")
    
# a =input('Schreibe das Wort "Hallo": ')
# if a=="Hallo":
#     print("Hallo ist richtig geschrieben")
# else:
#     print("Hallo ist falsch geschrieben")

#Beispiel der Strucktur einer if elif else Strucktur
# if Bedingung1:
#     Ausführung, wenn Bedingung1 zutriff
# elif Bedingung2:
#     Ausfürhung, wenn Bedingung zutrift, die vorherigen Bedingungn jedoch nicht
# elif Bedingung3:
#     Ausführung, wenn Bedingung zutrift, die vorherigen Bedingungen jedoch nicht
# else:
#     Ausführung, wenn keine der Bedingungen zutrifft
#
#Beispiel Wahrenbestand
a=int(input("Gebe den Wahrenbetand ein"))
if a >= 10 and a < 100:
    print("Die Warenbestände liegen bei",a,"Artikel")
elif a>=100:
    print("Warnung: Warenkapazität ausgereizt")
elif a>0:
    print("Nur noch",a,"im bestand")
elif a==0:
    print("Warnung, Artikel nicht mehr verfügbar")
else:
    print("Ungültige eingabe")


# Mögliche Bedingungen    > ist größer
#                         < ist kleiner
#                         >= größer gleich
#                         <= kleiner gleich
#                         != ungleich
# oder mit Booleschen Variablen 
#     a=True
#     if a:
#         print("Der Wert der ariable ist True.")

# oder if not a
# oder if not a==5



#Verknüpfung mehrerer Bedingungen

# #Beispiel if not
# a=int(input("Gebe die Zahl 5 ein: "))
# b=int(input("Gebe die Zahl 10 ein: "))

# if a==5 and b==10:
#     print("Die eingabe ist korrekt")
# if not (a==5 and b==10):               #die klammer, sonst wird nur auf den ersten ausdruck bezogen
#     print("die eingbe ist falsch") 

# #Beispiel or
# if a==5 or b==10:
#     print("Mindestens eine Zahl wurde korrekt eingegeben")
# if not (a==5 or b==10):               
#     print("es wurde zweimal eine falsche Zahl eingegeben") 




