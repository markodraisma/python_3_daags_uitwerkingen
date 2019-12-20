#!/usr/bin/env python3

class Medium(object):
    """Een Medium klasse
    bedoeld als superclass van alle echte media
    """

    def __init__(self, titel, prijs):
        self.settitel(titel)
        self.setprijs(prijs)

    def settitel(self, titel):
        self.titel = titel

    def setprijs(self, prijs):
        self.prijs = prijs

    def show(self):
        print('Titel: ', self.titel)
        print('Prijs: ', self.prijs)

    def __str__(self):
        return "Titel: %s, Prijs: %s" % (self.titel, self.prijs)

class Boek(Medium):
    """Een boek klasse
    """

    def __init__(self, titel, prijs, auteur, paginas):
        super().__init__(titel, prijs)
        self.setauteur(auteur)
        self.setpaginas(paginas)

    def setauteur(self, auteur):
        self.auteur = auteur
    
    def setpaginas(self, paginas):
        self.paginas = paginas

    def settitel(self, titel):
        if len(titel)>100:
            raise Exception("Dat is te lang")
        else:
            super().settitel(titel)
    
    def show(self):
        super().show()
        print('Auteur: ', self.auteur)
        print('Paginas: ', self.paginas)
		
    def __str__(self):
        return super().__str__() + "\nAuteur: %s, Paginas: %s" % (self.auteur, self.paginas)

class Strip(Boek):
    
    def __init__(self, titel, prijs, auteur, paginas, tekenaar):
        super().__init__(titel, prijs, auteur, paginas)
        self.settekenaar(tekenaar)
        
    def settekenaar(self, tekenaar):
        self.tekenaar = tekenaar  

    def show(self):
        super().show()
        print('Tekenaar: ', self.tekenaar)
		
    def __str__(self):
	    return super().__str__() + "\nTekenaar: %s" % self.tekenaar 
        

if __name__ == '__main__':
#             titel             prijs   auteur                     paginas
    leapr = Boek("Learning Python", 35.50, "Mark Lutz & David Ascher", 595)

#             titel                    prijs   auteur    pags tekenaar
    astrx = Strip("Asterix en Cleopatra", 3.95, "Goscinny", 32, "Uderzo")

#             titel                    prijs   regisseur       leeftijd
# spody = Dvd("2001, a space odyssey", 17.50, "Stanley Kubrik", 12)

    leapr.show()    # druk leapr af
    astrx.show()
    print(astrx)
# spody.show()
