import os
import pyautogui
import pyperclip
from time import sleep
from datetime import datetime

now = datetime.now()
date_time = now.strftime('%d/%m/%Y %H:%M:%S')
day_of_week= now.strftime('%A')

print (f"Today is {day_of_week}, {date_time}!")
