#Code example for Lecture 2 WEBPROG 2017
#Python 3.4, Windows 7
#Author: Charlotte Lesley, copy of Peter Mozelius's code from the year before
"""
Expanded by Rasmus Hen for Assignment 1, WEBPROG 2018
Python 3.6.2, Windows 10
"""

import geometri

def main():
    print("GeoTest: \n")
    p1 = geometri.Punkt(3, 4)
    p2 = geometri.Punkt(5, 2)
    print(str(p1))
    print(p2)
    print(p1 == p2)

#Testar Cirkel-klassen
    c1 = geometri.Cirkel(7, 3, 4)
    c2 = geometri.Cirkel(11, 5, 2)
    c3 = geometri.Cirkel(7, 3, 4)
    print("Cirkeln area =", c1.get_area())
    print("Cirkeln omkrets =", c1.get_circumference())
    print(c1 == c2)
    print(c1)
    print(c3)
    print(c1 == c3, "\n")

#----------------Expansion starts here-----------------------------

#Tests the class "Rektangel"
    #defines the three variables r1, r2 and r3
    r1 = geometri.Rektangel(5, 6, 2, 7)
    r2 = geometri.Rektangel(6, 3, 9, 2)
    r3 = geometri.Rektangel(5, 6, 2, 7)
    #Tests the methods get_area() and get_circumference()
    print("Första rektangelns area är: " + str(r1.get_area()))
    print("Första rektangelns omkrets är: " + str(r1.get_circumference()))
    print("Andra rektangelns area är: " + str(r2.get_area()))
    print("Andra rektangelns omkrets är: " + str(r2.get_circumference()))
    print("Tredje rektangelns area är: " + str(r3.get_area()))
    print("Tredje rektangelns omkrets är: " + str(r3.get_circumference()))
    #Tests the method __str__()
    print(r1)
    print(r2)
    print(r3)
    #Tests the method __eq__()
    if r1 == r2:
        print("Första och andra rektangeln är likadana\n")
    elif r1 == r3:
        print("Första och tredje rektangeln är likadana\n")
    elif r2 == r3:
        print("Andra och tredje rektangeln är likadana\n")
    else:
        print("Ingen av rektanglarna är likadana\n")


#Tests the class "Triangel"
    #Defines the three variables t1, t2 and t3
    t1 = geometri.Triangel(7, 8, 3, 2)
    t2 = geometri.Triangel(7, 8, 3, 2)
    t3 = geometri.Triangel(2, 6, 4, 9)
    #Tests the methods get_area() and get_circumference()
    print("Första triangelns area är: " + str(t1.get_area()))
    print("Första triangelns omkrets är: " + str(t1.get_circumference()))
    print("Andra triangelns area är: " + str(t2.get_area()))
    print("Andra triangelns omkrets är: " + str(t2.get_circumference()))
    print("Tredje triangelns area är: " + str(t3.get_area()))
    print("Tredje triangelns omkrets är: " + str(t3.get_circumference()))
    #Tests the method __str__()
    print(t1)
    print(t2)
    print(t3)
    #Tests the method __eq__()
    if t1 == t2:
        print("Första och andra triangeln är likadana")
    elif t1 == t3:
        print("Första och tredje triangeln är likadana")
    elif t2 == t3:
        print("Andra och tredje triangeln är likadana")
    else:
        print("Ingen av trianglarna är likadana")




if __name__ == "__main__":
    main()
