import os
import pyautogui
import pyperclip
from time import sleep


# 1 Open notepad, write 3 lines and save as 3rdclass.txt
# 2 Reopen 3rdclass.txt and add text with accents. (In english we do not have)
# 3 So, just write something like Código (word code in portuguese)

name = input("What's your name?")
age = input("How old are you?")
anything = input("What do you want to know?")

inputs = [
    name,
    age,
    anything
]

pyautogui.hotkey("win","r")
sleep(0.3)
pyautogui.write("notepad")
pyautogui.press("enter")
sleep(1.5)


for inp in inputs:
    pyautogui.write(inp, interval=0.05)
    pyautogui.press('enter')
    sleep(0.2)

pyperclip.copy("Parabéns")
pyautogui.hotkey("ctrl","v")
pyautogui.press('enter')
pyperclip.copy("Código")
pyautogui.hotkey("ctrl","v")

# This command below will force to close notepad!
os.system("taskkill /f /im notepad.exe")
    
