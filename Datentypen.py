# Zahlen (int, float, complex)
integer_num = 10            # Ganzzahl (int)
float_num = 10.5            # Gleitkommazahl (float)
complex_num = 3 + 5j        # Komplexe Zahl (complex)

# Boolescher Datentyp (bool)
bool_true = True
bool_false = False

# Zeichenketten (str)
text = "Hallo Welt"
single_char = 'A'

# Listen (list) - veränderbare, geordnete Sammlung von Elementen
list_example = [1, 2, 3, "Python", [4, 5], True]  # Verschiedene Datentypen sind möglich
list_example[0] = 10       # Listen sind veränderbar (mutable)

# Tupel (tuple) - unveränderbare, geordnete Sammlung von Elementen
tuple_example = (1, 2, 3, "Python", [4, 5], False)
# tuple_example[0] = 10    # Tupel sind nicht veränderbar (immutable) und dieser Code würde einen Fehler verursachen

# Mengen (set) - ungeordnete Sammlung einzigartiger Elemente
set_example = {1, 2, 3, 3, "Python"}  # Duplikate werden entfernt
set_example.add(4)                    # Elemente hinzufügen

# Wörterbücher (dict) - ungeordnete Sammlung von Schlüssel-Wert-Paaren
dict_example = {
    "name": "Lukas",
    "age": 30,
    "skills": ["Python", "Java"]
}
dict_example["age"] = 31  # Wörterbücher sind veränderbar (mutable)

# None - Spezielle Konstante für den Null-Wert
none_example = None

# Byte-Strings (bytes)
byte_example = b"Hallo"

# Typprüfung
print(type(list_example))      # Ausgabe: <class 'list'>
print(type(tuple_example))     # Ausgabe: <class 'tuple'>
print(type(set_example))       # Ausgabe: <class 'set'>
print(type(dict_example))      # Ausgabe: <class 'dict'>
"""
Kurzbeschreibung:

int: Ganze Zahlen.
float: Gleitkommazahlen.
complex: Komplexe Zahlen.
bool: Boolesche Werte (True/False).
str: Zeichenketten.
list: Veränderbare, geordnete Sammlung von Elementen.
tuple: Unveränderbare, geordnete Sammlung von Elementen.
set: Ungeordnete Sammlung einzigartiger Elemente.
dict: Ungeordnete Sammlung von Schlüssel-Wert-Paaren.
None: Repräsentiert das Fehlen eines Wertes.
bytes: Byte-Sequenzen.
"""