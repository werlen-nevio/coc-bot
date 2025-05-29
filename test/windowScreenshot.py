import cv2
import pygetwindow as gw
import pyautogui
import time
import numpy as np

def get_window_screenshot(title):
    window_title = "Clash of Clans"
    win = next((w for w in gw.getWindowsWithTitle(window_title) if not w.isMinimized), None)
    if not win:
        raise Exception(f'Fenster mit Titel "{title}" nicht gefunden.')

    win.activate()
    time.sleep(0.5)

    left, top, width, height = win.left, win.top, win.width, win.height
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    return img