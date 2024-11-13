# Kapitel 15 Aufgabe 2
"""
Erstellen Sie eine Chackbox und einen Button. Wenn der Anwender den Button 
anklickt, soll ein neues Fenster mit einer beliebigen Nachricht geöffnet werden, 
allerdings nur, wenn die Checkbox zuvor ausgewählt wurde.
"""
from tkinter import *

class MyButton(Button):
    def aktion(self):
        if var.get()==1:
        
            fenster = Tk()
            fenster.geometry("300x200")  # Größerer Platz für Listbox und Scrollbar
            fenster.title("Checkbox Text is open")
            rahmen = Frame(fenster, relief="ridge", borderwidth=5)
            rahmen.pack(fill="both", expand=1)
            lable = Label(rahmen,text="You have it done")
            lable.pack(fill="both",expand=1)

fenster = Tk()
fenster.geometry("300x200")  # Größerer Platz für Listbox und Scrollbar
fenster.title("Checkbox open a Text")

rahmen = Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)

var = IntVar()
checkbutton = Checkbutton(rahmen,text="Setzt den Haken und Bestätige und \nes öffnet sich ein neues Fenster",variable=var)
checkbutton.place(x=40,y=60)

button = MyButton(rahmen,width=10,text="Bestätige")
button["command"]=button.aktion
button.place(x=100,y=100)

mainloop()