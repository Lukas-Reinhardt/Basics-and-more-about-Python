# Beispielprogramm Methoden
# # Änderrung der anzahl in allen Objekten

class Bohrmaschine:
    """
    Erstellt das Objekt Bohrmaschine für einen Baumarkt.
    """
    anzahl = 0
    
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
        
        Bohrmaschine.anzahl +=1
        
    # def __del__(self):
    #     """
    #     Löscht das Objekt Bohrmaschine.
    #     """
    #     Bohrmaschine.anzahl -=1
    #     print("Bohrmaschine wurde gelöscht")
    #     print("Es sind noch %d Bohrmaschinen verfügbar"%Bohrmaschine.anzahl)
    
    
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
    
    
    # def setPreis(self,preis_neu):
    #     """
    #     Ändert den Preis der Bohrmaschine
    #     """
    #     if abs(self.__Preis - preis_neu) < self.__Preis * 0.1:
    #         self.__Preis = preis_neu
    #     else:
    #         print("Die Abweichung zum vorherigen Preis ist größer 10%")
    #         bestaetigung = input("Soll %.2f als neuer Preis"%preis_neu +"festgelegt werden? (ja/nein)")
    #         if bestaetigung == "ja":
    #             self.__Preis = preis_neu

# # Bsp. wert einer einzelnen Variable ändern
# bohrmaschine1 = Bohrmaschine(10010,850,"Bosch", 59.99)
# wert = float(input("Geben Sie den neuen Preis ein:"))
# bohrmaschine1.setPreis(wert)    
# print("Neuer Preis: ",bohrmaschine1.getPreis())

# # Bsp. die Anzahl aller Objekte ändern
# print (Bohrmaschine.anzahl)
bohrmaschine1 = Bohrmaschine(10010, 850, "Bosch", 59.99)
# print (Bohrmaschine.anzahl, bohrmaschine1.anzahl)
bohrmaschine2 = Bohrmaschine(10014, 1000, "Makita", 54.99)
# print (Bohrmaschine.anzahl, bohrmaschine1.anzahl, bohrmaschine2.anzahl)
bohrmaschine3 = Bohrmaschine(10003,600,"Metabo",39.99)
# print (Bohrmaschine.anzahl,bohrmaschine1.anzahl,bohrmaschine2.anzahl,bohrmaschine3.anzahl)

# del bohrmaschine1
# print(Bohrmaschine.anzahl, bohrmaschine2.anzahl,bohrmaschine3.anzahl)


# Bsp. Unterkategorie
class Akkuschrauber(Bohrmaschine):
    """
    Erstellt das Objekt Akkuschrauber: abgeleitt von der Klasse Bohrmaschine.
    """
    def __init__(self, art, le, ma, pr, sp):
        """
        Initialisiert ein neues Objekt Akkuschrauber
        
        Argumente
        *Artikelnummer (int): Artikelnummer des Produkts
        *Leistung (int): Leistungsaufnahme in Watt
        *Marke (string): Marke der Bohrmaschine
        *Preis (int): Verkaufspreis
        *Akkuspannung(int): Die Akkuspannung des Geräts
        """
        Bohrmaschine.__init__(self, art, le, ma, pr)
        self.__Akkuspannung = sp
        
    def getAukkuspannung(self):
        """
        Gibt die Akkuspannung zurück
        """
        return self.__Akkuspannung

Akkuschrauber1 =Akkuschrauber(10035, 400, "Black", 46.99, 18)
print (Akkuschrauber1.getAukkuspannung()) # neu aus unterkategorie
print(Akkuschrauber1.getMarke())          # aus Unterkategorie mit 
                                          # vererbter information
