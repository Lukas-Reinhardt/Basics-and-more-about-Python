#Kapittel 11 Objektorientierung

#Klassen
# Class Bohrmaschine: 
# in Klassen können Objekte sortiert werden, die an sich wiederholende eigenschaften
# besitzen
# Spezifischen Eigenschaften der Klasse der Bohrmaschinen stehen in der Methode.
# Ein Konstruktor in Python ist eine spezielle Methode, die automatisch aufgerufen wird, 
# wenn eine neue Instanz einer Klasse erstellt wird. In Python wird der 
# Konstruktor mit der Methode __init__ definiert. Um deutlich zu machen, 
# dass es sich hierbei um den Konstruktor handelt, muss 
# als Methodenname stets der Ausdruck __init__ verwendet werden.
# Danach folgt eine Klammer, in der an erster Stelle der Begriff self stehen muss. 
# Wie bei Funktionen üblich, stehen in der Klammer die Werte, die übergeben werden sollen.
# Der Ausdrück self steht dafür, dass dem Konstruktor ein Objekt seiner eigenen Klasse übergeben wird.

# class Bohrmaschine:
# def__init__(self,art,le,ma,pr):
# Die einzelnen Variablen der Klasse, also art,le,ma und pr, werden auch Member genannt

#-----
# # Member definieren
# class Bohrmaschine:
#     def__init__(self,art,le,ma,pr):
#         self.Artikelnummer = art
#         self.Leistung = le
#         self.Marke = ma
#         self.Preis = pr
   
#-----     
# # Es ist üblich einen Docstring einzufügen. Das ist ein Kommentar, der den Zweck
# # der Klasse erklärt. Er wird wie volgt eingefügt: """ Text """
# class Bohrmaschine:
#     """
#     Erstellt das Objekt Bohrmaschine für einen Baumarkt.
#     """
#     def__init__(self,art,le,ma,pr):
#         """
#         Initialisiert ein neues Objekt Bohrmaschine
        
#         Argumente:
#         * Artikelnummer (int): Artikelnummer des Produktes
#         * Leistung (int) : Leistungsaufnahme in Watt
#         * Marke (string): Marke der Bohrmaschine
#         * Preis (float): Verkaufspreis
#         """
        
#         self.Artikelnummer = art
#         self.Leistung = le
#         self.Marke = ma
#         self.Preis =pr

#-----
# # Ein Objekt ist eine Instanz der Klasse
# # Klassen geben die Struktur für ein Onjekt vor.
# # Anhand dieses Bauplans ist es möglich, ein konkretes Objekt zu erzeugen, das
# # einen realen Gegenstant abbildet.
# # Erzeugen eines Objektes

# bohrmaschine1 = Bohrmaschine(10010, 850, "Bosch", 59.99) #Das Objekt ist bohrmaschine1
#                 "----------Klasse----------------------"
# #Beliebig weitere Objekte einer Klasse erzeugen:
# bohrmaschine2 = Bohrmaschine(10014, 1000, "Makita",54.99)
# bohrmaschine3 = Bohrmaschine3(10003, 600, "Metabo",39.99)

#-----
# # Zugriff auf eine Member-Variable eines Objekts
# print(bohrmaschine1.Marke, bohrmaschine2.Marke, bohrmaschine3.Marke)
# print(bohrmaschine1.Preis, bohrmaschine2.Preis, bohrmaschine3.Preis)

#----
# # Änderung eines Members eines Objektes
# bohrmaschine1.Marke = "Neue Marke"

#-----
# # Kapselung der Daten
# # Das bedeutet, Zugriff auf Werte innerhalb einer Klasse nicht immer zu ermöglichen
# # zum Schutz der Daten
# # Änderrungen danach nur innerhalb der Klasse möglich. Nicht von Hauptprogramm oder
# # Anderen Klassen mehr.
# # Kapselung durch zwei Unterstriche vor dem Variablennamen
# self.__Artikelnummer = art
# self.__Leistung = le
# self.__Marke = ma
# self.__Preis = pr

# # Kapselung betrifft auch Leser
# # print (bohrmaschind1.__Artikelnummer) gibt fehlermeldung aus

#-----
# # Methoden: Funktionen für Objekte
# # Um zu bestimmen auf welche Member zugriff gewährleistet wird, nach zuvorriger
# # Kapselung. 
# # Man kann einstellen, dass etwas gelesen werden kann aber nicht ändern.
# # Methoden lassen sich ausschließlich auf Objekte anwenden weil sie
# # inerhalb einer Klasse stehen. Somit wird erziehlt das die Methode zugriff auf die
# # Member der Objekte hat.

# # Erstellen von Methoden

# # get-Methode zum Auslesen
# def getArtikelnummer(self):
#     """
#     Gibt die Artikelnummer der Bohrmaschine zurück.
#     """
#     return self.__Artikelnummer
# # Der Begriff "getArtikelnummer" ist frei auswählbar, wobei get für die abfrage
# # eines inhaltes eine übliche benennung dastellt

# # set-Methode zum ändern eines Inhaltes
# def setPreis(self,preis_neu):
#     """
#     Ändert den Preis der Bohrmaschine
#     """
#     self.__Preis = preis_neu
# # Die anderen Member sind dabei unangetastet und weiterhin gekapselt

# # Komplexes Beispiel. Nur Preisänderungen zulassen von 10%
# # Komplette lösung in Datei Kapittel 11 Objektorientierung
# def setPreis(self,preis_neu):
#     """
#     Ändert den Preis der Bohrmaschine
#     """
#     if abs(self.__Preis - preis_neu) < self.__Preis*0.1:
#         self.__Preis = preis_neu
#     else:
#         print("Die Abweichung zum vorherigen Preis ist sehr groß.")
#         bestaetigung= input("Soll %d als neuer Preis"%preis_neu+"festgelegt werden?(ja/nein)")
#         if bestaetigung == "ja":
#             self.__Preis = preis_neu
            
