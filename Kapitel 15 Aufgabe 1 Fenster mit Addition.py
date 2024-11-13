# Kapitel 15 Aufgabe 1
"""
Gestalten Sie ein Fenster, das zwei Eingabefelder enthält, in die der Anwender 
jeweils eine Zahl einfügen soll. Danach folgt ein Button und dann ein weiteres 
Eingabefeld. Wenn der Anwender den Button betätigt, soll das Programm die Werte 
der beiden Felder addieren und als Ergebnis mit dem insert-Befehl im letzten 
Eingabefeld ausgeben. Dieser muss als Parameter zunächst die Zahl 0 erhalten, 
damit das Ergebnis an der ersten Position des Feldes angezeigt wir. Danach 
folgt die Ausgabe (also das Ergebnis der Addition). Ordnen Sie die einzelnen 
Elemente mit dem place-Manager an.
"""

from tkinter import *

class TheButton(Button):
    def addition(self):
        zahl1= float( eingabe_1.get())
        zahl2= float(eingabe_2.get())
        eingabe_1.delete(0,'end')
        eingabe_2.delete(0,'end')
        ausgabe.delete(0,'end')
        ausgabe.insert(0,zahl1+zahl2)
        
fenster =Tk()
fenster.title("Addition")
fenster.geometry("300x200")
rahmen = Frame(fenster,relief="ridge",borderwidth=5)
rahmen.pack(fill="both",expand=1)

label1 = Label(rahmen,text="Addition zweier werte")
label1.pack()

label_eingabe_1= Label(rahmen,text="Wert1")
label_eingabe_1.place(x=20,y=20)
eingabe_1 = Entry(rahmen,bd=2,width=15)
eingabe_1.place(x=20,y=50)

label_eingabe_2= Label(rahmen,text="Wert1")
label_eingabe_2.place(x=180,y=20)
eingabe_2 = Entry(rahmen,bd=2,width=15)
eingabe_2.place(x=180,y=50)

button = TheButton(rahmen,width=10,text="Addition")
button["command"]= button.addition
button.place(x=100,y=80)

ausgabe=Entry(rahmen,bd=2,width=15)
ausgabe.place(x=90,y=120)

fenster.mainloop()



