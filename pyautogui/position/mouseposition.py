import pyautogui
import time

print("Click anywhere to log the position. Ctrl+C to stop.")
try:
    while True:
        x, y = pyautogui.position()
        if pyautogui.mouseDown():
            print(f"Clicked at: ({x}, {y})")
            time.sleep(0.3)   # avoid duplicate prints while button is held
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nDone.")