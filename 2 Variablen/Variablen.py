# Python-Code zur Erklärung von Variablen

# 1. Was sind Variablen?
# Variablen sind Namen, die verwendet werden, um Daten zu speichern.
# Sie bestehen aus einem Namen, einem Zuweisungsoperator (=) und einem Wert.

# Beispiel:
name = "Lukas"
alter = 30
pi = 3.14159
print(name, alter, pi)

# 2. Regeln für Variablennamen
# - Variablennamen dürfen mit Buchstaben (a-z, A-Z) oder einem Unterstrich (_) beginnen.
# - Sie dürfen keine Sonderzeichen (z.B. @, $, %) enthalten.
# - Groß- und Kleinschreibung wird unterschieden (name ≠ Name).
# - Variablennamen dürfen keine reservierten Schlüsselwörter (wie if, for, while) sein.

# Beispiel:
mein_name = "Lukas"   # gültiger Variablenname
_MEINE_VARIABLE = 100  # gültig
# 3name = 5  # ungültig, da der Name mit einer Zahl beginnt

# 3. Datentypen von Variablen
# Python erkennt den Typ einer Variablen automatisch basierend auf dem zugewiesenen Wert.
ganzzahl = 10          # Integer (int)
kommazahl = 3.14       # Float (Dezimalzahl)
text = "Hallo"         # String (str)
boolean = True         # Boolean (bool)

print(ganzzahl, kommazahl, text, boolean)

# Mit der Funktion `type()` kannst du den Datentyp einer Variable anzeigen:
print("Typ von 'ganzzahl':", type(ganzzahl))
print("Typ von 'kommazahl':", type(kommazahl))
print("Typ von 'text':", type(text))
print("Typ von 'boolean':", type(boolean))

# 4. Mehrere Variablen gleichzeitig zuweisen
x, y, z = 1, 2, 3
print(x, y, z)

# Mehrere Variablen auf denselben Wert setzen:
a = b = c = 0
print(a, b, c)

# 5. Variablenwerte ändern
# Variablen sind veränderbar. Du kannst ihnen neue Werte zuweisen.
zahl = 10
print("Vorher:", zahl)
zahl = 20
print("Nachher:", zahl)

# 6. Dynamische Typisierung
# In Python können Variablen ihren Typ ändern, je nachdem, welcher Wert zugewiesen wird.
variable = 5
print("Typ von 'variable':", type(variable))  # int
variable = "Text"
print("Typ von 'variable':", type(variable))  # str

# 7. Typumwandlung (Type Casting)
# Manchmal musst du den Typ einer Variable explizit ändern.
zahl_str = "123"
zahl_int = int(zahl_str)  # String wird in Integer umgewandelt
print("Typ von 'zahl_str':", type(zahl_str))
print("Typ von 'zahl_int':", type(zahl_int))

# Weitere Beispiele für Typumwandlung:
float_zahl = float("3.14")
str_zahl = str(42)
print("Float-Zahl:", float_zahl, "Typ:", type(float_zahl))
print("String-Zahl:", str_zahl, "Typ:", type(str_zahl))

# 8. Konstanten
# In Python gibt es keine echten Konstanten (unveränderliche Variablen), aber es ist üblich, Konstanten in Großbuchstaben zu schreiben.
PI = 3.14159
GRAVITY = 9.81
print("Konstanten:", PI, GRAVITY)

# Hinweis: Obwohl wir diese Variablen als Konstanten betrachten, können sie trotzdem verändert werden.

# 9. Beispiel für eine Zählvariable in einer Schleife
# Zählvariablen werden oft in Schleifen verwendet.
for i in range(5):
    print("Zählvariable i:", i)

# 10. Debugging-Tipp
# Wenn du dir unsicher bist, welchen Wert oder Typ eine Variable hat, kannst du print() verwenden.
debug_variable = 123
print(f"Debugging: debug_variable={debug_variable}, Typ={type(debug_variable)}")

# 11. Variablen löschen
# Du kannst eine Variable mit `del` löschen.
variable = "Hallo"
print(variable)
del variable
# print(variable)  # Fehler, da die Variable gelöscht wurde

# 12. die eval Funkion
# Ermöglicht das einfache ändern der Datentypen gewünscht um. 
# Es heißt, Hacker können damit ins Programm eindringen, daher dieses hier besser
# nicht nutzen.

# inhalt = eval(input("Gebe bitte eine Zahl ein: "))
# inhalt = inhalt*2
# print ("Doppelter Wert: ",inhalt)