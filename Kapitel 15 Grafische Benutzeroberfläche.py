# -*- coding: utf-8 -*-
#Kapitel 15 Grafische Benutzeroberflächen mit Tkinter erzeugen

"""
Grafische Oberflächen in Python zu Programmieren ist sehr aufwendig. 
Andere Programmierer haben daher diese Aufgabe eines entsprechenden 
Moduls in Phyton vorgenommen. Dieses wird als GUI-Toolkit bezeichnet.
Es steht für Graphical User Interface.

Es gibt mehrere möglichichkeiten Fenster in Python zu gestalten,
hier verwenden wir Tkinter. 
Dabei handelt es sich um das älteste und am weitesten verbreitete GUI-Toolkit 
für Python. Es ist außerdem kostenfrei und bereits im Python Interpreter 
enthalten, wesshalb keine zusätliche installation notwendig ist. 

Tkinter wird auch in der Standardbiblithek behandelt. Zu Beginn ist es sinnvoll, 
einen kurzen Blick in dieses Kapitel zu werfen, um einen Überblick über die 
Möglichkeiten zu erhalten. Außerdem sind hier viele Tutorials und 
Nachschlagewerke verlinkt, die einen tiefergehenden Einstie in Tkinter 
ermöglichen, als es hier möglich ist.
"""
#------------------------------------------------------------------------------
# Kapitel 15.1 Ein erstes einfaches Fenster erstellen
#------------------------------------------------------------------------------

"""
Um mit Tkinter zu arbeiten, ist es zunächst notwendig, das entsprechende Modul 
zu importieren
"""
# from tkinter import *
"""
Wie die meisten Module in Python arbeitet auch Tkinter mit Objekten. Jedes 
Fenster, das entstehen soll, ist ein Objekt. Die entsprechende Klasse hierfür 
lautet Tk. Es ist bei der Erzeugung des Objekts nicht notwendig, Werte aus dem 
Hauptprogramm zu übergeben. Durch folgende Code-Zeile entsteht ein neues Objekt  
des Typs Tk:
"""
# fenster =Tk()
"""
Nun hat man zwar bereits ein Objekt für das Fenster ertellt, wenn man das 
Programm aufruft, passiert aber bislang nichts. Das liegt daran, dass es 
notwendig ist, die mainloop-Methode aufzurufen, um das Fenster anzuzeigen. Wenn 
man den entsprechenden Befehl einfügt, ist es bereits möglich, das erste 
Fenster anzuzeigen:
"""
# from tkinter import *

# fenster = Tk()
# fenster.mainloop()
"""
Es öffnet sich ein lehres Fenster

Ein Fenster kann verschiedene weitere Elemente enthalten. Diese müssen nach der 
Erstellung des Fensters, aber vor dem Aufruf der mainloop-Metode hinüzugefügt 
werden.

Zum platzieren eines Textes im Fenster kommt ein Label zum Einsatz. Auch 
hierbei handelt es sich um ein Objekt. Als Parameter bei der Erstellung ist es 
notwendig, den Text einzufügen, den das Label wiedergeben soll:
"""
#label = Label(text="Willkommen zum Python-Kurs!")
"""
Damit das erstellte Label auch auch angezeigt wird, kommt die pack-Methode
zum einsatz. Es fügt das Label zum Fenster hinzu und ordnet es an
"""
# from tkinter import *

# fenster = Tk()

# label = Label (text="Willkommen zum Python-Kurs!")
# label.pack()

