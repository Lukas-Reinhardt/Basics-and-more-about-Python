# Kapitel 14 Aufgabe 1
"""
Um Ihre nächste Geburtstagsfeier zu organisieren, möchten Sie eine Gästeliste 
erstellen, die den Vor-und den Nachnamen sowie die Telefonnummer der einzelnen 
Gäste enthält. Da manche dieser Angaben bei einigen Gästen gleich sein können, 
ist es sinnvoll, zusätzlich eine Nummer  zu vergeben, die nur ein einziges Maal 
vergeben werden darf. Nennen Sie diese Spalte ID und definieren Sie sie als 
PRIMARY KEY. Erstellen Sie zunächst eine Datenbank mit einer Tabelle, die diese 
Struktur aufweist.
"""
#Laden der Datenbank SQLite
import sqlite3
from sqlite3 import Error

try:    
    #Verbindung zur Datenbank aufbauen, bzw. erstellung
    db = sqlite3.Connection("K14_Aufgabe_Geburtstagsfeier.db")
    print("Verbindung zur Datenbank Erfolgreich")
    
    #Mit der cursor()-Funktion auf stelle zeigen zur Änderrung an Datenbank
    c = db.cursor()
    befehl = """CREATE TABLE IF NOT EXISTS Geburtstagsfeier(
                ID INTEGER PRIMARY KEY,
                Vorname TEXT,
                Nachname TEXT,
                Telefon INTEGER);"""  
    c.execute(befehl)
except Error as e:
    print(e)
finally:
    db.close()

