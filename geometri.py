#Code example for Lecture 2 WEBPROG 2017
#Python 3.4, Windows 7
#Author: Charlotte Lesley, copy of Peter Mozelius's code from the year before
"""
Expanded by Rasmus Hen for Assignment 1, WEBPROG 2018
Python 3.6.2, Windows 10
"""

import math

class Punkt():
    
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

    def __str__(self):
        return "Punkt: (" + str(self.__x) + ", " + str(self.__y) + ")"




class Cirkel(Punkt):

    def __init__(self, radie, x = 0, y = 0):
        Punkt.__init__(self, x, y)
        self.__radie = radie


    def get_radie(self):
        return self.__radie

    def get_area(self):
        return math.pi * (self.__radie ** 2)

    def get_circumference(self):
        return math.pi * 2 * self.__radie

    def __eq__(self, other):
        return self.__radie == other.get_radie() and Punkt.__eq__(self, other)

    def __str__(self):
        return "Cirkel med radien: " + str(self.__radie) + " och x = " + str(self.get_x()) + ", y = " + str(self.get_y())

#-----------------------Expansion starts here---------------------------
class Rektangel(Punkt):
    
    #Defines the constructor that in turn calls the cunstructor in the class "Punkt" and creates the attributes __height and __width
    def __init__(self, height, width, x = 0, y = 0):
        Punkt.__init__(self, x, y)
        self.__height = height
        self.__width = width
        
    #Defines a method to get the attribute __height
    def get_height(self):
        return self.__height
    
    #Defines a method to get the attribute __width
    def get_width(self):
        return self.__width
    
    #Defines a method to get the area of a given rectangle
    def get_area(self):
        return self.__width * self.__height
    
    #Defines a method to get the circumference of a given rectangle
    def get_circumference(self):
        return (self.__width * 2) + (self.__height * 2)
    
    #Changes the method __eq__() to compare two rectangles with each other
    def __eq__(self, other):
        return self.__height == other.get_height() and self.__width == other.get_width() and Punkt.__eq__(self, other)
    
    #Changes the method __str__() to return a new string when called
    def __str__(self):
        return "Rektangel med höjden: " + str(self.__height) + " och bredden: " + str(self.__width) + ", x = " + str(self.get_x()) + " och y = " + str(self.get_y())


class Triangel(Punkt):
    #Defines the constructor that in turn calls the cunstructor in the class "Punkt" and creates the attributes __height and __width
    def __init__(self, height, width, x = 0, y = 0):
        Punkt.__init__(self, x, y)
        self.__height = height
        self.__width = width

    #Defines a method to get the attribute __height
    def get_height(self):
        return self.__height

    #Defines a method to get the attribute __width
    def get_width(self):
        return self.__width

    #Defines a method to get the area of a given triangle
    def get_area(self):
        return (self.__width * self.__height) / 2

    #Defines a method to get the circumference of a given triangle
    def get_circumference(self):
        return (self.__width ** 2 + self.__height ** 2) ** (0.5)

    #Changes the method __eq__() to compare two triangles with each other
    def __eq__(self, other):
        return self.__height == other.get_height() and self.__width == other.get_width() and Punkt.__eq__(self, other)

    #Changes the method __str__() to return a new string when called
    def __str__(self):
        return "Triangel med höjden: " + str(self.__height) + " och bredden: " + str(self.__width) + ", x = " + str(self.get_x()) + " och y = " + str(self.get_y())    












        
    
