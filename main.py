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
# add possible call to start music.

pullChapter("Introduction", "introduction", player)

sleep(3)
selection = selectFromList(dayStatus)
print(f"You: \"{selection}\"\n")
sleep(2)
clear()
if choiceIndex != 0:
   pullChapter("Introduction", "meetingInquiry", player)
choiceIndex = 0

print("You: \"Anyways, let us begin.\"\n")
sleep(1)
clear()
print("You: \"Tell me about...\"\n\n")

selection = selectFromList(firstQuestion)
print(f"You: \"{selection}\"\n")
sleep(2)
print("Gatsby: \"Yes, yes, let me think...\"\n")
sleep(2)

# TODO Code in the options here for choices. The introduction should be complete before this.
if choiceIndex == 0:
    pullChapter("Passion", "passion", player)
elif choiceIndex == 1:
    pullChapter("Ambition", "ambition", player)
elif choiceIndex == 2:
    pullChapter("Greed", "greed", player)

