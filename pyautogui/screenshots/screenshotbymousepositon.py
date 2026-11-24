import os
import pyautogui
import pyperclip
from time import sleep
from datetime import datetime

print("Let's take a picture limiting the region!")
print('Put the cursor on the top-left corner...')
sleep(3)
x1,y1 = pyautogui.position()

print('Put the cursor on the bottom-right corner...')
sleep(3)
x2,y2 = pyautogui.position()

width  = x2 - x1
height = y2 - y1

if width<=0 or height<=0:
    print('Invalid corners!')
    exit()

try:
    str_now =  datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    file_name = f'screenshot_4b_{str_now}.png'
    image = pyautogui.screenshot(region=(x1,y1,width,height))
    path_string = "C:\\Users\\Thiago Paiva\\OneDrive - sharkcoders\\20260915-python\\"
    full_path = os.path.join(path_string, file_name)


    image.save(full_path)
    print(full_path + ' saved with success!')
except Exception as e:
    print(f"Critical error!{e}")
