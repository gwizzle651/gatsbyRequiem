'''
General use library for creating "Choose Your Own Adventure" games.

Please note that file structure for this shall place the main program with the library, and a folder for the chapters and characters.
'''
import os
import keyboard
from time import sleep


def clear():
    '''
    Clears the terminal, allowing it to be easily read
    '''
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def selectFromList(items: list[str]) -> str:
    '''
    Displays a numbered list of items and returns the user's selection.

    :param items: A list of strings.
    :type items: list[str]
    :return selection: The user's selection.
    :rtype: str
    '''
    for index, item in enumerate(items):
        print(f"[{index + 1}] {item}")
    
    choiceIndex = getInput(len(items)) - 1
    selection = items[choiceIndex]
    return selection

class character():
    def __init__(self, name = "N/A", gender = "N/A", hairColor = "N/A", eyeColor = "N/A", skinColor = "N/A", height = "N/A"):
        # Traits
        self.name = name
        self.gender = gender
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.skinColor = skinColor
        self.height = height
        # Stats
        self.health = 50
        self.strength = 0
        self.intellect = 0
        self.dexterity = 0

def getInput(options: int) -> int:
    '''
    Accepts input for storytelling
    
    :param options: The amount of options, with the maximum of 10 (Buttons 1-0 on keyboard)
    :return choice: Returns an integer of 1-0, based on keyboard input.
    '''
    while True:
        choice = keyboard.read_key()
        try:
            if int(choice) == 0:
                choice = 10
            if int(choice) > options:
                choice = options
            return int(choice)
        
        except Exception:
            choice = options
            return int(choice)

def createCharacter() -> object:
    '''
    Goes through the process of creating a character for the game.

    :return character: A compendium of traits [class]
    '''
    # Variable setup
    gendersPossible = ["male", "female"]
    eyeColorsPossible = ["black", "blue", "green", "brown", "gray"]
    heightPossible = ["very tall", "tall", "medium", "short", "very short"]
    hairColorsPossible = ["red", "brown", "black", "blond", "gray", "white"]
    skinColorsPossible = ["pale", "tan", "olive", "copper", "ebony"]

    creatingChar = character()
    # Name selection
    creatingChar.name = input("What shall your adventurer be named (first and last)? ")
    sleep(0.5)

    # Gender selection
    clear()
    print("Please select a gender:")
    creatingChar.gender = selectFromList(gendersPossible)
    sleep(1)

    # Eye color setup
    clear()
    print(f"Your gender is {creatingChar.gender}, and your eyes are...")
    creatingChar.eyeColor = selectFromList(eyeColorsPossible)
    sleep(1)

    # Height setup
    clear()
    print(f"You are a {creatingChar.gender}, with {creatingChar.eyeColor} eyes, standing at a _______ height...")

    creatingChar.height = selectFromList(heightPossible)
    sleep(1)

    # Hair setup
    clear()
    print(f"You are a {creatingChar.gender}, with {creatingChar.eyeColor} eyes, standing at a {creatingChar.height} height. Your hair color is...")
    creatingChar.hairColor = selectFromList(hairColorsPossible)
    sleep(1)

    # Skin Color
    clear()
    print(f"You are a {creatingChar.gender}, with {creatingChar.eyeColor} eyes, standing at a {creatingChar.height} height. Your hair color is {creatingChar.hairColor} with a(n) __________ skin color.")
    creatingChar.skinColor = selectFromList(skinColorsPossible)
    sleep(1)
    
    # Conclusion
    clear()
    print(f"You are a {creatingChar.gender}, with {creatingChar.eyeColor} eyes, standing at a {creatingChar.height} height. Your hair color is {creatingChar.hairColor} with a(n) {creatingChar.skinColor} skin color.")
    print("Please read the above data. The screen will clear in 10 seconds.")
    sleep(10)
    return creatingChar

