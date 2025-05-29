import pygetwindow as gw
import pyautogui
import time
from shouldAttack_utils import shouldAttack

window_title = "Clash of Clans"
win = next((w for w in gw.getWindowsWithTitle(window_title) if w.isActive or not w.isMinimized), None)

def clickAt(xCord, yCord):
    if win:
        win.activate()
        time.sleep(1)

        x = win.left + xCord
        y = win.top + yCord

        pyautogui.moveTo(x, y)
        pyautogui.click()
    else:
        print(f"Window with title '{window_title}' not found.")

def homeSearchAttack():
    clickAt(100, 900)
    clickAt(1400, 600)

    if shouldAttack():
        print("Attack initiated.")
    else:
        print("No attack initiated. Conditions not met.")