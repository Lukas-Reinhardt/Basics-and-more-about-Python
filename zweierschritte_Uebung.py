# Funktion zu Aufgabe 1 in Kapitel 9

def zweierschritte (a,b):
    if a<b:
        for n in range (a,b+1,2):
            print(n)
    else:
        for n in range (a,b-1,-2):
            print(n)
            

