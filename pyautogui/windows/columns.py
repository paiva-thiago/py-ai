import pyautogui
import time
import pygetwindow as gw


WIDTH, HEIGHT = pyautogui.size()  # e.g.: (1920, 1080)
MARGIN = 10
COL_WIDTH = (WIDTH - MARGIN * 4) // 3  # 3 columns with margins: 626
COL_HEIGHT = HEIGHT - 80  # space for the taskbar: 1000
# Position of each column:
x_col1 = MARGIN  # 10
x_col2 = MARGIN + COL_WIDTH + MARGIN  # 646
x_col3 = MARGIN + (COL_WIDTH + MARGIN) * 2  # 1282

TOLERANCE = 30  # px of deviation before reorganizing
def find_window(titles):
    for t in titles:
        ws = gw.getWindowsWithTitle(t)
        if ws: return ws[0]
    return None

def out_of_place(w, x_exp, y_exp, w_exp, h_exp, tol):
    return (abs(w.left-x_exp)>tol or abs(w.top-y_exp)>tol 
      or abs(w.width-w_exp)>tol or abs(w.height-h_exp)>tol)

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
        if win and not win.isMinimized and out_of_place(win, x, y, w, h, TOLERANCE):
            win.restore(); 
            win.activate(); 
            win.moveTo(x, y); 
            win.resizeTo(w, h)
    sleep(2.0)