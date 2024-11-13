#Kapitel 13 Aufgabe 2

"""
Schreiben Sie ein Programm, das es ermöglicht, eine Nummer von der Liste zu
löschen. Dafür soll der Anwender per input-Befehl eine beliebige Artikelnummer
eingeben können. Allerdings kennen wir keine Möglichkeit, um einen Teilbereich
der Liste zu löschen. Daher müssen Sie zunächst die komplette Datei einlesen
und in einer Liste abspeichern. Anschließend müssen Sie die Datei wieder
schließen. Nun können Sie überprüfen, ob die eingegebene Nummer in unserer
Liste enthalten ist und den entsprechenden Eintrag dann innerhalb dieser Liste
löschen.

Dabei müssen Sie beachten, dass die Inhalte der einzelnen Zeilen, die Sie über
den readlines()-Befehl erhalten, bereits über einen Zeilenumbruch verfügen.
Um sie mit der eingegebnene Artikelnummer zu vergleichen, müssen Sie an diese
ebenfalls einen Zeilenumbruch anhängen(+"/n"). Danach müssen Sie die Datei
erneut öffenen. Verwendesn Sie dazu das Attribut "w". Das führt dazu, dass
alle bisherigen Inhalte überschrieben werden. Wenn Sie nun die Inhalte der
überarbeiteten Liste in die Datei schreiben, ist der entsprechende Eintrag
nicht mehr enthalten.
 """
 


f = open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'r')
inhalt = f.readlines()
f.close()

zuentfernen=input("Schreibe die Artikelnummer die gelöscht werden soll: ")

# Erstellt eine neue Liste und fügt nur die Zeilen hinzu,
# die nicht die zu löschende Artikelnummer enthalten
inhaltneu = []
for zeile in inhalt:
    if zuentfernen not in zeile:
        inhaltneu.append(zeile)

with open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'w') as f:
    f.writelines(inhaltneu)
    
    
    
# Buchlösung (Funktioniert nicht. Element wird nicht in lsite gefunden
# und daher auch nicht gelöscht)

# f = open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'r')
# liste = f.readlines()
# f.close()

# geloescht = False
# eingabe = input("Schreibe die Artikelnummer die gelscht werden soll: ")

# for i in range(len(liste)):
#     if liste[i] == eingabe+"/n":
#         liste = liste[:i] + liste[i+1:]
#         f = open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'w')
#         for linie in liste:
#             f.write(linie)
#         print(eingabe,"wurde erfolgreich gelöscht")
#         geloescht = True
#         break
#     if not geloescht:
#         print(eingabe,"ist nicht in der Liste")



# KI lösung anhand Buch (Funktioniert nicht. Element wird nicht in lsite gefunden
# und daher auch nicht gelöscht)


# # Öffnet die Datei und liest die Zeilen
# with open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'r') as f:
#     liste = f.readlines()

# # Setzt den Status für das Löschen auf False
# geloescht = False

# # Fordert die Eingabe der zu löschenden Artikelnummer
# eingabe = input("Schreibe die Artikelnummer die gelöscht werden soll: ") + "\n"

# # Durchläuft die Liste und überprüft jede Zeile
# for i in range(len(liste)):
#     if liste[i] == eingabe:
#         liste = liste[:i] + liste[i+1:]  # Entfernt die gefundene Zeile
#         geloescht = True
#         break

# # Überprüft, ob die Artikelnummer gefunden und gelöscht wurde
# if geloescht:
#     with open('Kapitel13_Aufgabe1_Nachbestellung_Baumarkt.txt', 'w') as f:
#         f.writelines(liste)
#     print(eingabe.strip(), "wurde erfolgreich gelöscht")
# else:
#     print(eingabe.strip(), "ist nicht in der Liste")







        
        




