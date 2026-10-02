def test(function):
    def wrapper():
        print("Hello start")
        function()
        print("finish Hello")
    return wrapper


@test
def hello():
    print("hello")

hello()
