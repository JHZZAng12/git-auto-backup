class CustomException(Exception):
    def __init__(self):
        super().__init__()
        print("#### error create####")

    def __str__(self):
        return "ERROR"

raise CustomException

  
