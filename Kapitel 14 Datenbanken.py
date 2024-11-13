# Kapitel 14 Datenbanken für eine sichere und effiziente Datenspeicherung verwenden

#14.1 Was ist eine Datenbak
"""
Stell dir vor, eine Datenbank ist wie eine digitale Bibliothek. Sie speichert 
und organisiert große Mengen an Informationen so, dass du sie einfach 
durchsuchen, ändern und verwalten kannst. Jede Informationseinheit in dieser 
"Bibliothek" wird oft in Tabellen mit Zeilen und Spalten organisiert, ähnlich 
wie eine Excel-Tabelle, aber viel leistungsfähiger und flexibler. Datenbanken 
sind das Rückgrat vieler moderner Anwendungen, von Webseiten über Apps bis hin 
zu Unternehmenssoftware. 
"""
# 14.2 Ein passendes Datenbanksystem fuer Python-Programme auswaehlen
"""
Sie
Ein passendes Datenbanksystem (DBMS-Datenbank Management System) 
für python-Programme auswählen
Copilot
Es gibt verschiedene Datenbanksysteme, die gut mit Python zusammenarbeiten. 
Hier sind einige der beliebtesten Optionen:

SQLite: 
Eine leichtgewichtige, eingebettete Datenbank, die keine separate 
Serverinstallation erfordert1
Sie ist ideal für kleinere Anwendungen und Prototypen

MySQL:
Ein weit verbreitetes, relationales Datenbanksystem, das gut mit Python über
Module wie mysql-connector-python integriert werden kann

PostgreSQL:
Ein fortschrittliches, Open-Source-relationales Datenbanksystem, das für seine
Leistungsfähigkeit und Erweiterbarkeit bekannt ist

MongoDB: 
Ein NoSQL-Datenbanksystem, das besonders gut für die Speicherung von
unstrukturierten oder halbstrukturierten Daten geeignet ist

SQLAlchemy:
Ein SQL-Toolkit und ORM (Object-Relational Mapping) für Python, das mit
verschiedenen Datenbanksystemen arbeiten kann

Die Wahl des richtigen Datenbanksystems hängt von den spezifischen
Anforderungen deines Projekts ab. Wenn du zum Beispiel eine einfache,
eingebettete Lösung benötigst, könnte SQLite die beste Wahl sein.
für größere Anwendungen oder Anwendungen mit komplexen Abfragen könnte
PostgreSQL oder MySQL besser geeignet sein.
"""
# Noch mehr Ueber SQLite
"""
Sie
gehe tieffer auf AQLite ein
Copilot
SQLite ist eine leichte, eigenständige SQL-Datenbank-Engine, die in einer 
Vielzahl von Anwendungen und Geräten weltweit verwendet wird1

Hier sind einige wichtige Merkmale von SQLite:

Einfachheit und Leichtigkeit: 
SQLite ist eine kleine, schnelle und zuverlässige Datenbank-Engine, die keine
separate Serverinstallation erfordert.
Sie ist in vielen Anwendungen und Geräten eingebaut, wie z.B. Mobiltelefone, 
Browser und andere Software1

SQL-kompatibel: 
SQLite unterstützt einen Großteil der im SQL-92-Standard festgelegten 
SQL-Befehle, einschließlich Transaktionen, Unterabfragen, Sichten, 
Trigger und benutzerdefinierte Funktionen

Einzeldatei-Struktur: 
Eine SQLite-Datenbank besteht aus einer einzigen Datei, die alle Tabellen, 
Indizes, Ansichten und Trigger enthält
Dies erleichtert den Austausch und die Verwaltung der Datenbank1

Plattformübergreifend: 
SQLite funktioniert auf verschiedenen Betriebssystemen 
wie Windows, macOS, Linux und anderen Unix-ähnlichen Systemen1

Open Source: 
SQLite ist gemeinfrei und kostenlos für jeden Zweck verfügbar
Die Quellcode ist öffentlich zugänglich und wird von einer Gemeinschaft 
von Entwicklern weiterentwickelt

Hier Programmieren wir in Python, es gibt jedoch auch ein Programm, das eine 
grafische Benutzeroberfäche für die Bearbeitung der Datenbanken anbietet. 
Dieses trägt den Namen SQLite Browser.
Die Installation des SQLite Browsers ist jedoch für die Bearbeitung nicht 
zwingend notwendig. Wenn Sie diese Software dennoch installieren möchten, 
finden Sie sie unter folgenden Link:
    https://sqlitebrowser.org/dl/
"""
# 14.3 Eine SQLite-Datenbank erstellen und Tabellen anlegen

