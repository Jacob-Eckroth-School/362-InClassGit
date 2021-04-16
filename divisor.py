
def divisors(num):
    divisorsList = []
    for i in range(num,0,-1):
        if(num%i == 0):
            divisorsList.append(i)
    print(divisorsList)

def getUserInput():
    userInput = input("Please enter a positive integer:")
    while(!isdigit(userInput)):
        print("Incorrect input, please enter a positive integer >0")
        userInput = input("Please enter a positive integer:")
    divisors(int(userInput))
getUserInput()