# fenster.mainloop()
"""
Die Abbildung zeigt, dass der Text nun zwar ausgegeben wird, doch ist das 
Fenster winzig klein. Das liegt daran, dass es sich automatisch an den 
ausgegebenen Text anpasst. Daher ist es notwendig, eine feste Größe vorzugebeb. 
Auf diese Weise wird es deutlich ansprechender. Hierfür kommt die 
geometry-Methode zum Einsatz. Dabei kann man als Parameter die Breite und die 
Höhe vorgeben.
"""
# fenster.geometry("300x100")
"""
Darüber hinaus soll der Tetel des Fensters angepasst werden. Dieser trägt 
standarmäßig die Bezeichnung tk. Mit der title-Methode lässt sich das jedoch 
individuell anpassen:
"""
# fenster.title("Python-Kurs)
"""
Zum Schluss soll noch ein Rahmen eingefügt werden, damit das Fenster optisch 
etwas ansprechender wird. Hierfür ist das Objekt Frame notwendeig. Als 
Parameter wird diesem in der Regel das Element übermittelt, in das er eingefügt 
wird. In diesem Fall wäre dieses das Objekt fenster. Diese Angabe ist hierbei 
jedoch optional, da es sich bei fenster um das Hauptobjekt handetl. Ist keine 
weiter Angabe enthalten, wird dieses automatisch verwendet. Für eine 
individuelle Gestaltung ist es möglich, die Art des Rahmens 
(in diesem Fall ridge) und die Breite des Randes zu übermitteln:
"""
# rahmen = Frame (fenster, relief="ridge", borderwidth=5)
"""
Um den Rahmen einzufügen, kommt wieder die pack-Methode zum Einsatz. Dieser 
müssen nun jedoch die Attribute fill = "both" un expand = 1 übergeben werden. 
Diese sorgen dafür, dass der Rahmen das gesamte Fenster abdeckt und nciht nur 
den Bereich mit der Schrift:
"""
# rahmen.pack(fill="both",expand = 1)
"""
Wenn man nun das Programm ausführt, stellt man fest, dass zunächst der Rahmen 
angezeigt wird, und erst danach die Schrift. Das Ziel besteht jedoch darin, 
dass die Schrift innerhalb des Rahmens steht. Dafür ist es notwendig, dem Label 
den Rahmen als übergeordnetes Element zuzuweisen.

Dafür muss er lediglich als Parameter übermittelt werden:
"""
# label = Label(rahmen, text"Willkommen zum Python-Kurs!")
"""
Nun ist das Fenster bereits fast fertig. Nur noch ein kleines Detail wirkt 
störend: Die Schrift befindet sich ganz oben im Fenster. Um dies zu ändern, muss 
bei der pack-Methode für das Label noch das Attribut expand = 1 eingefügt werden:
"""
# label.pack(expand =1)
"""
Dieser Befehl ist dann sinnvoll, wenn das übergeordnete Element (also in diesem 
Fall das Tk-Objekt fenster) durch den geometry-Befehl künstlich vergrößert wird 
und daher mehr Platz bietet, als die darin enthaltenen Elemente benötigen. Er 
bewirkt, dass das Label so weit vergrößert wird, dass es den gesamten freien 
Raum einnimmt. Auf diese Weise erscheint es in der Mitte des Fensters.
"""
# Aus dem bishier beschrieben Inhalt ergibt sich folgendes Begrüßungsfenster

# from tkinter import *

# fenster = Tk()
# fenster.geometry("300x100")
# fenster.title("Python-Kurs")
# rahmen= Frame(fenster, relief="ridge", borderwidth=5)
# rahmen.pack(fill="both",expand=1)

# label = Label(rahmen, text="Willkommen zum Python-Kurs!")
# label.pack(expand=1)

# fenster.mainloop()