"""
Wenn wir eine SQLite-Datenbank in unserem Programm verwenden möchten, mpssen 
wir zunächst die entsprechende Programmbibliothek einbinden. Darüber hinaus 
ist es sinnvoll, das Modul für die Fehlerbehandlung, das für dieses 
Datenbanksystem besteht, ebenfalls zu importieren. Da es beim Öffnen der 
Datenbank hin und wieder zu Fehlern kommen kan, ist es wichtig, die 
enntsprechenden Befehle in ein try-Block zu schreiben. Durch den Import des 
entwprechenden Fehlermoduls kann man im Falle eines Problems eine passende 
Meldung ausgeben.
"""
# import sqlite3
# from sqlite3 import Error
"""
Importiert die Error-Klasse aus dem sqlite3-Modul.

Diese Klasse wird verwendet, um spezifische Datenbankfehler zu handhaben. 
Wenn ein Fehler beim Arbeiten mit der Datenbank auftritt, kannst du diese 
Klasse nutzen, um den Fehler zu fangen und entsprechend darauf zu reagieren.
"""
"""
Um die Verbindung zur Datenbank herzustellen, kommt der connect-Befehl zum 
Einsatz. Da dieser aus dem Modul sqlite3 stammt, müssen wir ihm dessen 
Namen voranstellen. In der Klammer steht der Name der entsprechenden 
Datenbankdatei. Hierbei können wir einen beliebigen Namen auswählen.
Die Endung muss dabei jedoch immer .db lauten. Wenn die entsprechende Datenbank
bereits vorhanden ist, öffnet das Programm sie. Ist dies nicht der Fall, 
erstellt es eine neue Datei mit der gewählten Bezeichnung.
"""
# db = sqlite3.connect("Datenbank_Kapitel14.db")
"""
Wie bereits erwähnt wurde, ist es sinnvoll, diesen Befehl in einem try-Block 
zu setzen. In diesen fügen wir außerdem eine kurze Meldung ein, die anzeigt, 
dass unser Programm die Datenbank erfolgtreich geöffnet hat. Daraufhin müssen 
wir einen except-Block einrichten, der im Falle eines Fehlers eine 
entsprechende Meldung ausgibt. Zum Schluss fügen wir noch einen finally-Block 
hinzu. Darin schließen wir die Datenbank wieder. Das erte Programm sieht dann 
so aus:
"""
# import sqlite3
# from sqlite3 import Error

