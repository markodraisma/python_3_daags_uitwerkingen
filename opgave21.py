#!/usr/bin/env python3
class Geld(object):
    """een Geld klasse
    """

    def __init__(self, euro, cent, valuta="EUR"):
        self.euro = euro 
        self.cent = cent
        self.valuta = valuta
        self._normalize()

    def _normalize(self):
        self.euro+= self.cent // 100
        self.cent = self.cent % 100


    def __add__(self, other):
        if not isinstance(other,Geld):
            raise TypeError("geld kan alleen bij geld worden opgeteld")
        if not self.valuta == other.valuta:
            raise TypeError("Valuta komt niet overeen")
        val = Geld(self.euro + other.euro, self.cent + other.cent)
        return val

    def __mul__(self, factor):
        if not isinstance(factor,int):
            raise TypeError("geld kan alleen met een geheel getal worden vermenigvuldigd")
        return Geld(self.euro*factor, self.cent*factor)

    def __rmul__(self, factor):
        return self.__mul__(factor)

    def __truediv__(self, factor):
        if not isinstance(factor,int):
            raise TypeError("geld kan alleen door een geheel getal worden gedeeld")
        g=Geld(0, (self.euro*100+self.cent) // factor)
        return g
        
    def __str__(self):
        return "{valuta} {euro},{cent:02d}".format(valuta=self.valuta, euro=self.euro, cent=self.cent)

if __name__ == '__main__':
    g1 = Geld(1,75)
    g2 = Geld(1,10)
    g2 = 3 * g2
    print(g1+g2)
    g3 = g1+g2
    print(g3)
    g3/=5
    print(g3)
    g1+=g3
    print(g1)

