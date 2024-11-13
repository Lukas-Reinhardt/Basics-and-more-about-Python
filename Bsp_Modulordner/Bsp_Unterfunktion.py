#unterfunktion Bsp. Kapitel 9.5

def formel(x):
    if x<50:
        print("x kleienr 50")
        return 2*x**2+4*x+8
    else:
        print("x größer 50")
        return 7*x**2+3*x+3