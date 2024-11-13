#Kapitel 14 Aufgabe 4
"""Erstellen Sie zum Abschluss ein Programm, das die komplette Gästeliste 
ausgibt
"""

#Aus Aufgabe 1
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

#Aus Aufgabe 2
        
import sqlite3
from sqlite3 import Error

abfrage = False
neuerGast = input('Soll ein neuer Gast hinzugefügt werden? Schreibe "ja": ').lower()
if neuerGast == "ja":
    abfrage = True

if abfrage:
    try:
        db = sqlite3.connect("K14_Aufgabe_Geburtstagsfeier.db")
        c = db.cursor()
        Vor = input("Vorname Gast: ")
        Nach = input("Nachname Gast: ")
        Tel = input("TelefonNr. Gast: ")
        befehl = """INSERT INTO Geburtstagsfeier (Vorname, Nachname, Telefon)
                    VALUES (?, ?, ?)"""
        c.execute(befehl, (Vor, Nach, Tel))
        db.commit()  # Nicht vergessen, die Änderungen zu speichern
        print(f"{Vor} {Nach} wurde erfolgreich hinzugefügt.")
    except Error as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        db.close()
        
# Aus Aufgabe 3

abfrage = False
gastloeschen = input('Soll ein Gast aus der Tabelle gestrichen werden, ja?').lower()
if gastloeschen == "ja":
    abfrage = True
    
if abfrage:
    try:
        db = sqlite3.connect("K14_Aufgabe_Geburtstagsfeier.db")
        c = db.cursor()
        print("Wer soll den aus der Tabelle gestrichen werden?")
        Vor = input("Vorname: ")
        Nach = input("Nachname: ")
        befehl = """DELETE FROM Geburtstagsfeier WHERE Vorname = ? AND Nachname = ?;"""
        c.execute(befehl,(Vor,Nach))
        db.commit()
        print(f"{Vor}{Nach} wurde erfolgreich gelöscht")
    except Error as e:
        print(e)
    finally:
        db.close()

#------Aufgabe 4------
try:
    db = sqlite3.connect("K14_Aufgabe_Geburtstagsfeier.db")
    c = db.cursor()
    befehl = """SELECT * FROM Geburtstagsfeier"""
    c.execute(befehl)
    inhalt= c.fetchall()
    for zeile in inhalt:
        print(zeile)    
except Error as e:
    print(e)
finally:
    db.close()








































