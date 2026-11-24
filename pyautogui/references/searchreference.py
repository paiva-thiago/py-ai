import pyautogui, time
from time import sleep

def wait_for_element(img_path, timeout=60, interval=1.0, confidence=0.85):
    start_time = time.time()
    attempts = 0
    while True:
        elapsed = time.time() - start_time
        if elapsed > timeout:
            return None
        attempts += 1
        try:
            loc = pyautogui.locateOnScreen(img_path, confidence=confidence)
            if loc:
                center = pyautogui.center(loc)
                return center
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as e:
            print(f'Unexpected error: {e}')
        sleep(interval)
# Use
center = wait_for_element('reference.png', timeout=30)
if center:
    pyautogui.click(center.x, center.y)
else:
    print('Element did not appear in time.')