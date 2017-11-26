def my_decorator(func):
    def wrapper(a,b):
        print(a+b)
        func(9,2)
        print("1")
    return wrapper

@my_decorator
def diff(a,b):
    print(a-b)

print(diff(8,7))

