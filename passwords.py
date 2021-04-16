import random


def createPass(num):
    password = ""
    for i in range(0,num):
        randomNumber = random.randint(32,126)
       
        password += chr(randomNumber)

    print("Your password: " + password)


def getUserInput():
    userInput = input("Please enter a positive integer:")
    while(not userInput.isdigit() or int(userInput) == 0):
        print("Incorrect input, please enter a integer >0")
        userInput = input("Please enter a positive integer:")
    createPass(int(userInput))

getUserInput()