# try:
#     db = sqlite3.connect("Datenbank_Kapitel14.db")
#     print("Datenbank erfolgreich geöffnet.")
# except Error as e:
#     print(e)
# finally:
#     db.close()
"""
Als nächstes kommt der curser()
Ein Cursor in der Datenbankwelt ist ein Steuerungsstruktur, die es ermöglicht, 
durch die Datensätze in einer Ergebnismenge zu navigieren und diese zu 
manipulieren. Man kann es wie einen Zeiger betrachten, der eine Position in 
einer Menge von Daten hält und auf einzelne Zeilen zeigt, um diese dann zu 
bearbeiten oder zu verarbeiten. 
"""
#c = db.cursor()
"""
Jetzt Befehle an ein Datenbank-Management-System übermitteln. In useren Fall
SQL. Befehle zur erstellung von Tabellen, veränderungen, Daten einfügen oder 
Inhalte abfragen.

Tabelle erzeugen mit CREATE TABLE IF NOT EXIST NamederTabelle
Es wird eine Tabelle erzeugt und wenn diese nicht bereits vorliegt,
wird eine solche angelegt.
"""
# CREATE TABLE IF NOT EXISTS Bohrmaschinen
"""
Danach folgt eine Klammer. In diese fügen wir ein, welche Spalten unsere 
Tabelle enthalten soll. Dafür verwenden wir zunächst eine passende Bezeichnug 
und anschließend den Datentyp. Dabei gild zu beachten, dass SQLite andere 
Datenypen als Python verwendet.
INTEGER ->Ganze Zahlen
TEXT ->Zeichenketten
REAL ->Fließkommazeichen
PRIMARY KEY -> Primärschlüssel wie etwa Artikelnummern und dient deer Zuordnung.
Dieser darf also immer nur einmal vorkommen.
"""
# CREATE TABLE IF NOT EXISTS Bohrmaschinen(
#     Artikelnummer INTEGER PRIMARY KEY,
#     Leistung INTEGER,
#     Marke TEXT,
#     Preis REAL);
"""
Um die Erzeugte Tabelle zu übermittel kommt der Befehl execute() zum einsatz,
den wir auf das Cursor-Objekt anwenden. Es könnte in die klammer von 
execute(der Befehl von gerade stehen. Create TABLE IF...). Da das sehr lang ist,
wird dieses in einer Variable gespeichert.
Bei der Erstellung dieser Variablen ist es sinnvoll, den SQL-Befehl in 
dreifache Anführungszeichen zu setzten. Das erzeugt eine gewöhnliche 
string-Variable. Allerdings bietet diese Alternative im Vergleich zu 
gewöhnlichen Anführungszeichen zwei große Vorteile. Zum einen kann man den 
Inhalt aufdiese Weise auf mehrere Zeilen aufteilen, was zu einem deutlich 
übersichtlicheren Code führt. Zum anderen kann man innerhalb des SQL-Befehls 
problemlos sowohl einfache als auch doppelte Anführungszeichen verwenden, ohne 
dass das zu Konflikten mit dem eigentlichen Python-Programm führt.
"""
# # Bsp.

# import sqlite3
# from sqlite3 import Error
# try:
#     db=sqlite3.connect("Datenbank_Kapitel14.db")
#     print("Datenbank erfolgreich geöffnet.")
#     befehl="""CREATE TABLE IF NOT EXISTS Bohrmaschinen(
#         Artikelnummer INTEGER PRIMARY KEY,
#         Leistung INTEGER,
#         Marke TEXT,
#         Preis REAL);"""
#     c= db.cursor()
#     c.execute(befehl)
# except Error as e:
#     print(e)
# finally:
#     db.close()

"""
Es wird eine Datenbank mit entsprechender Tabelle erstellt. Dieses ist über
dem DB rowser für SQLite ersichtlich. Download des Tools über:
    https://sqlitebrowser.org/dl/
"""
# 14.4 Daten in die Tabellen einfügen

"""
Zum einfügen von Daten in Tabllen wird der INSERT-Befehl verwendet
"""
# INSERT INTO TABELLE (Spalte) VALUES (Wert);
"""
Der Begriff Tabelle steht dabei als Platzhalter. An dieser Stelle muss der Name
der Tabelle genannt werden, in die der neue Wert eingefügt werden soll. Das
gleche trifft auf den BEgriff Spalte zu. Hier steht der Name der Spalte, die
die entsprechende Information aufnehmen soll. Die Spaltennamen haben wir
bereits im vorherigen Abschnitt mit dem Befehl CREATE TABELE festgelegt.
Zum Schluss müssen wir noch den konkreten Wer einfügen, den die Zelle annehmen
soll.
"""
#Bsp. Einfeugen von Werten in eine Tabelle
# INSERT INTO Bohrmaschinen (Artikelnummer,Leistung,Marke,Preis) VALUES (10010,850,"Bosch",59.99);
"""
Auch hier ist es wieder sinnvoll, den SQL-Befehl zunächst in eine Variable zu 
schreiben. 
Um ihn auszuführen muss ein Curser-Objekt vorhanden sein. Da wir in diesem
Beispiel jedoch das bisherige Programm erweitern, gibt es dieses bereits, sodass
wir es nich neu erzeugen müssen. Jetzt können wir den Befehl mit dem Kommando 
execute() ausführen.

Der execute()-Befehl dient eigentlich dazu, eine Änderung an der Datenbank 
vorzunehmen. Wenn wir das Programm ausführen und anschließend die Tabelle im 
SQLite Browser betrachten, stellen wir jedoch fest, dass keine Änderungen zu 
erkennen sind. Das liegt darin begründet, dass SQLite mit sogenannten 
Transaktionen arbeitet. Wenn wir die entsprechenden Befehle eingeben, wird 
automatisch eine neue Transaktion gestartet. Innerhalb des Programms kann man 
dann bereits auf die veränderten Werte zugreifen.
Allerdings handelt es sich dabei um eine Kopie der Werte, die nur für die 
jeweilige Transaktion gültig  ist. Sobald wir die Datenbank schließen oder das 
Programm beendet, gehen diese verloren. Damit die neuen Werte in die Datenbank 
übernommen werden, müssen wir daher abschließend den commit()-Befehl auf unsere 
Datenbankverbindung anwenden. Dieser führt dazu, dass SQLite die Datenbank 
aktualisiert und die Änderungen übernimmt. Das komplette Programm sieht dann so 
aus:
"""
# import sqlite3
# from sqlite3 import Error

