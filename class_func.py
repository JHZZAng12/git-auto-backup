class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------ student list ------")
        print("name \t total \t average")

        for student in cls.students:
            print(str(student))

        print("------ ------ ------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + \
               self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )


Student("insung", 87, 98, 88, 95)
Student("hajin", 92, 98, 96, 98)
Student("ziyeoun", 76, 96, 94, 90)
Student("sunju", 98, 92, 96, 92)
Student("arin", 95, 98, 98, 98)
Student("myoungwall", 64, 88, 92, 92)
Student("mihwa", 82, 86, 98, 88)
Student("yeounhwa", 88, 74, 78, 92)
Student("ahyeon", 97, 92, 88, 95)
Student("juneseo", 45, 52, 72, 78)


Student.print()
