# Kapitel 15 Aufgabe 1
"""
Gestalten Sie ein Fenster, das zwei Eingabefelder enthält, in die der Anwender 
jeweils eine Zahl einfügen soll. Danach folgt ein Button und dann ein weiteres 
Eingabefeld. Wenn der Anwender den Button betätigt, soll das Programm die Wert 
der beiden Felder addieren und as Ergebnis mit dem insert-Befehl im letzten 
Eingabefeld ausgeben. Dieser muss als Parameter zunächst die Zahl 0 erhalten, 
damit deas Ergebnis an der ersten Position des Feldes angezeigt wir. Danach 
folgt die Ausgabe (also das Ergebnis der Addition). Ordnen Sie die einzelnen 
Elemente mit dem place-Manager an.
"""

from tkinter import *

class TheButton(Button):
    def addition(self):
        x=5+1
        print(x)
        
fenster =Tk()
fenster.title("Addition")
fenster.geometry("300x100")
rahmen = Frame(fenster,relief="ridge",borderwidth=5)
rahmen.pack(fill="both",expand=1)

label = Label(rahmen,text="Addition")
label.grid(row=1,column=1,columnspan=2,pady=15,padx=120)

button = TheButton(rahmen,width=10,text="Addition")
button["command"]= button.addition
button.grid(row=2,column=2)

eingabe = Entry()

        

fenster.mainloop()