import os
import pyautogui
import pyperclip
from time import sleep
from datetime import datetime

print("Taking the picture in 3 seconds...")
sleep(3)
try:
    str_now =  datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    file_name = f'screenshot_{str_now}.png'
    image = pyautogui.screenshot()
    path_string = ""
    full_path = os.path.join(path_string, file_name)


    image.save(full_path)
    print(full_path + ' saved with success!')
except Exception as e:
    print(f"Critical error!{e}")
