createPass(num):


def getUserInput():
    userInput = input("Please enter a positive integer:")
    while(not userInput.isdigit() or int(userInput) == 0):
        print("Incorrect input, please enter a integer >0")
        userInput = input("Please enter a positive integer:")
    createPass(int(userInput))