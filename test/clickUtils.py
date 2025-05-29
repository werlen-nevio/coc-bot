import pygetwindow as gw
import pyautogui
import time
from shouldAttack_utils import shouldAttack

window_title = "Clash of Clans"
win = next((w for w in gw.getWindowsWithTitle(window_title) if w.isActive or not w.isMinimized), None)

def clickAt(xCord, yCord):
    if win:
        time.sleep(0.5)

        x = win.left + xCord
        y = win.top + yCord

        pyautogui.moveTo(x, y)
        pyautogui.click()
    else:
        print(f"Window with title '{window_title}' not found.")

def fullScreen():
    window_title = "Clash of Clans"
    win = next((w for w in gw.getWindowsWithTitle(window_title) if not w.isMinimized), None)

    win.activate()
    win.restore()
    win.maximize()

    time.sleep(1)

def homeSearchAttack():
    clickAt(100, 900)
    clickAt(1400, 600)

    # Wait until game is ready
    # TODO - Implement a more robust check for game readiness
    time.sleep(5)

    if shouldAttack():
        print("Attack initiated.")
    else:
        print("No attack initiated. Conditions not met.")