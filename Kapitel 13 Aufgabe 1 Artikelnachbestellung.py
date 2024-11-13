#Kapitel 13 Aufgabe 1
"""
Schreiben Sie ein Programm, das es erlaubt, Nachbestellungen für unseren 
Baumarkt zu organisieren. Dieses soll eine Schleife enthalten, in der Sie 
beliebig viele Artikelnummern eintragen können. Sollte vor dem Aufruf des 
Programms bereits eine Liste mit offenen Nachbestellungen bestehen, dann 
sollen die neuen Nummern an die bisherige Datei angehängt werden. Schreiben 
Sie jede Nummer in eine eigen Zeile.
"""

# #Meine Lösung
        
# Eine Nachricht ausgeben, um den Benutzer zu informieren
print('Infolge kannst du Artikelnummern zum Nachbestellen eingeben. Es wird '
      'automatisch geprüft, ob dieser Artikel bereits bestellt wurde '
      '\nWenn du fertig bist, schreibe "fertig" um den Vorgang abzuschließen')

# Öffnen der Datei im Anhangsmodus
f = open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'a')

# Variable zur Steuerung der Schleife
eingabe = True

# Hauptschleife zur Benutzerabfrage
while eingabe:
    # Benutzer zur Eingabe einer Artikelnummer auffordern
    ArtklNr = input('Gebe die zu bestellende Nachbestellung ein und bestätige '
                    'mit der "Enter-Taste": ')

    # Lesen der Datei: Das with-Statement wird verwendet, 
    # um die Datei im Lesemodus zu öffnen und ihren Inhalt zu lesen. 
    # Dies stellt sicher, dass die Datei richtig geschlossen wird.
    with open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'r') as file:
        inhalt = file.readlines()

    # Zeilenweise Überprüfung der Artikelnumme
    #Die Methode strip() entfernt führende und nachfolgende Leerzeichen 
    #(inkl. Tabulatoren und Zeilenumbrüche) von einem String. In deinem Fall, 
    #zeile.strip(), wird jede Zeile aus der Datei bereinigt, um 
    #sicherzustellen, dass du nur den tatsächlichen Text ohne extra Leerzeichen
    #oder Zeilenumbrüche erhältst.
    artikel_bereits_bestellt = False
    for zeile in inhalt:
        if ArtklNr == zeile.strip():
            print("Artikel wurde bereits bestellt")
            artikel_bereits_bestellt = True
            break

    # Artikelnummer in Datei schreiben, wenn sie noch nicht bestellt wurde
    if not artikel_bereits_bestellt:
        f.write(ArtklNr + '\n')

    # Überprüfen, ob der Benutzer den Vorgang abschließen möchte
    if ArtklNr.lower() == "fertig":
        print("Vorgang wird abgeschlossen")
        f.close()
        eingabe = False


# Lösung nach Buch