#------------------------------------------------------------------------------
# 15.2 Buttons mit Funktionen hinzufügen
#------------------------------------------------------------------------------
"""
Um einen Button in das Fenster einzufügen, ist es zunächst notwendig, ein Objekt 
dieses Typs zu erzeugen: button = Button(). Um ihn in das Fenster zu integrieren, 
kommt wieder der pack-Befehl zum Einsatz: 
"""
# button.pack().
"""
Wenn man das Programm ausführt, erscheint der Button zwar bereits, doch sitzt 
er außerhalb des Rahmens und hat keine Beschriftung. Damit er innerhalb des 
Rahmens erscheint, ist es notwendig, bei der Erzeugung den Rahmen als 
übergeordnetes Element anzugeben- genau wie dies beim Label gemacht wurde. 
Außerdem ist es hierbei möglich, auch gleich die Beschriftung vorzugeben.

Der Befehl siet dann wie folgt aus:
"""
# button = Button(rahmen, text ="OK")
"""
Alternativ dazu lässt sich der Beschriftungstext auch erst später einfügen. 
Wenn man dies nicht bereits bei der Erzeugung des Objekts gemacht hat, kann man 
später auf die einzelnen Attribute zugreifen.

Dafür wäre folgender Befehl notwendig:
"""
# button["text"]="OK"
"""
Wenn man das Programm jetzt ausführt, hat der Button bereits eine Beschriftung 
und befindet sich innerhalb des Rahmens. Allerdings sitzt er hier ganz oben und 
nicht wie gewünscht am unteren Rand des Fensters. Dafür ist es notwendig, den 
pack-Befehl azupassen:
"""
# button.pack(side ="bottom")
"""
Wenn man auf den Button klickt, passiert aber noch nichts. Dafür ist es 
notwendig, einen Befehl für das Attribut command vorzugeben. Dieser lautet 
fenster.destroy und führt dazu, dass das Fenster geschlossen wird. Alternativ 
dazu wäre es auch möglich, den Befehl fenster.quit zu verwenden. Dieser hat auf 
den ersten Blick genau die gleiche Auswirkung. Während fenster. destroy jedoch 
nur das entsprechende Fenster schließt, beendet fenster.quit den kompletten 
TCL-Interpreter, der für die Gestaltung der Fenster verantwortlich ist. Das 
kann jedoch auch andere Fenster, die gerade geöffnet sind, beeinflussen und 
sollte daher vermieden werden.

Genau wie bei der Beschriftung kann dies entweder direkt bei der Erzeugung des 
Objekts oder später durch einen dirketen Zugriff erfolgen.

In diesem Beispiel sollen alle Eigenschaften des Buttons bereis bei dessen 
Erzeugung eingefügt werden, SODASS DER Code wie folgt aussieht:
"""
# from tkinter import *

# fenster = Tk()
# fenster.geometry("300x100")
# fenster.title("Python-Kurs")

# rahmen = Frame(fenster, relief="ridge", borderwidth=5)
# rahmen.pack(fill="both",expand=1)

# button = Button(rahmen, text="OK", command=fenster.destroy)
# button.pack(side = "bottom")

# label=Label(rahmen,text="Willkomen zum Python-Kurs!")
# label.pack(expand=1)

# fenster.mainloop()
"""
Wenn man nun auf den OK-Button klickt, wird das Fenster geschlossen.

Buttons sind nicht nur zum Schließen von Fenstern da, sondern können alle 
denkbaren Funktionen aufrufen bzw. ausführen. In unseren Fall soll ein Kurzer 
Print befehl in der Console ausgeführt werden.  
Dafür soll zunächst ein weiterer Button in das Fenster eingefügt werden.

Um die Funktion des Buttons festzulgene, ist es notwendig, ihm eine eigene 
Methode zuzuweisen. Da kein direkter Zugriff auf die Klasse Button möglich ist, 
soll eine Unterklasse von dieser abgeleitet werden. Diese soll den Namen 
MyButton erhalten. Sie enthält lediglich eine Methode, die ausgeführt werden 
soll, wenn der Button angeklickt wird. In diesem Fall soll hier ein einfacher 
print-Befehl stehen. Es wäre aber auch möglich, eine Datei einzulesen, ein 
neues Fenster zu öffnen oder eine beliebige andere Aktion durchzuführen. Die 
Unterklasse My Button muss wie folgt aussehen:
"""
# class MyButton(Button):
#     def aktion(self):
#         print("Sie haben den Button gedrückt")
"""
Wenn man nun den Button in das Programm einfügen will, muss dieser nicht wie im 
vorherigen Beispiel ein Objekt der Klasse Button darstellen, sondern der Klasse 
MyButton. Er soll als übergeordnetes Objekt wieder den Rahmen enthalten und die 
Beschriftung soll Action! lauten.
"""
# button2 = MyButton(rahmen, text="Action!")
"""
Die command-Zuweisung kann in diesem Beispiel nicht in diesem Befehl stehen. 
Der Grund dafür leigt darin, dass diese eine Methode des neu erstellten Objekt 
aufrufen soll. Das ist erst möglich, nachdem dieser Vorgang abgeschlossen wurde. 
Daher ist es notwendig, in der nächsten Zeile folgenden Befehlt einzufügen:
"""
# button2["command"] = button2.aktion
"""
Dieser ruft die zuvor erstellte Methode auf, sobald der Button angeklickt wird.
Danach ist es nur noch notwednig, den Button wieder mit dem pack-Befehl in das
Fenster einzubinden. Danach ist das Programm bereits vollständig.
"""

