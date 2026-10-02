import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)


    def get_radius(self):
        return self.__radius
    def set_radius(self,value):
        self.__radius = value

circle = Circle(10)
print("# circle circumference, area.")
print("circumference:", circle.get_circumference())
print("circle area:", circle.get_area())

print()

print("#__radius")
print(circle.get_radius())
print()

circle.set_radius(2)
print("radius = 2 ")
print("circumference:", circle.get_circumference())
print("circle area:", circle.get_area())
