#Kapitel 11 Aufgabe 1

class Wohnung:
    """
    Erstellt die Klasse Wohnung
    """
    def __init__(self,Na,Ort,Anz_Bett,Pr):
        """
        Initialisierung 
        *Name der Wohnung: Na = Name
        *Standort der Wohnung: Ort = Standort
        *Anzahl an Betten: Anz_Bett = Betten
        *Preis der Betten: Pr = Preis
        """
        self.__Name = Na
        self.__Standort = Ort
        self.__Betten = Anz_Bett
        self.__Preis = Pr
    
    def getName(self):
        """
        Gibt den Namen der Wohnungen zurück
        """
        return self.__Name
    def getStandort(self):
        """
        Gibt den Standort zurück
        """
        return self.__Standort
    def getBetten(self):
        """
        Gibt die Anzahl Betten der Wohnung zurück
        """
        return self.__Betten
    def getPreis(self):
        """
        Gibt den Preis zurück
        """
        return self.__Preis
    
    
    
    def SetPreis(self,preis_neu):
        """
        Ermöglicht änderrungen am Preis
        """
        self.__Preis=preis_neu

    def SetAnz_Bett(self,Anz_Bett_neu):
        """
        Ermöglicht Änderrung der Bettenzahl
        """
        self.__Betten= Anz_Bett_neu
        
        
        
Wohnung1=Wohnung("Angela", "Früch", 3, 40.55)
Wohnung2=Wohnung("Helga", "Rubenheim", 7, 1000)

print("Wohnung1:", Wohnung1.getName(), Wohnung1.getStandort(), Wohnung1.getPreis(), Wohnung1.getBetten())
print("Standort", Wohnung2.getStandort())       
    

Preisabfrage = input("Soll der Preis von Wohnung1 Angela angepasst werden? (ja/nein): ")
if Preisabfrage == "ja":
    preis_neu = float(input("Gebe den neuen Preis ein: "))  
    Wohnung1.SetPreis(preis_neu)
    print("Neuer Preis: ",Wohnung1.getPreis())