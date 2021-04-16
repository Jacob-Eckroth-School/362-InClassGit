
def divisors(num):
    divisorsList = []
    for i in range(num,0,-1):
        if(num%i == 0):
            divisorsList.append(i)
    print(divisorsList)

def getUserInput():
    input = input("Please enter a positive integer:")



getUserInput()