import keyboard
import os
import choices
from time import sleep

global choiceIndex = 0

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
    selection = items[choice]

    return selection

def getInput(options: int) -> int:
    '''
    :param options: The amount of options, with the maximum of 10. (Buttons 1-0 on keyboard.)
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


# game start

# add possible call to start music.

introduction()

sleep(3)
selection = selectFromList(dayStatus)
print(f"You: \"{selection}\"\n")
sleep(2)

if choiceIndex != 0:
   meetingInquiry()
choiceIndex = 0

print("You: \"Anyways, let us begin.\"\n")
sleep(1)
print("You: \"Tell me about...\"\n\n")

selection = selectFromList(firstQuestion)
print(f"You: \"{selection}\"\n")
sleep(2)
print("Gatsby: \"Yes, yes, let me think...\"\n")
sleep(2)

if choiceIndex == 0:
    pass
    #passion()
elif choiceIndex == 1:
    pass
    #ambition()
elif choiceIndex == 2:
    pass
    #greed()

