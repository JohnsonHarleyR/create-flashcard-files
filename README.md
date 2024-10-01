# create-flashcard-files
There should eventually be both a python program and HTML/JavaScript file. The Python program should allow the user to create flashcards. The HTML/JavaScript should allow the user to view and use those flashcards to study. There may also be helper files that are used while creating the code.

# Python - flashcard.py
A python program to create flashcards and place them into a JSON file. Each flashcard will have a colored symbol to help with memory.

What the program should do:
1. Ask the user whether to (A) open an existing JSON file to add to, or (B) create a new.
2. A. Ask for name of file, open and load file to continue working on. B. Ask for name and create new file with name.
3. Find out the name of these flashcards. What class or title would they like to use? If (A) the file was loaded, just get this information from the file. If (B) find out and store this information from the user.
4. There should be a dictionary with a list of used symbols - a list, the title - a string, and the chapters - a list. The chapter list will be sorted by chapter number, so each item will be a dictionary with a chapter number, a chapter title, and then a list of flashcards under that chapter. Each flashcard in the list should be it's own dictionary that gets the color and symbol to display, the question, and the answer.
5. Ask the user if they want to add a new flashcard. If yes, ask for the section, the question, and the answer. The symbol should be generated randomly.
6. To generate the symbol, there should be a list of possible colors and possible symbol numbers. It should select a random color and a random symbol. After this, it should check the list of used colors and symbols (can be the same color or the same symbol, but can not have both of the same attributes). If the symbol is already used, it should generate a different symbol instead and keep doing this until it finds an unused symbol.
7. After each flashcard is completed, ask the user if they would like to add another. Once they say no, save the file and close the program. Allow them to save their progress at any time.

8. In the future, allow the user to modify the questions and answers and symbols in a file. Allow them to delete. This should be after the entire program is complete, if I ever have extra time and want to add this extra feature. It isn't hard to open a text file and delete items and used symbols, so it isn't super important, but it would be a nice feature.

Future Purpose
The future purpose of this program is to be able to load the created JSON files into a JavaScript program in order to display and use the flashcards while studying.

# Python - support/helper.py
The sole purpose of this file should be to aid in creating flashcard.py.

# Files Folder - files/
This is where all the text files created by flashcards.py should be stored. This should be accessed by the html/javascript file as well in order to display the flashcards.

# HTML/JavaScript - index.html
A page to display and even print the flashcards will eventually be created once the python files are complete.

# Format for Dictionary of Flashcards
Note: The values are examples for the sake of understanding the format.
{
    className: "Name of Class",
    chapters: [
        {
            chapterNumber: 1,
            chapterName: "First Chapter Name",
            flashcards: [
                {
                    symbol: {
                        color: "#ffffff",
                        number: 100,
                    },
                    question: "Question or description here",
                    answer: "Answer to question here"
                },
                {
                    symbol: {
                        color: "#fffff0",
                        number: 101,
                    },
                    question: "Question or description here",
                    answer: "Answer to question here"
                }
            ]
        },
        {
            chapterNumber: 2,
            chapterName: "Second Chapter Name",
            flashcards: [
                {
                    symbol: {
                        color: "#ffff00",
                        number: 200,
                    },
                    question: "Question or description here",
                    answer: "Answer to question here"
                },
                {
                    symbol: {
                        color: "#fff000",
                        number: 201,
                    },
                    question: "Question or description here",
                    answer: "Answer to question here"
                }
            ]
        }
    ],
    usedSymbols: [
        {color: "#ffffff", number: 100},
        {color: "#fffff0", number: 101},
        {color: "#ffff00", number: 200},
        {color: "#fff000", number: 201}
    ],
}