# from tkinter import *

# class MyButton(Button):
#     def aktion (self):
#         print("Sie haben den Button gedrückt")
        
# fenster = Tk()

# fenster.geometry("300x100")
# fenster.title("Python-Kurs")
# rahmen = Frame(fenster, relief="ridge", borderwidth=5)
# rahmen.pack(fill="both",expand=1)

# button = Button(rahmen,text="OK",command=fenster.destroy)
# button.pack(side="bottom")

# button2 = MyButton(rahmen,text="Action!")
# button2["command"] = button2.aktion
# button2.pack(side="bottom")

# label = Label(rahmen, text="Willkommen zum Python-Kurs!")
# label.pack(expand=1)

# fenster.mainloop()


#------------------------------------------------------------------------------
#15.3 Das Layout der Fenster
#------------------------------------------------------------------------------

"""
Aktuell sieht das Fenster noch nicht schön aus. Wie etwa, die anordnung der
Buttons und deren Unterschiedliche größe. Aus diesem grund soll der folgende 
Abschnitt sich mit dem Layout befassen.

Tkinter verfügt über mehrere Lyout-Manager, die sich um die Anordnung der 
Elemente im Fenster kümmern. In den bisherigen Beispeilen wurde stets der 
pack-Manager verwendet. Dieser ist zwar einfach anzuwenden, doch bietet er nur 
sehr wenige Gestaltungsmöglichkeiten.

Mit den Befehlen fill und expand, ist es möglich, vorzugeben, wie der zur 
Verfügung stehende Raum ausgefüllt werden soll. Außerdem hatten wir den Befehl
side = bottom. Dieser sorgte dafür, dass der Button am unteren Rand des Fensters
erschien. Anstatt bottom kann man an dieser Stelle auch top,left oder right 
angeben. Damit sind die Möglichkeiten des Layout-Managers jedoch bereits 
weitestgehend erschöpft.

Deutlich mehr Möglichkkeiten bietet der grid-Manager. Dieser ermöglicht eine 
tabellenartige Gestaltung des Fensters. Hierbei ist es stets notwendig, die 
Zeile und die Spate anzugeben, in der das entsprechende Element stehen soll. 
Der grid-Manager teilt das Fenster dann in so viele Zeilen und Spalten ein, 
dass er alle Werte, die der Programmierer angegeben hat, bedienen kann.

Auf diese Weise wäre es beispielsweise möglich, die beiden Buttons nebeneinander 
im unteren Bereich des Fensters einzufügen, während das Label zentral 
positioniert bleibt.

Bevor man sich der Tabelle widmet, ist jedoch noch eine kleine Anpassung bei 
den Buttons notwendig. Diese soll die gleiche Breite erhalten. Das ist möglich, 
indem man bei beiden Elementen width = 10 einfügt.

Wenn man sich die gewünschte Anordnung als Tabelle vorstellt, wäre hierfür ein 
System mit zwei Zeilen und zwei Spalten sinnvoll. In der ersten Spalte der 
ersten Zeile steht das Label. In der zweiten Zeile stehen die beiden Buttons 
(jeweils in verschiedenen Spalten)

Daher ist für das Label und die beiden Buttons folgender Code notwendig:
"""

