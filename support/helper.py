# Helper functions should go here to aid in creating main python program
def formatInput(inputString):
    return inputString.lower().strip()

def checkIfStringIsInteger(string):
    try:
        int(string)
        return True
    except:
        return False
    
def getInteger(inputString):
    isInteger = False
    userInput = ""
    while isInteger == False:
        userInput = formatInput(input(inputString))
        isInteger = checkIfStringIsInteger(userInput)
        if isInteger == False:
            print("Input is not an integer. Please try again.")
    return int(userInput)

def generateNumbers():
    #generate numbers here
    print("\nGENERATE LIST OF NUMBERS\nEnter a start and end range.\nKeep doing this until you are finished.")
    print("A list separated by commas will display at the end.\n")

    numbersString = ""
    keepGoing = "y"
    isFirst = True
    while keepGoing == "y":
        startNumber = getInteger("Starting number: ")
        endNumber = getInteger("Ending number: ")
        while startNumber <= endNumber:
            if isFirst == True:
                numbersString = numbersString + str(startNumber)
                isFirst = False
            else:
                numbersString = numbersString + ", " + str(startNumber)
            startNumber += 1
        keepGoing = formatInput(input("Keep going? (y/n): "))
    print("\nHere is the finished list of numbers:")
    print(numbersString)



userInput = ""
while userInput != "exit":
    print("\nOPTIONS")
    print("A. Generate Numbers with Commas")
    print("OR type 'exit' to end program.\n")

    userInput = formatInput(input("What would you like to do?: "))
    if userInput == "exit":
        break
    if userInput == "a":
        generateNumbers()
    


