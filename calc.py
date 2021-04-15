
def calc(a,b):
    sum = a + b
    print(sum)
    difference = a - b
    print(difference)
    multiply = a * b
    print(multiply)
    divide = None
    if(b != 0):
        divide = a / b
        print(divide)
    else:
        print("You can't divide by zero!!!")
    results = [sum,difference,multiply,divide]


calc(4,3)



