class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())
students = [
    Student("insung", 87,98,88,95),
    Student("hajin", 92,98,96,98),
    Student("ziyeon", 76,96,94,90),
    Student("suckju", 98,92,96,92),
    Student("arin", 95,98,98,98),
    Student("myungwall", 64,88,92,92)
]

print("name", "total","average",sep="\t")

for student in students:
    print(str(student))
