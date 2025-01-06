def calculator():
    print("Please enter 2 numbers.")
    a = int(input("Num 1: "))
    b = int(input("Num 2: "))
    c = input("Please enter the function (+, -, x, /) you wish to compute: ")
    if c == '+':
        print(add(a,b))
    elif c == '-':
        print(subtract(a,b))
    elif c == 'x':
        print(multiply(a,b))
    elif c == '/':
        print(divide(a,b))


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


calculator()