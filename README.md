# create-flashcard-files
A python program to create flashcards and place them into a JSON file. Each flashcard will have a colored symbol to help with memory.

What the program should do:
1. Ask the user whether to (A) open an existing JSON file to add to, or (B) create a new.
2. A. Ask for name of file, open and load file to continue working on. B. Ask for name and create new file with name.
3. Find out the name of these flashcards. What class or title would they like to use? If (A) the file was loaded, just get this information from the file. If (B) find out and store this information from the user.
4. There should be a dictionary with a list of used symbols - a list, the title - a string, and the flashcards - a list. Each flashcard in the list should be it's own dictionary that gets the color and symbol to display, the section the question is from, the question, and the answer.
5. Ask the user if they want to add a new flashcard. If yes, ask for the section, the question, and the answer. The symbol should be generated randomly.
6. To generate the symbol, there should be a list of possible colors and possible symbol numbers. It should select a random color and a random symbol. After this, it should check the list of used colors and symbols (can be the same color or the same symbol, but can not have both of the same attributes). If the symbol is already used, it should generate a different symbol instead and keep doing this until it finds an unused symbol.
7. After each flashcard is completed, ask the user if they would like to add another. Once they say no, save the file and close the program. Allow them to save their progress at any time.

8. In the future, allow the user to modify the questions and answers and symbols in a file. Allow them to delete. This should be after the entire program is complete, if I ever have extra time and want to add this extra feature. It isn't hard to open a text file and delete items and used symbols, so it isn't super important, but it would be a nice feature.

# Future Purpose
The future purpose of this program is to be able to load the created JSON files into a JavaScript program in order to display and use the flashcards while studying.