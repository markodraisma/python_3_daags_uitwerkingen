#!/usr/bin/env python3

def omkeer(s):
    """keert een string om
    parameter:
    s - de om te keren string (VALUE)
    """
    return s[::-1]

def makeupper(s):
    """Maakt van een string een uppercase string
    parameter:
    s - de te 'uppercasen' string (VALUE)
    """
    return s.upper();

def doalle(l, s):
    """laat een lijst van functies los op een string
    parameters:
    l - de lijst van functies
    s - de string
    """
    for f in l:
        s = f(s)
    return s
    		


l=[ omkeer, makeupper ]

print( doalle(l, "lower case string") )
# uitvoer: GNIRTS ESAC REWOL
