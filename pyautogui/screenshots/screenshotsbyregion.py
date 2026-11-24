import os
import pyautogui
from time import sleep

path_string = ""
# Exact region of the element to capture (uses the coordinate reading)
X_ELEM = 100
Y_ELEM = 200
WIDTH = 80
HEIGHT = 40
REF_NAME = 'reference_b'
if X_ELEM is None:
    print('Fill in X_ELEM, Y_ELEM with coordinates!')
    exit()
desktop = path_string
path = os.path.join(desktop, f'{REF_NAME}.png')
print(f'Region: ({X_ELEM}, {Y_ELEM}), {WIDTH}x{HEIGHT}px')
print('Capturing in 3 seconds...')
sleep(3)
region = (X_ELEM, Y_ELEM, WIDTH, HEIGHT)
image = pyautogui.screenshot(region=region)
image.save(path)
if os.path.exists(path):
    print(f'Reference saved: {path}')
    print(f'Dimensions: {image.size[0]}x{image.size[1]}px')
    print(f'Size: {os.path.getsize(path):,} bytes')
else:
    print('Error saving the reference image.')
    exit()