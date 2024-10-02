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
#list of unicode numbers - 1632 possible combinations
unicodeNumbers = [10672, 10673, 10674, 10675, 10676, 10677, 10678, 10679, 10680, 10681, 10682, 10683, 10684, 10685, 10686, 10687, 10688, 10689, 10690, 10691, 10692, 10693, 10694, 10695, 10696, 10697, 10728, 10729, 10730, 10731, 10732, 10733, 10734, 10735, 10736, 10737, 10738, 10739, 10809, 10810, 10811, 9016, 9017, 9018, 9019, 9020, 9021, 9022, 9023, 9024, 9025, 9026, 9632, 9633, 9634, 9635, 9636, 9637, 9638, 9639, 9640, 9641, 9642, 9643, 9644, 9645, 9646, 9647, 9648, 9649, 9650, 9651, 9652, 9653, 9654, 9655, 9656, 9657, 9658, 9659, 9660, 9661, 9662, 9663, 9664, 9665, 9666, 9667, 9668, 9669, 9670, 9671, 9672, 9673, 9674, 9675, 9676, 9677, 9678, 9679, 9680, 9681, 9682, 9683, 9684, 9685, 9686, 9687, 9688, 9689, 9690, 9691, 9692, 9693, 9694, 9695, 9696, 9697, 9698, 9699, 9700, 9701, 9702, 9703, 9704, 9705, 9706, 9707, 9708, 9709, 9710, 9711, 9712, 9713, 9714, 9715, 9716, 9717, 9718, 9719, 9720, 9721, 9722, 9723, 9724, 9725, 9726, 9727, 9728, 9729, 9730, 9731, 9732, 9733, 9734, 9735, 9736, 9737, 9738, 9739, 9740, 9741, 9742, 9743, 9760, 9761, 9762, 9763, 9764, 9765, 9766, 9767, 9768, 9769, 9770, 9771, 9772, 9773, 9774, 9775, 9776, 9777, 9778, 9779, 9780, 9781, 9782, 9783, 9784, 9785, 9786, 9787, 9788, 9789, 9790, 9791, 9792, 9793, 9794, 9795, 9796, 9797, 9798, 9799]
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
