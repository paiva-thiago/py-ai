# Check if the window is NOT maximized,
#  1. if it is true, maximize it
#  2. Otherwise, restore it and resize to 400x400 and move it to 250, 300
#  3. In all cases activate the window.
#  4. Use a sleep for 1 - sleep(1)
# You will use:
# not(window.isMaximized)
# window.restore()
# window.maximize()
# window.moveTo(x, y)
# window.resizeTo(w,h)
# window.activate()
# sleep(1)
import pygetwindow as gw
from time import sleep
# 1. Find the window
windows = gw.getWindowsWithTitle("Note - Bloco de notas")
if not windows:
 print("Not found"); exit()
window = windows[0]