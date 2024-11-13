#Kapitell 13 Daten in Dateien dauerhaft abspeichern
"""
13.2 Daten in die Datei schreiben

Um inerhalb eines Programm Inhalte in eine Datei zu schreiben, müssen diese 
mittels open('DateiName')-Befehl geöfnet werden.
Ist eine Datei mit diesem Namen Vorhanden wird diese geöfnet oder andernfalls
erstellt.
Um auf Dateien zuzugreifen, die in einem anderen Dateienphat liegen als das 
Programm, so muss entsprechend der Datenphat mit angegeben werden. 
Ausgangsordner ist immer jener, in welchem sich das Programm befindet.
Darüber hinaus muss angegeben werden, auf welche Weise zugegriffen wird.
z.B. w für write um eine Datei zu schreiben.

open('DatenNamen','w') write    (Schreiben)
open('DatenNamen','a') append   (Anhängen)

Der open()-Befehl erzeigt ein Objekt, dass den Zugriff auf die Inhalte der Datei
ermöglicht. Dieses gibt er als Rückgabewert zurück. Daher ist es notwendig,
es in einer Variablen aufzunehmen. Deren Name ist zwar frei wählbar, doch ist 
es üblich, hier für den Buchstaben "f" als Abkürzung für "file" zu verwenden.
"""
# #Bsp.
# f = open('Kapitel 13 Bsp.text.txt','w')
# f.write("Hier kommt ein Text")
# f.close()

# #Bsp.
# f = open('Kapitel 13 Bsp.text.txt','w')
# text = input("Schreibe einen Text: ")
# f.write(text)
# f.write("\nEnde der Nutzer-Eingabe\n")
# f.close()

"""
13.3 Daten aus der Datei auslesen

Auslesen mittels
open('DatenName','r') read     (lesen)
"""
# #Bsp.
# f = open('Kapitel 13 Bsp.text.txt','r')
# inhalt = f.read()
# print(inhalt)
# f.close()
"""
Für Zeilenweise Ausgabe über den readlines()-Befehl. Dieser gibt eine Liste
zurück. In jedem Feld ist eine Zeile der Datei enthalten.
"""
# #Bsp.
# f =open('Bsp.Text.txt','r')

# inhalt = f.readlines()
# print (inhalt)
# print("\n",inhalt[0])   #Zeile 0 des txt
# print("Anzahl der Zeilen: %d" %len(inhalt))
# f.close()
"""
Es ist auch möglich auf bestimmte Zeilen mittels einer forschleife zuzugreifen
"""
# #Bsp.
# f =open('Bsp.Text.txt','r')
# i=1
# for inhalt in f:
#     print("Zeile %d: %s" %(i,inhalt))
#     i += 1
# f.close()



"""
13.4 XML-Datein verwenden
Der vorteil gegenüber txt: Bei dem Datentransfähr von beispielsweise txt
müsse eine genaue Strucktur vorliegen, in welcher Zeile was steht um auf 
deren Inhalte zuzugreifen. Wenn eine Datei gesendet wird um zum Beispiel ein
Katalog von Waren zu senden, die wiederrum bei einem anderen Anbieter in sein
Katalog geladen werden soll, wären solche struckturen schwierig in der 
Komunikation und fehleranfälltig. Daher ist es sinnig XML-Daten zu nehmen.

XML verden sogennnte Tags, um Inhalte auszuzeichnen. Deren Bezeichnung kann 
man frei wählen. Um sie zu kennzeichnen, kommen spitze Klammern <> zum Einsatz.
Vor der eigentlichen Information steht ein öffnendes Tag. Danach steht ein 
schließendes Tag. Dieses erhält die gleiche Bezeichnung wie das öffnende Tag 
allwesings mit einem vorangestellten Schrägstrich.
"""
# #Bsp. Für Artikelnummer eines Gerätes angeben aus einer XML-Datei.
# <artikelnummer>10010</artikelnummer>
"""
Tags sind hierarchisch aufgebaut. Das heißt, dass ein Tag weitere Tags 
enthalten kann. Es gibt einige weitere Regeln zum erstellen eines Tags,
die hier aber nicht alle erwähnt werden, da es den Inhalt an dieser stelle
unnötig sprengen würde. 
"""
# # Bsp. Sortiment einer XML-Datei eines Großhändlers das als 
# # BeispielXML-Datei im Ordner gespeichert ist.