# try:
#     db=sqlite3.connect("Datenbank_Kapitel14.db")
#     print("Datenbank erfolgreich geöffnet.")
#     befehl = """CREATE TABLE IF NOT EXISTS Bohrmaschinen(
#                 Artikelnummer INTEGER PRIMARY KEY,
#                 Leistung INTEGER,
#                 Marke TEXT,
#                 Preis REAL);"""
#     c=db.cursor()
#     c.execute(befehl)
#     befehl=""" INSERT INTO Bohrmaschinen (Artikelnummer,Leistung,Marke,Preis)
#                 VALUES(10010,850,"Bosch",59.99);"""
#     c.execute(befehl)
#     db.commit()
# except Error as e:
#     print(e)
# finally:
#     db.close()

"""
In den meisten Programmen ist es notwendig, mehrere Zeilen in eine 
Datenbanktabelle einzufügen. Daher ist es sinnvoll, eine Funktion für diese 
Aufgabe zu erstellen. So kann man diese immer wieder erneut verwenden. Die neuen 
Werte übermitteln wir diese einfach per Übergabewert.

Innerhalb der Funktion wäre es nun selbstverständlich möglich, den SQL-Befehl 
jedes Mal aufs Neue aus den festen BEstandteilen und den Übergabewerten per
string-Konkatenation (mit dem Pluszeichen) zusammenzusetzen. Das wäre jedoch 
recht umständlich. Es gibt noch eine deutlich einfachere Möglichkeit. 
Anstatt feste Werte in den SQL-Befehl einzufügen, verwenden wir einfach ein
Fragezeichen als Platzhalter. Bei der Ausführung des execute-Befehls müssen
wir dann jedocch zwei Argumente übermitteln: zunächst den eigentlichen 
SQL-Befehl mit dem Platzhalter und nachfolgend die gewünschten Werte. Diese 
müssen in eine Klammer stehen und durch ein Komma voneinander getrennt sein. 
Auf diese Weise können wir problemlos mehrere Zeilen in unsere Tabelle einfügen:
"""
# import sqlite3
# from sqlite3 import Error

# def neueZeile(werte):
#     befehl=""" INSERT INTO Bohrmaschinen (Artikelnummer,Leistung,Marke,Preis)
#                 VALUES(?,?,?,?);"""
#     c.execute(befehl, werte)
#     db.commit()
    

# try:
#     db=sqlite3.connect("Datenbank_Kapitel14.db")
#     print("Datenbank erfolgreich geöffnet.")
#     befehl = """CREATE TABLE IF NOT EXISTS Bohrmaschinen(
#                 Artikelnummer INTEGER PRIMARY KEY,
#                 Leistung INTEGER,
#                 Marke TEXT,
#                 Preis REAL);"""
#     c=db.cursor()
#     c.execute(befehl)
#     neueZeile((10010,850,"Bosch",59.99))
#     neueZeile((10014,100,"Makita",54.99))
#     neueZeile((10003,600,"Metabo",39.99))
# except Error as e:
#     print(e)
# finally:
#     db.close()
"""
Zweifache ausführung nicht möglich, da der PRIMARY KEY in der Tabelle bereits
gespeichert ist. PRIMARY KEY darf nur einmal vorhanden sein
"""

