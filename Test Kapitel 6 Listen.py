#Test zu Kapittel 6

artikel_Nr =10010
leistung = 850
marke = "Bosch"
preis =59.99

Borhmaschine1 =[10010, 850, "Bosch", 59.99] #Als Liste
Borhmaschine1[0]                            #Um auf elemente zuzugreifen
Borhmaschine1[-2]
Borhmaschine1[0:2]
Borhmaschine1[:3]
Borhmaschine1[2:]
Borhmaschine1[:]

Borhmaschine2= [10014, 1000, "Makita", 54.99]
Borhmaschine1+Borhmaschine2         #Listen werden Hintereinander gelegt
Borhmaschine1*3                     #Liste wird 3* Hintereinander verdoppelt
neueListe = Borhmaschine1[1:3]      #Ellemente von 1:3 in neuer Liste gespeichert
neueListe = neueListe + [900]       #Liste wird um einen Wert erweitert

Borhmaschine3= [10003, 600, "Metabo", 39,99]
listeBorhmaschinen=[Borhmaschine1, Borhmaschine2, Borhmaschine3]
listeBorhmaschinen[0][0]            #Aus Bormaschine 1 der Erste Listeneitrag

#6.2 Dictionaries: Zugriff über einen Schlüsselbegriff
Borhmaschine1= {"artikelnummer": 10010,"leistung":850,"marke":"Bosch","preis":59.99}
Borhmaschine1["marke"]              #Gibt die Marke der Bormaschine aus
Borhmaschine1["drehzahl"]=900       #Erweitert die Liste um drehzahl
del Borhmaschine1["leistung"]       #Löscht den Eintrag Leistung aus der liste, Liste wird kleiner
list(Borhmaschine1.keys())          #Gibt Liste der Schlagwörter aus
sorted(Borhmaschine1.keys())        #sortiert die Liste Alphabetisch

#Alternative eingabemöglichkeit Liste mit der funktion dict()

Borhmaschine1 = dict([("artikelnummer",10010),("Leistung",850)])
Borhmaschine1 = dict(artikelnummer=10010,Leistung=850)          #Bei dieser Variante ist das
                                                                #Schlüsselwort immer in Zeichen 
                                                                #einzugeben und nicht als Zahl
#6.3 Tupel: unveränderliche Daten
Borhmaschine4= 10010,850,"Bosch",59.9       #Man kann die einzelnen Listenelemente ausgeben
                                            #mit Borhmaschine4[2] aber nicht abändern mit
                                            #Borhmaschine4[2]=700
tu=900,                                     #Tupel mit nur einem Wert benötigt ein Komma
Borhmaschine4=Borhmaschine4+tu              #Tubel mit einem + Erweitert
Borhmaschine4=10010,850,"Bosch",[59,99]     #Inhalt in Eckiger klammer lässt sich ändern
Borhmaschine4[3][0]=56.99