# <?xml version="1.0" encoding="ISO-8859-1"?>
# <sortiment>
#     <bohrmaschine>
#         <artikelnummer>10010</artikelnummer>
#         <leistung>850</leistung>
#         <marke>Bosch</marke>
#         <preis>46.25</preis>
#     </bohrmaschine>
#     <bohrmaschine>
#         <artikelnummer>10014</artikelnummer>
#         <leistung>1000</leistung>
#         <preis>42.25</preis>
#     </bohrmaschine>
#     <winkelschleifer>
#         <artikelnummer>10207</artikelnummer>
#         <leistung>600</leistung>
#         <marke>Bosch</marke>
#         <preis>30.67</preis>
#     </winkelschleifer>
# </sortiment>
"""
So sieht also eine xml datei aus. Zum weiteren Testen ist es möglich
diesen Text im Ordner des Programms zu  als und die ändung von txt auf xml zu
ändern.

Um die xml-datei zu öffnen kommt der befehl open() zum einsatz, als auch
read() zum einlesen. Die inhalte einzelner Tags müssen in Variablen 
abgespeichert werden. Dazu wird ein XML-Parser verwendet. Dieser erkennt
die einzelnen Tags und kann deren Inhalt extrahieren.

Als erstes frag das Programm den anwender nach welchen Begriff
er suchen will und speichert diesen Wert in der Varbiable eingabe ab.
Daruafhin fügt es Klammern und ggebenfalls den Schrägstrich hinzu, um das 
entsprechende Anfags- und das End-Tag zu erstellen.
"""
# anfang ="<"+eingabe+">"
# ende = "</"+eingabe+">"
"""
Im nächsten Schritt wird die Datei eingelsen und es wird nach dem entsprechenden
Tag gesucht, dazu der Befhel find() zur anwendung auf string-Variablen.
In der Klammer steht der Ausdruck, nachem gesucht wird. Dieses Kommando
gibt ie Possition innerhalb des Textes an, an der sich der erste Buchstabe des 
gesuchten Ausdrucks befindet. Um die Inhalte zu extrahieren, benötigt man die 
Positionen, an denen dieser beginnt und endet. Dafür werden die folgenden 
Befehle verwendet:
"""
# start = inhalt.find(anfang)+len(anfang)
# stop = inhalt.find(ende)
"""
Für den Startpunkt muss die Position noh um die Länge des Anfangs-Tags erhöht 
werden. Das liegt daran, dass find()-Befehl immer die Position des ersten 
Buchstabens des Suchbegriffs zurückgibt. Wenn man diesen Wert unverändert 
übernimmt, würde auch das Start-Tag in den ausgewählten Inhalten erscheinen. 
Das ist jedoch nicht erwünscht. Indem man die Länge dieses Ausdrucks 
hinzuaddiert, wird der Startpunkt direkt hinter das Tag gesetzt. Mit diesen 
Informationen kann man nun den gewünschten Teilbereich des Dokuments ausgeben
"""
# #Bsp. des Kompletten Programms zum auslesen einer XML-Datei

# f = open('BspCodeXML.xml','r')

# eingabe = input("Nach welchen Tag möchten Sie suchen?") #(schreibe bohrmaschine oder winkelschleifer oder preis...)

# anfang = "<"+eingabe+">"
# ende = "</"+eingabe+">"

# inhalt = f.read()

# start = inhalt.find(anfang)+len(anfang)
# stopp = inhalt.find(ende)

