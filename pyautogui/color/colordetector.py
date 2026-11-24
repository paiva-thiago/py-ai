import pyautogui, time
from time import sleep

def get_mouse_color_info():
    """Return the current mouse pixel's color as a formatted string."""
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    return f'RGB: ({r},{g},{b})  HEX: #{r:02X}{g:02X}{b:02X}'
    
print(get_mouse_color_info())
interactions=0
try:
    while True:
        print(get_mouse_color_info())
        sleep(1)
        interactions+=1
except KeyboardInterrupt:
    print("Stopped by user.")

print(f"Total color checkings: {interactions}")
