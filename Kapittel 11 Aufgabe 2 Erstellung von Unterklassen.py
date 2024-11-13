#Kapittel 11 Aufgabe 2

class Bohrmaschine:
    """
    Erstellt das Objekt Bohrmaschine für einen Baumarkt
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
        gibt die Artikelnummer der Klasse Bohrmaschine zurück
        """
        return self.__Artikelnummer
    def getLeistung(self):
        """
        gibt die Leistung der Klasse Bohrmaschine zurück
        """
        return self.__Leistung
    def getMarke(self):
        """
        gibt die Marke der Klasse Bohrmaschine zurück
        """
        return self.__Marke
    def getPreis(self):
        """
        gibt den Preis der Klasse Bohrmaschine zurück
        """
        return self.__Preis
    
class Akkuschrauber(Bohrmaschine):
    """
    Erstellt Kinderklasse Akkuschrauber von der Klasse Bohrmaschine
    """
    def __init__(self,art,le,ma,pr, sp):
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
        # super().__init__(art, le, ma, pr) # Alternative schreibweise die die Elternklasse aufruft.
        
        # und die zusätliche Variable sp
        self.__Akkuspannung = sp
        
    def getAkkuspannung(self):
        """
        gibt die Akkuspannung der Kindklasse 
        """
        return self.__Akkuspannung
        
class Bohrhammer(Bohrmaschine):
    """
    Erstellt Kinderklasse Bohrhammer von der Klasse Bohrmaschine
    """
    def __init__(self,art,le,ma,pr,Fs,fs):
        """
        Initialisiert ein neues Objekt Akkuschrauber
        
        Argumente
        *Artikelnummer (int): Artikelnummer des Produkts
        *Leistung (int): Leistungsaufnahme in Watt
        *Marke (string): Marke der Bohrmaschine
        *Preis (int): Verkaufspreis
        *Einzalschlagstärke(int): 
        *Einzelschlagfrequenz(int):
        """
        Bohrmaschine.__init__(self, art, le, ma, pr)
        self.__Einschlagstaerke = Fs
        self.__Einschlagfrequenz =fs
    
    def getEinschlagstaerke(self):
        """
        gibt die Einschlagstaerke der Kinderklasse zurück
        """
        return self.__Einschlagstaerke
    def getEinschlagfrequenz(self):
        """
        gibt die Einschlagfrequenz der Kinderklasse zurück
        """
        return self.__Einschlagfrequenz

Akkuschrauber1= Akkuschrauber(10001, 750, "Bosch", 90, 15)
Bohrhammer1= Bohrhammer(101010, 800, "Hilti", 100, 800, 70)


print("Artikelnummer",Akkuschrauber1.getArtikelnummer(),"mit Akkuspannung",Akkuschrauber1.getAkkuspannung())
print("Makre",Bohrhammer1.getMarke(),"Mit Einschlagstaerke",Bohrhammer1.getEinschlagstaerke())