# print("Inhalt des Tags: "+inhalt[start:stopp])

# f.close()

"""
Dieser kleine XML-Parser führt also nur einzige Grundfunktion aus und reicht 
nicht um Dokumente komplett zu verarbeite.
Da XML-Parser für eine komplette auswertung eines Dokumentes sehr aufwändig wären,
gibt es daher andere lösungen.
Dazu ist es eine wichtige entscheidung der richtigen wahl eines
API (Programmierschnittstelle). Es gibt dazu zahlreiche API wie etwa minidom,
ElementTree (etree) oder lxml. 
Hier verwenden wir minidom, da es für einsteiger am leichtesten ist zu erlernen.
Die Auswertung und gestalltung von XML-Daten und dies über auswahl von XML-API
ist ein eigenes komplexes thema das hier nicht im ganzen erfasst werden kann.

Zur einbindung des API minidom kommt folgender Befehl zum einsatz
"""
#from xml.dom import minidom
"""
danach der parse Befehl um Daten zu analysieren und zu verarbeiten
"""
#dokument = minidom.parse('beispiel.xml')
"""
Dabei wird der komplette Inhalt des XML-Dokuments in der ariablen dokument
gespeichert.
Danach fordern wir den Anwender zur Eingabe des Produkttyps auf:
"""
#eingabe = input("Welcher Produkttyp soll angezeigt werden?: ")
"""
Nun können wir innerhalb des Dokuments nach Tags mit der gewünschten Bezeichnung
suchen. Dazu der Befehl getElementsByTagName().
"""
#produktListe = dokument.getElementsByTagName(eingabe)
"""
In produktListe ist dnn eine Liste, die alle Tags entählt, die die entsprechende
Bezeichnung aufweist. Also, jedes einzelne Feld der Liste  ist ein spezifisches 
Produkt mit allen seinen Werten. Um alle einzelnen Inhalte auszugeen kann mit 
einer for-Schleife alle Listenellemente, also alle einzelnen Produkte
nacheinander durchgegangen werden.
"""
#for produkt in produktListe:
"""
minidom geht dabei nach dem Prinzip der Knotenpunkte vor.
Bei jedem Tag, bei jedem Attribut und bei jedem Text handelt es sich um eien
eigenen Knotenpunkt. Aufgrund der hierarchischen Struktur kann ein Knoten 
weitere Knotenpunkte enthalten. In diesem Bsp wollen wir genau auf diese 
untergeordneten Knotenpunkte zugreifen, z.B. auf den Preis,Marke oder ArtikelNr.

Wenn wir die Namen der entsprechenden Tags bereits kennen, können wir diese 
innerhalb der Schleife direkt ansteuern. Das ist in unserem Beispiel zwar der 
Fall, doch soll das Programm möglichst allgemein gehalten sein. Das bedeutet, 
dass es auch dann alle Inhalte ausgeben soll, wenn der Händler noch weitere 
Merkmale der Geräte angibt. Daher greifen wir auf das Attrribut child-Nodes 
zu, über das jeder Knotenpunkt verfügt. Darin sind alle Untergeordneten 
Alemente aufgelistet. Da es sich heirbei wieder um eine Liste handelt, beginnen
wir eine neue for-Schleife, um alle enthaltenen Elemente auszugeben.
"""
#for wert in produkt.childNodes:
"""
Die Liste chilNodes enthält die entsprechenden Tags für die Artikelnummer, die
Leistung und für die weiteren Eigenschaften der Geräte. Daher können wir in
dieser for-Schleife bereits darauf zugreifen. Allerdings müssen wir beachten,
dass in der Liste childNodes neben diesen Tags noch weitere Elemente enthalten
sind. Da wir die einzelnen XML-Tags übersichtlich darstellen wollten, haben
wir Zeilenumrüche und Einrückungen eingefügt. Minidom wertet diese jedoch als
Text und damit als einen eigenen Knotenpunkt. Daher müssen wir bei jedem
Durchlauf der Liste zunächst überprüfen, ob es sich dabei wirklich um
einweiteres XML-Element handelt. 
Dazu dient folgende if-Abfrage:
"""
#if wert.nodeType == minidom.Node.ELEMENT_NODE:
"""
Nun können wir die Werte ausgeben. Zunächst fügen wir den Namen des Tags in
den print-Befehl ein, um deutlich zu machen, was der entsprechende Wert
bedeutet. Dieser ist im Attribut tag-Name abgespeichert. Um auf den Inhalt
des Tags zuzugreifen, müssen wir in der Dokumentenstruktur noch eine Stufe
weiter vordringen. Das ist notwendig, da es sich wie gesagt bei dejem
Textelement um einen eigenen Knotenpunkt handelt. Dafür verwenden wir
das Attribut childNodes. Diesees verfügt wiederum über ein Attribut mit
der Bezeichnung data, das den gewünschten Wert enthält. Daher sieht unser
print-Befehl wie folgt aus:
"""
#print(wert.tagName+":"+wert.firstChild.data)
"""
Für eine übersichtliche Darstellung fügen wir am Ende der inneren for-Schleife
noch eine Leerzeile hinzu. Damit ist das Programm abgeschlossen:
"""
# #Bsp. im ganzen