def save(yourCharacterClass):
    '''
    Saves your character to a .txt file, as well as current turn, etc.

    :param yourCharacterClass: The "character" object, contains physical traits as well as statistics.
    '''
    baseDir = os.path.dirname(os.path.abspath(__file__))
    savesDir = os.path.join(baseDir, "Characters (Saves)")
    savePath = os.path.join(savesDir, f"{yourCharacterClass.name}.txt")

    print("Would you like to save your adventure?")
    print("[1] Yes")
    print("[2] No")

    choice = getInput(2)
    sleep(0.25)

    if choice == 1:
        with open(savePath, "w", encoding="utf-8") as file:
            file.write(yourCharacterClass.name + "\n")
            file.write(yourCharacterClass.gender + "\n")
            file.write(yourCharacterClass.hairColor + "\n")
            file.write(yourCharacterClass.eyeColor + "\n")
            file.write(yourCharacterClass.skinColor + "\n")
            file.write(yourCharacterClass.height + "\n")

            file.write(str(yourCharacterClass.strength) + "\n")
            file.write(str(yourCharacterClass.intellect) + "\n")
            file.write(str(yourCharacterClass.dexterity) + "\n")
        
        clear()
    
    else:
        print("Nothing has been saved.")
        clear()

def load() -> object:
    '''
    Loads a character. Note that it will read in the data in the same direction of saving it.
    
    :return character: A character loaded from the /saves folder
    '''

    baseDir = os.path.dirname(os.path.abspath(__file__))
    savesDir = os.path.join(baseDir, "Characters (Saves)")

    # Ensure saves directory exists and collect .txt files
    if not os.path.exists(savesDir):
        print("No saves directory found.")
        return None

    saveFiles = [f for f in os.listdir(savesDir) if f.lower().endswith('.txt')]
    if not saveFiles:
        print("No saved characters found.")
        return None

    # Print available saves (without the .txt extension)
    print("Select a saved character:")
    for idx, fileName in enumerate(saveFiles):
        nameOnly = os.path.splitext(fileName)[0]
        print(f"[{idx + 1}] {nameOnly}")

    # Let the user pick one using existing getInput()
    choice = getInput(len(saveFiles))
    selectedFile = saveFiles[choice - 1]
    selectedPath = os.path.join(savesDir, selectedFile)

    # Read the save file and reconstruct a character
    creatingChar = character()
    try:
        with open(selectedPath, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        if len(lines) >= 1:
            creatingChar.name = lines[0]
        if len(lines) >= 2:
            creatingChar.gender = lines[1]
        if len(lines) >= 3:
            creatingChar.hairColor = lines[2]
        if len(lines) >= 4:
            creatingChar.eyeColor = lines[3]
        if len(lines) >= 5:
            creatingChar.skinColor = lines[4]
        if len(lines) >= 6:
            creatingChar.height = lines[5]

        # Stats (optional if not present)
        if len(lines) >= 7:
            try:
                creatingChar.strength = int(lines[6])
            except Exception:
                creatingChar.strength = 0
        if len(lines) >= 8:
            try:
                creatingChar.intellect = int(lines[7])
            except Exception:
                creatingChar.intellect = 0
        if len(lines) >= 9:
            try:
                creatingChar.dexterity = int(lines[8])
            except Exception:
                creatingChar.dexterity = 0

    except Exception as e:
        print(f"Failed to load save: {e}")
        return None

    # Print character summary in same format as createCharacter()
    clear()
    print(f"You are a {creatingChar.gender}, with {creatingChar.eyeColor} eyes, standing at a {creatingChar.height} height. Your hair color is {creatingChar.hairColor} with a(n) {creatingChar.skinColor} skin color.")
    sleep(1)
    return creatingChar

def pullChapter(chapter: str, fileName: str, char: character):
    '''
    Reads in the chapter, printing it out. Replaces all of the variable names with the correct variable from your character

    :param chapter: The name of the chapter needed 
    :param fileName: The file name of the needed variation (chapterOne.txt would be passed in as chapterOne)
    :param char: The character class. 
    '''
    baseDir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(baseDir, "Chapters", chapter, f"{fileName}.txt")

    lines = []
    try:
        # Pull in the chapter
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                lines.append(line.strip())
        
        traits = ["{name}", "{gender}", "{hairColor}", "{eyeColor}", "{skinColor}", "{height}", "{strength}", "{intellect}", "{dexterity}", "{health}"]
        charVars = [char.name, char.gender, char.hairColor, char.eyeColor, char.skinColor, char.height, str(char.strength), str(char.intellect), str(char.dexterity), str(char.health)]

        iteration = 0
        for trait in traits:
            for i, Line in enumerate(lines):
                lines[i] = Line.replace(trait, charVars[iteration])
            iteration += 1

        for line in lines:
            print(line)
            sleep(1)
    except FileNotFoundError as e:
        print(f"Could not open file: {e}")
