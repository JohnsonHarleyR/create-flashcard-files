import sys
import random
import json

# Basic functions
def formatInput(input):
    return input.lower().strip()

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

def getTxtFileName(inputString):
    isCorrectFormat = False
    userInput = ""
    while isCorrectFormat == False:
        userInput = formatInput(input(inputString))
        if ".txt" not in userInput:
            print("Must be '.txt' file. Please add '.txt' to the end.")
        else:
            isCorrectFormat = True
    return userInput
        
def convertToJson(dict):
    return json.dumps(dict, sort_keys=True, indent=4)

allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def getOptionIndexByLetter(letter):
    formattedLetter = formatInput(letter)
    for i in range(0, len(allLetters)):
        if allLetters[i] == formattedLetter:
            return i
    return -1 #this indicates an error

def getLetterFromIndex(index):
    if index < len(allLetters) and index >= 0:
        return(allLetters[index])
    return "ERROR"

# Unchanging variables
#list of unicode numbers - 1056 possible combinations
unicodeNumbers = ['2600', '2601', '2602', '2603', '2604', '2605', '2606', '2607', '2608', '2809', '260A', '260B', '260C', '260D', '260E', '260F', '2610', '2611', '2612', '2613', '2616', '2617', '2618', '2619', '261A', '261B', '261C', '261E', '261F', '2620', '2621', '2622', '2623', '2624', '2625', '2626', '2627', '2628', '2629', '262A', '262B', '262C', '262D', '262E', '262F', '2630', '2631', '2632', '2633', '2634', '2635', '2636', '2637', '2638', '2639', '263A', '263B', '263C', '263D', '263E', '263F', '2640', '2641', '2642', '2643', '2644', '2645', '2646', '2647', '2654', '2655', '2656', '2657', '2658', '2659', '265A', '265B', '265C', '265D', '265E', '265F', '2660', '2661', '2662', '2663', '2664', '2665', '2666', '2667', '2668', '2669', '266A', '266B', '266C', '266D', '266E', '266F', '2670', '2671', '2672', '2680', '2681', '2682', '2683', '2684', '2685', '2686', '2687', '2688', '2689', '268A', '268B', '268C', '268D', '268E', '268F', '2690', '2691', '2692', '2693', '2694', '2695', '2696', '2697', '2698', '2699', '269A', '269B', '269C', '269D', '269E', '269F']
colors = ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff", "#a0c4ff", "#bdb2ff", "#ffc6ff"]

def generateRandomSymbol(usedSymbols):
    randomColor = ""
    randomUnicode = 0
    while True:
        randomColor = random.choice(colors)
        randomUnicode = random.choice(unicodeNumbers)
        isAlreadyUsed = False
        for symbol in usedSymbols:
            if symbol["color"] == randomColor and symbol["number"] == randomUnicode:
                isAlreadyUsed = True
                break
        if isAlreadyUsed == False:
            newSymbol = {
                "color": randomColor,
                "number": randomUnicode
            }
            usedSymbols.append(newSymbol)
            return newSymbol
        

nameForFile = ""
fileInfo = {
    "className": "",
    "chapters": [],
    "usedSymbols": []
}

# Menu Options Function
def selectMenuOption(options):
    selectedIndex = -1
    while selectedIndex == -1 or selectedIndex >= len(options):
        print("\nPlease select from the following options.")
        for i in range(0, len(options)):
            letterToPrint = getLetterFromIndex(i).upper()
            text = options[i][0]
            print(letterToPrint + ". " + text)
        userInput = input("\nSelected letter: ")
        selectedIndex = getOptionIndexByLetter(userInput)
        if selectedIndex == -1 or selectedIndex >= len(options):
            print("Error in selecting option. Please enter valid letter for an option.")
        else:
            func = options[selectedIndex][1]
            func()
            selectedIndex = -1

# Possible Option Functions
def unavailableOption():
    print("OPTION IS UNAVAILABLE")

def createNewFile():
    global fileInfo
    print("")
    #TODO Add validation for filename
    global nameForFile
    nameForFile = getTxtFileName("Creating new flashcards file. What should the file be called?: ")
    fileInfo["className"] = input("Name of class: ")
    print("\nOkay, let's create a chapter to add flashcards to.")

    modifyFileInfo()

