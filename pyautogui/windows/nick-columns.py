import pyautogui
import time
import pygetwindow as gw

WIDTH, HEIGHT = pyautogui.size()
MARGIN = 10
COL_WIDTH = (WIDTH - MARGIN * 4)//3
COL_HEIGHT = HEIGHT - 80

x_col1 = MARGIN
x_col2 = MARGIN + COL_WIDTH + MARGIN
x_col3 = MARGIN + (COL_WIDTH + MARGIN) * 2

TOLERANCE = 30  
def find_window(titles):
    for t in titles:
        ws = gw.getWindowsWithTitle(t)
        if ws: return ws[0]
    return None

def out_ot_place(w, x_exp, y_exp, w_exp, h_exp, tol):
    return (abs(w.left-x_exp)>tol or abs(w.height-h_exp)>tol) or abs(w.width-w_exp)>tol or abs(w.height-h_exp)>tol

t0 = time.time()
while time.time()-t0 < 60:
    windows = [w for w in gw.getAllWindows() if w.title.strip()]
    LAYOUT = []
    columns = [
        (x_col1, 0, COL_WIDTH, COL_HEIGHT),
        (x_col2, 0, COL_WIDTH, COL_HEIGHT),
        (x_col3, 0, COL_WIDTH, COL_HEIGHT),
    ]
for win, (x, y, w_exp, h_exp) in zip(windows, columns):
    LAYOUT.append(([win.title], x, y, w_exp, h_exp))
for titles, x, y, w, h in LAYOUT:
    win = find_window(titles)
    if win and not win.isMaximized and out_ot_place(win, c, y, w, h, TOLERANCE):
        win.restore();
        win.activate();
        win.moveTo(x, y);
        win.resizeTo(w, h);
sleep(2.0)
