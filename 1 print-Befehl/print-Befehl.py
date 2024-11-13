# Python-Code zur Erklärung der print()-Funktion

# 1. Grundlegende Verwendung
print("Hallo, Welt!")  # Gibt den Text "Hallo, Welt!" in die Konsole aus.

# 2. Ausgabe von mehreren Werten
name = "Lukas"
alter = 30
print("Name:", name, "Alter:", alter)  # Die Werte werden mit einem Leerzeichen getrennt.

# 3. Verwendung des 'sep'-Parameters
# Der 'sep'-Parameter legt das Trennzeichen zwischen den Argumenten fest.
print("Apfel", "Banane", "Orange", sep=", ")  # Ausgabe: Apfel, Banane, Orange

# 4. Verwendung des 'end'-Parameters
# Der 'end'-Parameter legt fest, was am Ende der Ausgabe erscheint (Standard ist '\n' für Zeilenumbruch).
print("Erste Zeile", end=" | ")
print("Zweite Zeile")  # Ausgabe: Erste Zeile | Zweite Zeile

# 5. Formatierte Ausgabe mit f-Strings (ab Python 3.6)
# F-Strings erlauben das direkte Einfügen von Variablen in einen String.
vorname = "Lukas"
nachname = "Reinhardt"
print(f"Hallo, {vorname} {nachname}!")  # Ausgabe: Hallo, Lukas Reinhardt!

# 6. Formatierte Ausgabe mit der format()-Methode
# Die format()-Methode erlaubt Platzhalter im String.
print("Das Alter von {} ist {} Jahre.".format(vorname, alter))

# 7. Escape-Sequenzen
# Escape-Sequenzen werden verwendet, um Sonderzeichen auszugeben.
print("Dies ist ein Tabulator:\tund dies ist ein Zeilenumbruch:\nNeue Zeile")
print("Doppelte Anführungszeichen: \"Zitat\" und Backslash: \\")

# 8. Mehrzeilige Strings
# Mit dreifachen Anführungszeichen kann ein mehrzeiliger Text ausgegeben werden.
print("""
Dies ist ein mehrzeiliger String.
Er kann mehrere Zeilen enthalten.
""")

# 9. Ausgeben von Variablenwerten mit repr() und str()
# repr() zeigt den "unveränderten" Wert der Variable an (für Debugging nützlich).
pi = 3.14159
print("Pi als String:", str(pi))  # Ausgabe: Pi als String: 3.14159
print("Pi als repr:", repr(pi))   # Ausgabe: Pi als repr: 3.14159

# 10. Beispiel für die Verwendung der flush-Option
# Normalerweise puffert die print()-Funktion die Ausgabe. Mit flush=True wird 
# die Ausgabe sofort angezeigt.
import time

print("Lade", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(1)
print("\nFertig!")

# 11. Benutzen von 'file' für die Ausgabe
# Standardmäßig gibt print() die Ausgabe auf der Konsole aus. Mit dem 
# 'file'-Parameter kann man die Ausgabe in eine Datei schreiben.
with open("output.txt", "w") as file:
    print("Diese Ausgabe wird in die Datei geschrieben.", file=file)

# 12. Hinweis: Debugging-Tipp
# Man kann print() verwenden, um Variablen und deren Werte während der Programmausführung anzuzeigen.
# Beispiel:
x = 42
y = "Test"
print(f"Debugging: x={x}, y={y}")  # Ausgabe: Debugging: x=42, y=Test