def modifyFileInfo():

    def addNewFlashcard(flashcardsInChapter):
        print("")
        print("Adding new flashcard.")
        newSymbol = generateRandomSymbol(fileInfo["usedSymbols"])
        question = input("Question or definition: ")
        answer = input("Answer: ")
        flashcardsInChapter.append({
            "symbol": newSymbol,
            "question": question,
            "answer": answer
        })

    def doesChapterAlreadyExist(chapterNumber):
        chapters = fileInfo["chapters"]
        for chapter in chapters:
            if chapter["chapterNumber"] == chapterNumber:
                return True
        return False

    def getChapterIndex(chapterNumber):
        chapters = fileInfo["chapters"]
        for i in range(0, len(chapters)):
            if chapters[i]["chapterNumber"] == chapterNumber:
                return i
        return -1 #indicates nothings was found

    def printExistingChapters():
        print("\nHere are the existing chapters.")
        for chapter in fileInfo["chapters"]:
            print(str(chapter["chapterNumber"]) + ". " + chapter["chapterName"])


    def assembleChapterWithFlashcards(chapterNumber, chapterName, flashcardsInChapter):
        addAnotherFlashcard = True
        while addAnotherFlashcard == True:
            addNewFlashcard(flashcardsInChapter)
            userAnswer = formatInput(input("Add another flashcard to chapter?(y/n): "))
            if userAnswer != "y":
                addAnotherFlashcard = False

        chapter = {
            "chapterNumber": chapterNumber,
            "chapterName": chapterName,
            "flashcards": flashcardsInChapter
        }
        return chapter

    def modifyExistingChapter():
        global fileInfo
        if len(fileInfo["chapters"]) == 0:
            print("No chapters exist yet. Please create a new one.")
            return
        
        chapterNumber = -1
        doesChapterExist = False
        while doesChapterExist == False:
            printExistingChapters()
            #TODO allow options other than just adding more flashcards, but for now this is fine
            chapterNumber = getInteger("Which chapter would you like to add flashcards to?: ")
            doesChapterExist = doesChapterAlreadyExist(chapterNumber)
            if doesChapterExist == False:
                print("\nThat chapter doesn't exist. Please choose an existing chapter.")
        chapterIndex = getChapterIndex(chapterNumber)
        
        chapterNumber = fileInfo["chapters"][chapterIndex]["chapterNumber"]
        chapterName = fileInfo["chapters"][chapterIndex]["chapterName"]
        chapterFlashcards = fileInfo["chapters"][chapterIndex]["flashcards"]

        replacementChapter = assembleChapterWithFlashcards(chapterNumber, chapterName, chapterFlashcards)

        fileInfo["chapters"][chapterIndex]["flashcards"] = replacementChapter["flashcards"]

    def createNewChapter():
        global fileInfo
        print("")
        # TODO Ensure chapter number doesn't already exist
        chapterNumber = 0
        alreadyExists = True
        while alreadyExists == True:
            chapterNumber = getInteger("Chapter number: ")
            alreadyExists = doesChapterAlreadyExist(chapterNumber)
            if alreadyExists == True:
                #TODO If the number already exists, give an option to switch over to modifying that chapter
                print("That chapter number already exists. Please enter a new chapter.")
        
        chapterName = input("Chapter name: ")
        chapter = assembleChapterWithFlashcards(chapterNumber, chapterName, [])
        
        fileInfo["chapters"].append(chapter)
            
    def saveFile():
        fileInfoAsJson = convertToJson(fileInfo)
        filePath = f"files/{nameForFile}"
        print("name for file: ", nameForFile)
        with open(filePath, 'w') as convert_file: 
            convert_file.write(fileInfoAsJson)
        print("\nSave is complete!")

    def askToSaveFirst():
        userAnswer = formatInput(input("\nWould you like to save first?(y/n): "))
        if userAnswer == "y":
            saveFile()

    def exitProgram():
        askToSaveFirst()
        print("\nExiting Program. Goodbye!")
        sys.exit()

    fileMenuOptions = [
        ["Create new chapter for adding flashcards", createNewChapter],
        ["Modify existing chapter", modifyExistingChapter],
        ["Save progress", saveFile],
        ["Return to main menu", unavailableOption],
        ["Exit program", exitProgram]
    ]


    #Create a chapter by default and add one flashcard. After that, start showing menu.
    #createNewChapter()
    
    selectMenuOption(fileMenuOptions)

def exitFromMainMenu():
    print("\nExiting Program. Goodbye!")
    sys.exit()

# Menu Option Variables
mainMenuOptions = [
    ["Create New File", createNewFile],
    ["Load Existing File", unavailableOption],
    ["Exit Program", exitFromMainMenu]
]

def showMainMenu():
    selectMenuOption(mainMenuOptions)

# Ask user to create or load file or exit
showMainMenu()
