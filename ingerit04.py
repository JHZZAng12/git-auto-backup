class CustomException(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message = message
        self.value =value

    def __str__(self):
        return self.message

    def print(self):
        print("####ERROR INFO####")
        print("message:", self.message)
        print("value:",self.value)
try:
    raise CustomException("No reason", 273)
except CustomException as e:
    e.print()
