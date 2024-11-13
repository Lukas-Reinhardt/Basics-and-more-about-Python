# Beispielprogramm Methoden

class Bohrmaschine:
    """
    Erstellt das Objekt Bohrmaschine für einen Baumarkt.
    """
    def __init__(self,art,le,ma,pr):
        """
        Initialisiert ein neues Objekt Bohrmaschine
    
        Argumente:
            *Artikelnummer (int): Artikelnummer des Produkts
            *Leistung (int): Leistungsaufnahme in Watt
            *Marke (string): Marke der Bohrmaschine
            *Preis (float): Cerkaufspreis
        """
        self.__Artikelnummer = art
        self.__Leistung = le
        self.__Marke = ma
        self.__Preis = pr
        
    def getArtikelnummer(self):
        """
        Gibt die Artikelnummer der Bohrmaschine zurück.
        """
        return self.__Artikelnummer
    
    def getLeistung(self):
        """
        Gibt die Leistung der Bohrmaschine zurück.
        """
        return self.__Leistung
    
    def getMarke(self):
        """
        Gibt die Marke der Bohrmaschine zurück.
        """
        return self.__Marke
    
    def getPreis(self):
        """
        Gibt den Preis der Bohrmaschine zurück
        """
        return self.__Preis
    
    
    def setPreis(self,preis_neu):
        """
        Ändert den Preis der Bohrmaschine
        """
        if abs(self.__Preis - preis_neu) < self.__Preis * 0.1:
            self.__Preis = preis_neu
        else:
            print("Die Abweichung zum vorherigen Preis ist größer 10%")
            bestaetigung = input("Soll %.2f als neuer Preis"%preis_neu +"festgelegt werden? (ja/nein)")
            if bestaetigung == "ja":
                self.__Preis = preis_neu
    
bohrmaschine1 = Bohrmaschine(10010,850,"Bosch", 59.99)
wert = float(input("Geben Sie den neuen Preis ein:"))
bohrmaschine1.setPreis(wert)
    
print("Neuer Preis: ",bohrmaschine1.getPreis())