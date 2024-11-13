#Unterfunktion Aufgabe Kapitel 9 Aufgabe 2 Passwort Username

# liste=[("Hans","Passwort01"),("Basti","Passwort02")]

# for inhalt in liste:
#     print(inhalt)

def User_Passwort (User,Passwort):
    userlist= [("Hans","Passwort01"),("Basti","Passwort02")]
    
    for i in userlist:
        if i[0]==User and i[1]==Passwort:
            print("Zugangsdaten gefunden")
            return True
        
    print("Zugangsdaten nicht gefunden")
    return False