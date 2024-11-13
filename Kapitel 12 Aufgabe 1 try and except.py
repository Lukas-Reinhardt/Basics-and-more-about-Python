# Kapitel 12 Aufgabe 1
"""
Schreiben Sie ein Programm, das zwei Zahlen vom Benutzer abfragt und 
anschließend die erste Zahl durch die weite teilt. Das Programm soll zwei 
Ausnahmen enthalten: eine für den Fall, dass der Anwender als zweite Zahl 0 
eingibt, und die andere, wenn er anstatt einer ganzen Zahl eine anderen Datyp 
eingibt.

Abschließend sollen alle weiteren Ausnahmen abgefangen und dabei die Art 
des Fehler ausgegeben werden.
"""
import sys
print("Gib in folgenden zwei Zahlen ein die miteinander difidiert werden")

try:
    z1=int(input("Erste Zahl für Zähler: "))
    z2=int(input("Zweite Zahl für Nenner: "))
    print("Das Ergebnis ist",z1/z2)
except ZeroDivisionError:
    print("Es darf nicht durch Null geteilt werden")
except ValueError:
    print("Es durfen nur Ganze Zahlen eigegeben werden")
except:
    print("Folgender Fehler ist aufgetreten:",sys.exc_info()[0])
else:
    print("Berechnung war erfolgreich")

