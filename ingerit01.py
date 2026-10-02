class Parent:
    def __init__(self):
        self.value = "test"
        print("Parent class __init__ method call")

    def test(self):
        print("Parent class test() method")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class __init__ method call")


child = Child()
child.test()
print(child.value)