# label = Label(rahmen,text="Willkommen zum Python-Kurs!")
# label.grid(row=2,column=1)

# button2 = MyButton(rahmen,width=10,text="Action!")
# button2["command"] = button2.aktion
# button2.grid(row=2,column=1)

# button = Button(rahmen,text="OK", width=10,command=fenster.destroy)
# button.grid(row=2,column=2)

"""
Wenn man sich das Fenster nun anschaut, stellt man fest, dass die grundlegende 
Struktur zwar bereits vorhanden, die Anordnung der einzelnen Elemente jedoch 
nicht optimal ist. Ein Problem besteht darin, dass das Label mit dem 
Begrüßungstext links im ersten Feld erscheint. Es soll jedoch zentriert werden. 
Um dies zu erreichen, ist es notwendig, dass es beide Spalten der ersten Zeile 
ausfüllt.

Dafür ist es notwendig, den Befehl columnspan = 2 einzufügen:
"""
#label.grid(row=1,column=1,columnspan=2)
"""
Damit entspricht das Fenster bereits etwas besser den Designvorstellungen. 
Allerdings sind alle Elemente in der linken oberen Ecke versammelt. Um das zu 
ändern, ist es notwendig, Abstände einzufügen. Das geschieht mit dem Befehl 
pdax für horizontale Abstände und pady für vertikale Abstände.

Dabei ist es pro Zeile oder Spalte nur einmal notwendig, die entsprechenden 
Voraben zu machen. Sie werden dann bei allen anderen Elementen, die sich in 
derselben Zeile oder Spalte befinden, übernommen.

Um die richtigen Abstände herauszufinden, muss man etwas probieren, bis man die 
richtigen Werte findet. Für das Label bietet es sich beispielsweise an, pady=15 
und padax=50 festzulegen. Für die Buttons ist pady=10 sinnvoll. Dieser Wert muss 
nur beim ersten Button eingetragen werden.

Daraus ergibt sich folgendes Programm für eine ansprechende Darstellung der 
einzelnen Elemente:
"""
# from tkinter import *

# class MyButton(Button):
#     def aktion(self):
#         print("Sie haben den Button gedrückt")
        
# fenster = Tk()

# fenster.geometry("300x100")
# fenster.title("Python-Kurs")
# rahmen = Frame(fenster, relief="ridge", borderwidth=5)
# rahmen.pack(fill="both",expand=1)

# label= Label(rahmen, text="Willkommen zum Python-Kurs")
# label.grid(row=1,column=1,columnspan=2,pady=15,padx=50)

# button2= MyButton(rahmen,width=10,text="Action!")
# button2["command"]= button2.aktion
# button2.grid(row=2,column=1,pady=10)

# button= Button(rahmen,text="OK",width=10,command=fenster.destroy)
# button.grid(row=2,column=2)

# fenster.mainloop()
"""
Es gibt noch eine weitere Alternative zum grid-Manager: den place-Manager.
Dieser ermöglicht eine vollkommen freie Anordnung aller Elemente. Dafür ist es 
lediglich notwendig, die x- und die y-Koordinaten innerhalb des Fensters 
anzugeben.

Auf diese Weise lässt sich ebenfalls ganz einfach ein Fenster mit der 
gewünschten Anordnung erstellen:
"""
# from tkinter import *

# class MyButton(Button):
#     def aktion(self):
#         print("Sie haen den Button gedrückt")

# fenster=Tk()

