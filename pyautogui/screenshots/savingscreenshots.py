import os, pyautogui
from time import sleep

X_ELEM, Y_ELEM = 100, 200
WIDTH, HEIGHT = 80, 40

file_name= "../references/reference.png"
image = pyautogui.screenshot()
path_string = ""
full_path = os.path.join(path_string, file_name)
print('Capturing it in 3 seconds...')
sleep(3)
imagem = pyautogui.screenshot(region=(X_ELEM, Y_ELEM, WIDTH, HEIGHT))
imagem.save(full_path)
print(f'Reference stored: {full_path}')