# # Importiere das Modul für die Arbeit mit XML-Dokumenten
# from xml.dom import minidom

# # Parsen der XML-Datei und Laden des Dokuments
# dokument = minidom.parse('BspCodeXML.xml')

# # Benutzerabfrage nach dem Produkttyp
# eingabe = input("Welcher Produkttyp soll angezeigt werden?: ")

# # Erhalte alle Elemente, die dem eingegebenen Produkttyp entsprechen
# produktListe = dokument.getElementsByTagName(eingabe)

# # Durchlaufe alle gefundenen Produkte in der Liste
# for produkt in produktListe:
#     # Durchlaufe alle Kindknoten des aktuellen Produkts
#     for wert in produkt.childNodes:
#         # Prüfen, ob der Kindknoten ein Elementknoten ist
#         if wert.nodeType == minidom.Node.ELEMENT_NODE:
#             # Ausgabe des Tag-Namens und des Textinhalts des Elements
#             print(wert.tagName + ": " + wert.firstChild.data)
#     # Trenne die einzelnen Produkte durch eine neue Zeile
#     print("\n")

"""
Zusatz Kindknoten

Kindknoten sind Elemente, die direkt unter einem übergeordneten Knoten 
(auch Elternknoten genannt) in einer hierarchischen Struktur liegen. In 
XML-Dokumenten bedeutet das, dass Kindknoten innerhalb eines anderen Knotens 
stehen und von diesem eingeschlossen werden. Zum Beispiel:

xml

Kopieren
<elternknoten>
    <kindknoten1>Inhalt</kindknoten1>
    <kindknoten2>Inhalt</kindknoten2>
</elternknoten>

Hier sind <kindknoten1> und <kindknoten2> die Kindknoten des <elternknoten>.
"""


"""
Zusatz erklärung im print-Befehl

In print(wert.tagName + ": " + wert.firstChild.data) werden die +-Zeichen
verwendet, um mehrere Strings (Textteile) zusammenzufügen. Das : wird
einfach als Text eingefügt, um die Ausgabe besser lesbar zu machen.

Hier ist eine Zerlegung des Ausdrucks:

   	- wert.tagName: Dies gibt den Namen des aktuellen XML-Tags zurück.

    - ": ": Dies ist ein fester String, der einfach ": " enthält.

    - wert.firstChild.data: Dies gibt den Textinhalt des ersten 
      Kindknotens des aktuellen Tags zurück.

Durch das Zusammenfügen mit + wird eine vollständige Ausgabe 
wie "artikelnummer: 10010" erzeugt.
"""