#14.5.1 Daten Veraendern
"""
Mittels SQL-Befehl UPDATE
"""
#UPDATE Tabelle SET Spalte = Wert;

#Bsp. dass alle Preise auf 53.99 ändert

# import sqlite3
# from sqlite3 import Error

# try:
#     db=sqlite3.connect("Datenbank_Kapitel14.db")
#     c=db.cursor()
#     befehl="""UPDATE Bohrmaschinen SET Preis=53.99"""
#     c.execute(befehl)
#     db.commit()
# except Error as e:
#     print(e)
# finally:
#     db.close()
"""
Um Werte in ausgewählten Feldern zu ändern kommt die WHERE-Klausel zum Einsatz.
 WHERE Artikelnummer = 10010
"""
# import sqlite3
# from sqlite3 import Error

# try:
#     db=sqlite3.connect("Datenbank_Kapitel14.db")
#     c=db.cursor()
#     befehl="""UPDATE Bohrmaschinen SET Preis=80.99
#     WHERE Artikelnummer = 10010;"""
#     c.execute(befehl)
#     db.commit()
# except Error as e:
#     print(e)
# finally:
#     db.close()
"""
Um Beispielsweise einen neuen Preis für alle Bohrmaschienen von Bosch zu ändern
WHERE Marke = "Bosch"
"""
# 14.5.2 Daten Loeschen

"""
Zum löscchen den Delet-Befehl
DELET FROM Tabelle

Wenn wir den Befehl in dieser Form verwenden, löscht er die gesamte Tabelle. 
Wenn wir jedoch nur einen einzelenen Eintrag entfernen möchten, ist es wichtig, 
wieder eine WHERE-Klausel hinzuzufügen. Dabei müssen wir jedoch beachten, dass 
der DELETE-Befehl keine einzelne Zelle löschen kann. Er entfernt stets die 
gesamte Zeile. Das folgene Programm löschtt aus unserer Tabelle den Eintrag für 
die Bohrmaschine mit der Artikelnummer 10010:
"""
# import sqlite3
# from sqlite3 import Error

# try:
#     db=sqlite3.connect("Datenbank_Kapitel14.db")
#     c=db.cursor()
#     befehl="""DELETE FROM Bohrmaschinen WHERE Artikelnummer = 10010;"""
#     c.execute(befehl)
#     db.commit()
# except Error as e:
#     print(e)
# finally:
#     db.close()
"""
Sowohl beim UPDATE- als auch beim DELETE-Befehl können wir auch wieder 
Fragezeichen als Platzhalter verwenden, um eine allgemeine Funktion zu 
definieren, die die Einträge verändert beziehungsweise löscht. Diese Funktonen 
könnten dann so aussehen:
"""
# def aendern(werte):
#     befehl = """UPDATE Bohrmaschinen SET Preis = ?
#                 WHERE Artikelnummer =?;"""
#     c.execute(befehl, wert)
#     db.commit()
    
# def loeschen (wert):
#     befehl="""DELETE FROM Bohrmaschinen WHERE Artikelnummer = ?;"""
#     c.execute(befehl,wert)
#     db.commit()

# # Aufrufen der Funktonen mit:
#     # aendern((66.49, 10003))
#     #loeschen((10014))


# 14.6 Informationen aus der Datenbank abrufen