# fenster.geometry("300x100")
# fenster.title("Python-Kurs")
# rahmen=Frame(fenster, relief="ridge", borderwidth=5)
# rahmen.pack(fill="both",expand=1)

# label=Label(rahmen, text="Willkommen zum Python-Kurs!")
# label.place(x=60,y=20)

# button2=MyButton(rahmen,width=10,text="Action!")
# button2["command"]=button2.aktion
# button2.place(x=40,y=60)

# button=Button(rahmen,text="OK",width=10,command=fenster.destroy)
# button.place(x=170,y=60)

# fenster.mainloop()

#------------------------------------------------------------------------------
# 15.4 Weitere Elemente für die Gestaltung der Fenster u. Eingabe ermöglichen
#------------------------------------------------------------------------------

"""
Bei vielen Programmen ist es notwendig, dem Anwender eine Eingabe zu 
ermöglichen. Zu diesem Zweick kommt das Objekt Entry zum Einsatz. Es erzegt ein 
Textfeld, in das der Nutzer einen beliebigen Text eintragen kann. Für dieses 
Objekt ist folgender Befehl notwendig:
"""
# eingabe = Entry()
"""
Als Parameter sollte hier wieder das übergeordnete Element stehen

Außerdem ist es möglich, weitere Vorgaben zu machen (beispielsweise zur Breite 
des Eingabefeldes und zur Stärke des Rahmens). Meistens wird dieses Eingabefeld 
zusammen mit einem Label verwendet, das dem Anwender aufzeigt, welchen Wert er 
hier eingeben soll. Um zu wissen, wann das Programm die Eingabe aufnehmen soll, 
ist darunter noch ein Button notwendig. Dieser soll die Methode aktion1 
aufrufen, die den Wert des Feldes abspeichert.

Dieser muss dann noch mit dem pack-Befehl in das Fenster eingefügt werden:
"""
# label = Label(rahmen,text="Geben Sie Ihren Namen ein: ")
# label.pack()

# eingabe = Entry(rahmen,bd=2,width=22)
# eingabe.pack()

# button = MyButton(rahmen,text="Eingabe")
# button["command"]=button.aktion1
# button.pack()
"""
Auch hier ist es wieder notwendig, eine Klasse für den Button zu erstellen. 
Diese soll zunächst den Wert der Eingabe abrufen und in der Variablen name 
speichern. Dazu kommt die get-Methode zum Ensatz. Danach gibt sie den Wert über 
den Kommandozeileninterpreter aus.

Schließlich entfernt sie die aktuelle Eingabe wieder aus dem Feld Dazu dient die 
delete-Methode. Diese muss den Anfangs- und den Endpunt des Bereichs, der 
gelöscht werden soll, enthalten. Da die Position des Endpunkts nicht bekannt 
ist, kommt hierfür der Plazhalter end zum Einsatz. Das führt dazu, dass stets 
der gesamte bereich bis zum Ende der Eingabe gelöscht wird.
"""
# class MyButton(Button):
#     def aktion1(self):
#         name = eingabe.get()
#         print(name)
#         eingabe.delet(0,'end')
"""
Anschließend soll ein Checkbox hinzugefügt werden. Diese kann der Anwender 
anklicken, wenn er eine bestimmte Auswahl treffen oder einen Vorgang bestätigen 
will. Dabei ist es möglich, eine Variable abzurufen, um die Auswahl 
abzuspeichern.

Zu diesem Zweck kommt der Datentyp IntVar zum Einsatz, der speziell für Tkinter 
entwickelt wurde. Hierbei handelt es sich genau genommen um ein Objekt. Dieses 
muss daher zunächst erzeugt werden. In diesem Beispiel erhhält es den Namen var:
"""
# var = IntVar()
"""
Innerhalb der Parameter bei der Erzeugung des Checkbuttons ist es notwendig, 
den gewählten Namen dem Ausdruck variable zuzuweisen:
"""
# variable = var
"""
Wenn die Checkbox ausgewählt wurde, beträgt der Wert 1, wurde sie nicht 
ausgewählt, beträgt er 0. Um das Ergebis abzurufen, ist die get-Methode notwendig. 
Ein Button unter der Checkbox soll eine Methode aufrufen, die den Wert abfragt 
und über den Komandozeileninterpreter ausgibt.

Diese Methode sieht wie folgt aus:
"""
# def aktion2(self):
#     print(var.get())
"""
Für die Erzeugung er Checkbox und des Buttons ist folgender Code notwendig:
"""
# var = IntVar()
# checkbutton = Checkbutton(rahmen,text="Bestätigun",variable = var)
# checkbutton.pack()