#-----
# Klassen- und Objektvariablen
# # Klassenvariable hinzugefügten, die die Anzahl an Bohrmaschinen 
# # in allen Objekten ändert mit z.b Bohrmaschine.anzahl +=1  .
# # Also Bezeichnung der Klasse, gefolgt von einem Punkt und dem Namen der Variablen
# # Es wird beim Erzeugen eines objektes wir ein Wert im Konstrukor geändert mit 
# # dem bsp. Bohrmaschine.anzahl +=1


 # class Bohrmaschine:
 #     """
 #     Erstellt das Objekt Bohrmaschine für einen Baumarkt.
 #     """
 #     def __init__(self,art,le,ma,pr):
 #         """
 #         Initialisiert ein neues Objekt Bohrmaschine
     
 #         Argumente:
 #             *Artikelnummer (int): Artikelnummer des Produkts
 #             *Leistung (int): Leistungsaufnahme in Watt
 #             *Marke (string): Marke der Bohrmaschine
 #             *Preis (float): Cerkaufspreis
 #         """
 #         self.__Artikelnummer = art
 #         self.__Leistung = le
 #         self.__Marke = ma
 #         self.__Preis = pr
         
 #         Bohrmaschine.anzahl +=1        #Erzeugt die Variable anzahl in der 
 #                                        #Klasse Bohrmaschine und erhöht diese 
 #                                        #um 1 beim anlegen
 #        def __del__(self):
 #            """Löscht das Objekt Bohrmaschine.
 #            """
 #            Bohrmaschine.anzahl -=1     # In der __del__ Funktion/Methode wird die anzahl
 #                                        # reduziert, bezw. eine Objekt Bohrmaschine gelöscht
 #            print("Bohrmaschine wurde gelöscht")
 #            print("Es sind noch %d Bohrmaschinen verfügbar"%Bohrmaschine.anzahl)
          
# # --------------->>>>>>Vollständiges beispiel unter Datei Bsp. Methoden Kapitel 11.6

#-----
# # 11.7 Vererbung: ein grundlegendes Prinzip der objektorientierten Programmierung
# Es geht dabei darum unterkategorien zu erstellen. Übergruppe ist Bohrmaschine und die
# unterkategorie sind sowas wie Akkuschrauber, Borhammer...
# Grundlegende eingenschaften einer Bohrmaschine treffen auf Akkuschrauber, als auch
# auf einen Borhammer zu. Jedoch muss zur Unterscheidung eine Unterkategorie
# bestimmte eigenschaften ergenst werden. 
# Es werden informationen der übergeordneten Kategorie "Vererbt" auf die 
# unterkategorie
# Für die Vererbung ist es notzwendig, stets mit der übergeordneten Klasse 
# zu beginnen. 
            
# Übergeordnete Klasse Bohrmaschine
 # class Bohrmaschine:
 #     """
 #     Erstellt das Objekt Bohrmaschine für einen Baumarkt.
 #     """
 #     def __init__(self,art,le,ma,pr):
 #         """
 #         Initialisiert ein neues Objekt Bohrmaschine
     
 #         Argumente:
 #             *Artikelnummer (int): Artikelnummer des Produkts
 #             *Leistung (int): Leistungsaufnahme in Watt
 #             *Marke (string): Marke der Bohrmaschine
 #             *Preis (float): Cerkaufspreis
 #         """
 #         self.__Artikelnummer = art
 #         self.__Leistung = le
 #         self.__Marke = ma
 #         self.__Preis = pr
         
 
# # Erzeugung einer Untergeordnete Klasse
# class Akkuschrauber(Bohrmaschine):
    
# # Alsnächstes der Aufruf des Konstruktors. 
# # Dieser erhält die 4 bekannten Werte der Bohrmaschine und entsprechend 
# # zusätzliche der Untergeordneten Klasse sp für Spannung mit der 
# # der Akkuschrauber Arbeitet.

#     def__init__(self, art, le, ma, pr, sp)
# # Im Konstruktor wird zunächst ein Objekt der Klasse Bohrmaschine erzeugt.
# # Dieser stellt einen festen Bestandteil eines jedeno Objekts der Unterklasse dar.
# # Dafür ist es notwendig, den Konstruktor der übergeordneten Klasse aufzurufen 
# # und ihm die entsprechenden Werte zu übergeben:
#     Bohrmaschine.__init__(self. art, le, ma, pr)
    
#     self.__Akkuspannung = sp
    
## Nochmal zusammen die Klasse Akkuschrauber
class Akkuschrauber(Bohrmaschine):
    """
    Erstellt das Objekt Akkuschrauber: abgeleitt von der Klasse Bohrmaschine.
    """
    def__init__(self, art, le, ma, pr, sp):
        """
        Initialisiert ein neues Objekt Akkuschrauber
        
        Argumente
        *Artikelnummer (int): Artikelnummer des Produkts
        *Leistung (int): Leistungsaufnahme in Watt
        *Marke (string): Marke der Bohrmaschine
        *Preis (int): Verkaufspreis
        *Akkuspannung(int): Die Akkuspannung des Geräts
        """
        Bohrmaschine.__init(self, art, le, ma, pr)
        self.__Akkuspannung = sp
        
    def getAukkuspannung(self):
        """
        Gibt die Akkuspannung zurück
        """
        return self.__Akkuspannung









        
        
