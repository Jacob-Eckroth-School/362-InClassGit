
def calc(a,b):
    sum = a + b
    print("Sum: ", str(sum))
    difference = a - b
    print("Difference: ",str(difference))
    multiply = a * b
    print("Product: ", str(multiply))
    divide = 0
    if(b != 0):
        divide = a / b
        print("Quotient: ",str(divide))
    else:
        print("You can't divide by zero!!!")
    results = [sum,difference,multiply,divide]
    addedList = 0
    for num in results:
        addedList += num
    print("Added list: ", str(addedList))


calc(4,3)