# button2 = MyButton(rahmen,text="Eingabe")
# button2["command"] = button.aktion2
# button2.pack()
"""
Schließlich soll noch ein Feld mit einer kleinen Scrollbar eingefügt werden. 
Dafür sind gleich zwei Objekte notwendig: eine Scrollbar und eine Listbox.

Zunächst muss die Scrollbar erstellt und in den Rahmen eingefügt werden
"""
# scrollbar = Scrollbar(rahmen)
"""
Danach folgt die Listbox. Diese wird ebenfalls in den Rahmen eingefügt. Um sie 
mit der Scrollbar zu verbinden, ist der Parameter 
yscrollcommand = scrollbar.set notwendig.

Danach folgt eine for-Schleife, die mit dem insert-Befehl 50 Zeilen in 
die Liste einfügt:
"""
# liste = Listbox(rahmen,yscrollcommand = scrollbar.set)
# for i in range(50):
#     liste.insert(END,"Zeile"+str(i))
"""
Danach ist es notwendig, diese Zeile einzufügen:
"""
#scrollbar.config(command=liste.yview)
"""
Sie sorgen dafür, dass sich eine Änderung der Scrollbar mit der Maus auch auf 
die Anzeige innerhalb des Felds auswirkt. Nun muss zunächst die Liste und dann 
die Scrollbar mit dem pack-Befehl in das Fenster eingefügt werden. Damit beide 
Elemente nebeneinder stehen, ist es notwendig, jeweils side = "left" als 
Parameter vorzugeben. Damit die Scrollbar die gleiche Höhe wie die Liste hat, 
wird der Parameterfill = "y benötigt"
"""
# liste.pack(side="left")
# scrollbar.pack(side = "left",fill="y")
"""
Damit ist auch dieses Element komplett, sodass es möglich ist, den 
vollständigen Programmcode anzugeben:
"""
from tkinter import *

class MyButton(Button):
    def aktion1(self):
        name = eingabe.get()
        print(name)
        eingabe.delete(0, 'end')
    
    def aktion2(self):
        print(var.get())

fenster = Tk()
fenster.geometry("300x200")  # Größerer Platz für Listbox und Scrollbar
fenster.title("Python-Kurs")

rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)

label = Label(rahmen, text="Geben Sie Ihren Namen ein: ")
label.pack()

eingabe = Entry(rahmen, bd=2, width=22)
eingabe.pack()

button = MyButton(rahmen, text="Eingabe")
button["command"] = button.aktion1
button.pack()

var = IntVar()
checkbutton = Checkbutton(rahmen, text="Bestätigen", variable=var)
checkbutton.pack()

button2 = MyButton(rahmen, text="Eingabe")
button2["command"] = button.aktion2
button2.pack()

scrollbar = Scrollbar(rahmen)
scrollbar.pack(side="right", fill="y")  # Ändere die Position zu 'right'

liste = Listbox(rahmen, yscrollcommand=scrollbar.set)
liste.pack(side="left", fill="both", expand=1)  # Ändere die Position zu 'left'

for i in range(50):
    liste.insert(END, "Zeile " + str(i))

scrollbar.config(command=liste.yview)

fenster.mainloop()

















