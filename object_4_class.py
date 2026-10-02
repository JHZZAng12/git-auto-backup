class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science= science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() /4
    
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
students = [
    Student("insung", 87, 98, 88, 95),
    Student("hajin", 92, 98, 96, 98),
    Student("ziyeoun", 76, 96, 94, 90),
    Student("sunju", 98, 92, 96, 92),
    Student("arin", 95, 98, 98, 98),
    Student("myoungwall", 64, 88, 92, 92)
]     

print("name","total score", "average", sep="\t")
for student in students:
    print(student.to_string())
