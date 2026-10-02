import math

class Circle:

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("radius is number")
            self.__radius = value
    
