#Kapitel 9 Aufgabe
while True:
    e1=int(input("Gib die erste Zahl ein: "))
    e2=int(input("Gib die zweite Zahl ein: "))

    import zweierschritte_Uebung
    zweierschritte_Uebung.zweierschritte(e1,e2)
 
    x=input("für Abbruch x Drucken: ")
    if x=="x":
        break