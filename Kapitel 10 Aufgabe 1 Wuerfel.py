#Kapitel 10 Aufgabe 1 und 2
from wuerfel import Wuerfel
from datetime import datetime


# Aktuelles Datum und Uhrzeit
now = datetime.now()

# Formatieren des Datums und der Uhrzeit
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Datum und Uhrzeit:", dt_string)

#Wuerfeln
x="ja"
while True:    
    if x=="ja":
        Wuerfel()
        x=input('Weiter Würfeln mit "ja": ')
    else:
        break
