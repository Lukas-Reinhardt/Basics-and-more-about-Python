#Kapitel 12 aufgabe 2
"""
Erstellen Sie ein Programm, das den Anwender dazu auffordert, ein Wort mit 
einer geraden Anzahl an Buchstaben einzugeben. Danach soll dasProgramm daraus
zwei Strings erstellen, die jeweils eine Hälfte des Wortes enthalten, und diese
dann ausgeben.

Das Programm soll eine selbst definierte Ausnahme auslösen, wenn die Anzahl
der Buchstaben ungerade ist.
"""


class NoEvenNumberError(Exception):
    def __init__(self,wort):
        self.Wort=wort

try:
    Wort=str(input("gibt ein Wort ein, welches eine Gerade Anzahl an Buchstaben hat: "))
    mitte =int(len(Wort)/2)
    h1=Wort[:mitte]
    h2=Wort[mitte:]

    if mitte%2 == 1:
        raise NoEvenNumberError(Wort)
    print("Erste Hälfte",h1)
    print("Zweite Hälfte",h2)
except NoEvenNumberError as fehler:
    print("das",fehler.Wort,"hat keine gerade anzahl")
    
print("Auf wiedersehen")