"""
Zum Abrufen bestimmter Informationen der SELECT-Befhel.
Dieser erlaubt es uns, geziehlt auf ein einzelnes Feld, auf eine Gruppe von 
Feldern oder auf die gesamte Tabelle zuzugreifen. Im ersten Schritt rufen wir 
den Inhalt einer spezifische Zelle ab. 
"""
# SELECT Spalte FROM NameDerTabelle WHERE Zeile
# SELECT Marke FROM Bohrmaschinen WHERE Artikelnummer = 10014
"""
Um Ergebnisse der Abfragefür das Programm verfügbar zu machen der 
fetchall()-Befehl, den wir auf das Cursor-Objekt anwenden.
Der Inhalt wird per Rückgabewert zurückgegeben, sodass wir diesen einer 
Variablen zuweisen müssen.
"""
# inhalt=c.fetchall()

# Bsp. auslesen eines Bestimmten Inhalts

# import sqlite3
# from sqlite3 import Error

# try:
#     db=sqlite3.connect("Datenbank_Kapitel14.db")
#     befehl="""SELECT Marke FROM Bohrmaschinen WHERE Artikelnummer = 10014;"""
#     c=db.cursor()
#     c.execute(befehl)
#     inhalt=c.fetchall()
#     print (inhalt)
# except Error as e:
#     print(e)
# finally:
#     db.close()
"""
An der Ausgabe erkennt man, dass es sich bei der Variablen inhalt um eine Liste 
handelt, die wiederum ein Tupel enthält. Wenn man mit dem SELECT-Befehl mehrere 
Werte gleichzeitig abruft, enthält die Liste die einzelnen Zeilen. In den Tupeln 
stehen dann die Werte, die in diesen jeweils enthalten sind. Wenn man wie in 
diesem Beispiel nur einen einzelnen Wert abruft, erreicht man diesen ganz 
einfach, indem man an die Variable inhalt zweimal 
die Indexnummer 0 anhängt: inhalt[0][0]

In unserer Datenbanktabelle stehen alle Daten, die zum gleichen Produkt gehören, 
in der gleicen Zeile. Wenn man nicht nur einen einzelnen Wert, sondern alle 
zusammengehörigen Produktdaten abrufen will, ist es daher sinnvoll, die 
komplette Zeile mit dem SELECT-Befehl auszuwählen. Nun könnte man die einzelnen 
Spaltennamen nacheinander durch ein Komma getrennt auflisten. Wenn man jedoch 
die gesamte Zeile erfassen will, ist es deutlich einfacher, hierfür das 
Sternsymbol zu verwenden. Das  bedeutet, dass wir den kompletten Zeileninhalt 
abrufen:
"""
# SELECT * FROM Bohrmaschinen WHERE Artikelnummer = 10014
"""
Manchmal ist es auch notwendig, eine komplette Spalte abzurufen. In diese Fall 
muss man wieder den Spaltennamen einfügen. Nun lassen wir jedoch die 
WHERE-Klausel weg. Wenn man beispielsweise die Preise für alle Geräte abfragen 
will, verwenden wir hierfür diesen Befehel:
"""
# Select Preis From Bohrmaschinen
"""
Abruf der gesammten Tabelle. Dafür Sternsymbol fü die Spalte und WHERE-Klausel 
für die Zeilen weglassen:
"""
# SELECT * FROM Bohrmaschinen

"""
Das folgende Programm ruft die komplette Tabelle ab. Anschließend gibt sie 
diese mit zwei for-Schleifen aus. Für eine bessere Übersichtlichkeit fügen wir 
nach jedem Punkt außerdem eine Leerzeile ein. Um zu zeigen, dass man auf diese 
Weise auch auf ganz konkrete Zellen zugreifen kann, geben wir danach noch einige 
Werte über deren Indexnummern aus:
"""
import sqlite3
from sqlite3 import Error

try:
    db= sqlite3.connect("Datenbank_Kapitel14.db")
    befehl="""SELECT * FROM Bohrmaschinen"""
    c = db.cursor()
    c.execute(befehl)
    inhalt = c.fetchall()
    for zeile in inhalt:
        for wert in zeile:
            print(wert)
        print("\n")
    
    print("Zeile 1, Spalte 1:", inhalt[0][0])
    print("Zeile 3, Spalte 2:", inhalt[2][1])
    print("Zeile 2, Spalte 4:", inhalt[1][3])

except Error as e:
    print(e)
finally:
    db.close()































