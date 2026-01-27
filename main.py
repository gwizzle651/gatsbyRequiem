import ensurepip
import keyboard
import subprocess
import sys
import os
import words
from time import sleep
from words import dayStatus, firstQuestion
from adventureLib import character, clear, selectFromList, pullChapter

choiceIndex = 0

# Installs
def ensurePip():
    '''Attempts to ensure that pip is installed.\n
    Uses ensurepip.bootstrap() and then get-pip methods.'''
    try:
        import pip  # noqa: F401
    except ImportError:
        try:
            ensurepip.bootstrap()
        except Exception:
            try:
                import urllib.request
                url = "https://bootstrap.pypa.io/get-pip.py"
                with urllib.request.urlopen(url) as response:
                    script = response.read()
                exec(script, {'__name__': '__main__'})
            except Exception as e:
                print(f"Failed to install pip using any method: {e}")
                sys.exit(1)

def install(package):
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-qqq",
        package])


pkgs = {"keyboard"}

for pkg in pkgs:
    try:
        import keyboard
    except Exception:
        try:
            install(pkg)
        except Exception as e:
            print(f"Could not install {pkg}: {e}")
            sys.exit(1)

import keyboard
# game start
player = character("Owl Eyes", "Male", height="short")
meetingOptions = ["One more haul", "Row towards it"]
stage = "intro"
# add possible call to start music.
for i in range(3):
    pullChapter("Introduction", "introduction", player)

    # Introduction
    sleep(3)
    choiceIndex = selectFromList(dayStatus)
    clear()
    print(f"You: \"{choiceIndex}\"\n")
    sleep(2)
    # If the user decides to ask about Gatsby, A brief dialouge will proceed
    if choiceIndex != dayStatus[0]:
       pullChapter("Introduction", "meetingInquiry", player)
       print("You: \"Anyways, let us begin.\"\n")
    else:
        print("YOU: Tell me about how all this began.\n")
    choiceIndex = ""

    # Start of inquiry
    sleep(2)
    print("Gatsby: \"Yes, yes, let me think...\"\n")
    sleep(2)
    pullChapter("Meeting", "meeting0", player)
    initialChoices = ["One more haul", "Return Home"]
    choiceIndex = selectFromList(initialChoices)
    if choiceIndex == initialChoices[1]:
        clear()
        pullChapter("Meeting", "returnHome", player)
        sys.exit()

    clear()
    iteration = 1
    while iteration != 5:
        pullChapter("Meeting", f"meeting{iteration}", player)
        choiceIndex = selectFromList(meetingOptions)
        if choiceIndex == meetingOptions[0]:
            iteration += 1
            clear()
        else:
            clear()
            pullChapter("Meeting", "row", player)
            stage = "greed"
            break

    if iteration == 5 and stage != "greed":
        pullChapter("Meeting", "meeting5", player)
        sys.exit()

    sleep(5)
# ---------------------
# GREED (Chapters/Traits/Greed/greed0.txt)
# ---------------------
    greedChoices = ["Get involved", "Stay Honest", "Be a hero?"]
    clear()
    pullChapter("Traits/Greed", "greed0", player)
    choiceIndex = selectFromList(greedChoices)
    if choiceIndex == greedChoices[0]:
        pullChapter("Traits/Greed", "involved", player)
        stage = "passionA"
        clear()
    elif choiceIndex == greedChoices[1]:
        pullChapter("Traits/Greed", "honesty", player)
        stage = "passionB"
        clear()
    else: 
        pullChapter("Traits/Greed", "hero", player)
        sleep(5)
        sys.exit()
    
    sleep(5)

# ---------------------
# PASSION (Chapters/Traits/Passion ({letter})/passion.txt)
# ---------------------
    passionChoices = ["Back down", "Stand up"]
    if stage == "passionA":
        pullChapter("Traits/Passion (A)", "passion", player)
        choiceIndex = selectFromList(passionChoices)
        clear()
        if choiceIndex == passionChoices[0]:
            pullChapter("Traits/Passion (A)", "backDown", player)
            sleep(5)
            clear()
        else:
            pullChapter("Traits/Passion (A)", "standUp", player)
            sleep(5)
            clear()
    else:
        pullChapter("Traits/Passion (B)", "passion", player)
        choiceIndex = selectFromList(passionChoices)
        clear()
        if choiceIndex == passionChoices[0]:
            pullChapter("Traits/Passion (B)", "backDown", player)
            sleep(5)
            clear()
        else:
            pullChapter("Traits/Passion (B)", "standUp", player)
            sleep(5)
            clear()

stage = "desire"
# ---------------------
# Desire (Chapters/Traits/Desire/desire0.txt)
# ---------------------
pullChapter("Traits/Desire", "desire", player)
sleep(5)
clear()
pullChapter("Conclusion", "end", player)
sleep(30)