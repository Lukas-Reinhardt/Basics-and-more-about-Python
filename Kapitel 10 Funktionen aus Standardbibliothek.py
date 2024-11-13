#10 Mit Modulen aus der Standardbibliothek arbeiten

#Build-in-
#https://docs.python.org/3/library/functions.html # übersicht von Build-in-Funktionen
# zudem gibt es Build-in-Konstanten wie True und False
#               Build-in-Typen wie Listen,Tupel und Dictionaries
#
#Module
#https://docs.python.org/3/library/index.html

#Bsp. Modul math - Mathematical function

import math
x=int(input("Eine Zahl zur Logarithmusberechnung eingeben: "))
basis=int(input("Auf welcher Basis? : "))
ergebnis=math.log(x,basis)
print("Der Logarithmus von", x,"zur Basis", basis,"ist", ergebnis,".")
print("Der Logarithmus von %d zur Basis %d ist %f."%(x, basis, ergebnis))   #Dise Methode erlaubt es einen Punkt am ende ohne Lehrzeichen
                                                                            #%s String %d Dubble , %f float