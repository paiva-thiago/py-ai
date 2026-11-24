
import pyautogui

def describe_box(box):
    if box is None:
        print("None")
    else:
        print(f"Box(left={box.left}, top={box.top}, width={box.width}, height={box.height})")

def describe_point(point):
    if point is None:
        print("None")
    else:
        print(f"Point(x={point.x}, y={point.y})")

loc = pyautogui.locateOnScreen('reference.png', confidence=0.9)
describe_box(loc)

locCenter = pyautogui.locateCenterOnScreen('reference.png', confidence=0.9)
describe_point(locCenter)

allReferences = list(pyautogui.locateAllOnScreen('reference.png', confidence=0.9))
for ref in allReferences:
    describe_box(ref)
