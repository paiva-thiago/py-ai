# This library will be needed:
# pip install pygetwindow

import pygetwindow as gw
from time import sleep
# 1. Find the window
windows = gw.getWindowsWithTitle("Note - Bloco de notas")
if not windows:
 print("Not found"); exit()
window = windows[0]
# 2. Restore before moving/resizing
window.restore()
sleep(0.3)
# 3. Activate (bring to front)
window.activate()
sleep(0.3)
# 4. Move and resize
window.moveTo(100, 100)
sleep(0.3)
window.resizeTo(800, 600)
sleep(0.3)
print(f"Window: ({window.left},{window.top}) {window.width}x{window.height}px")
