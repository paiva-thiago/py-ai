# Make the mouse go to the bottom of the screen
# Make the mouse go to the bottom right of the screen
# Make the mouse "draw" a square, moving it
import pyautogui
import time

pyautogui.PAUSE = 0.3

def openPaint():
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('mspaint')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('win', 'up')
    time.sleep(2)

def drawTheSquare():
    pyautogui.moveTo(400, 400)
    pyautogui.dragTo(800, 400, duration=0.8, button='left')
    pyautogui.dragTo(800, 600, duration=0.8, button='left')
    pyautogui.dragTo(400, 600, duration=0.8, button='left')
    pyautogui.dragTo(400, 400, duration=0.8, button='left')
    time.sleep(0.3)

def saveFile():
    pyautogui.hotkey('ctrl','s')
    time.sleep(2)
    pyautogui.write('square')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def restoreWindow():
    pyautogui.hotkey('win', 'up')
    time.sleep(1)
    pyautogui.moveTo(5,5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

def exitPaint():
    pyautogui.hotkey('alt', 'f4')

openPaint()
drawTheSquare()
saveFile()
#restoreWindow()
#exitPaint()
