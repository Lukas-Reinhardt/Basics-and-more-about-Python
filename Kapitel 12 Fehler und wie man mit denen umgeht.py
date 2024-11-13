# Kapitel 12 Fehler

# 12.1 Warum ist es wichtig, Fehler und Ausnahmen zu behandeln

# Tritt im Programm ein Fehler auf, etwa dadurch, dass der Anwender versucht
# durch Null zu teilen (4/0), kommt es zu einer Fehlermeldung. Solche Fehler
# führen zu einem Abbruch des Programmes. Um ein Programm Robust zu gestalten
# ist es daher sinnig bei solchen Fehlern eine erneute Abfrage einzubindne,
# oder an anderer Stelle das Programm vortzusetzen. 

# 12.2 try und exept: So werden Ausnahmen behandelt

# Block try: stehen alle abschnitte die eventuell zu Problemen führen
# Block except: Hier werden die Fehler abgefangen. Die rede ist von Ausnahmen.
# Aufbau except Blockt: except art  der Ausnahme :
# ---
# #Bsp. in dem trotz fehler kein Abbruch des Programmes folgt
# try:
#     x = int(input("Wert: "))
#     print("Ergebnis:", 4/x)
# except ZeroDivisionError:
#     print ("Es ist nicht möglich, einen Wert durch 0 zu teilen")
    
# print("Auf Wiedersehen!")
    
# Die Bezeichnungen der Ausnahmen wie ZeroDivisionError werden vom Kompiler
# bei einem Fehler angezeigt.
#---
# # Bsp. für mehrere Ausnahmen 
# try:
#     x = int(input("Wert: "))
#     print("Ergebnis:", 4/x)
# except (ZeroDivisionError, ValueError):
#     print ("Es ist ein Fehler aufgetreten")
    
# print("Auf Wiedersehen!")

# Damit ein User über seinen Fehler bescheid weis, ist es sinnig die Fehler,
# also je Art der Ausnahme ein except zu erstellen.
#---
# # Bsp. für mehrere Ausnahmen in aufgeteileten except
# try:
#     x = int(input("Wert: "))
#     print("Ergebnis:", 4/x)
# except ZeroDivisionError:
#     print ("Durch Null teilen ist nicht möglich")
# except ValueError: 
#     print("Bitte nur durch ganze zahlen Teilen")
# print("Auf Wiedersehen!")
#---
# # Bsp. für alle Arten von Ausnahmen
# try:
#     x = int(input("Wert: "))
#     print("Ergebnis:", 4/x)
# except:
#     print ("Fehlermeldung")

# print("Auf Wiedersehen!")
#--- 
# # Bsp.Fehlermeldung für User mittels import sys
# import sys
# try:
#     x = int(input("Wert: "))
#     print("Ergebnis:", 4/x)
# except:
#     print("Folgender Fehler ist aufgetreten:",sys.exc_info()[0])
# print("Auf Wiedersehen!")
#---
# # Bsp. mit einer einer Erfolgsmitteilung
# # Bsp.Fehlermeldung für User mittels import sys
# import sys
# try:
#     x = int(input("Wert: "))
#     print("Ergebnis:", 4/x)
# except:
#     print("Folgender Fehler ist aufgetreten:",sys.exc_info()[0])
# else:
#     print("Des Ergebnis wurde erfolgreich berechnet")
# print("Auf Wiedersehen!")

# 12.3 finally: die Ausnahmebehandlung abschließen
# der finally Block wird in jeden Fall ausgeführt. Ob eine Ausnahme zutrifft oder nicht
# Er kommt bei Aufräumarbeiten in Einsatz etwa beim löschen von Objekten,
# zur freigabe von Speicher, ein Programm zu schließen.

# #Bsp.
# class Obj:
#     wert = 4
# try:
#     objekt = Obj()
#     x = int(input("Wert: "))
#     print("Ergebnis:",Obj.wert/x)
# except ZeroDivisionError:
#     print("Teilen durch Null nicht möglich")
# else:
#     print("Das Ergebnis wurde erfolgreich berechnet")
# finally:
#     del objekt
#     print("objekt zerstört")
# print("Auf Wiedersehen")

# 12.4 Selbst definierte Ausnahmen festlegen
# Ausnahmen sind in Klassen definiert. Daher werden eigene Ausnahem ebenfalls
# in Klassen definiert. diese werden innerhabl einer if abfrage mittels 
# Schlüsselbegrif raise ausgelöst.
# # Bsp. Programm in dem nur Zahlen zwischen 10 und 20 zulässig sind
# class OutOfRangeError(Exception):
#     def __init__(self,wert):
#         self.Wert=wert
# try:
#     x=int(input("Gib eine Zahl zwischen 10 und 20 ein: "))
#     if x>20 or x<10:
#         raise OutOfRangeError(x)
#     print("Ergebnis",4/x)
# except OutOfRangeError as fehler:
#     print("Die Zahl",fehler.Wert,"liegt nicht zwischen 10 und 20")
    
# print("Auf wiedersehen")
#---
# #Bsp. aus eigenen Ausnahmen gemsicht mit Standard-Ausnahmen

# class OutOfRangeError(Exception):
#     def __init__(self,wert):
#         self.Wert=wert
# try:
#     x=int(input("Gib eine Zahl zwischen 10 und 20 ein: "))
#     if x>20 or x<10:
#         raise OutOfRangeError(x)
#     print("Ergebnis",4/x)
# except OutOfRangeError as fehler:
#     print("Die Zahl",fehler.Wert,"liegt nicht zwischen 10 und 20")
# except ValueError:
#     print("Nur ganze Zahlen")
# print("Auf wiedersehen")















