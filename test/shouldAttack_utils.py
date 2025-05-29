import pytesseract
import cv2
from windowScreenshot import get_window_screenshot

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getResourceValue(resource_type):
    window_title = "Clash of Clans"
    img = get_window_screenshot(window_title)

    if resource_type == "gold":
        x, y, w, h = 60, 120, 260, 60
    elif resource_type == "elixir":
        x, y, w, h = 60, 170, 260, 60
    elif resource_type == "dark_elixir":
        x, y, w, h = 60, 220, 260, 60
    else:
        raise ValueError("Invalid resource type. Choose from 'gold', 'elixir', or 'dark_elixir'.")
    
    crop = img[y:y+h, x:x+w]

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY_INV)

    config = '--psm 6 -c tessedit_char_whitelist=0123456789 '
    text = pytesseract.image_to_string(thresh, config=config)

    text = text.replace(" ", "").strip()
    digits = ''.join(filter(str.isdigit, text))

    return int(digits) if digits else None

def shouldAttack():
    gold = getResourceValue("gold")
    elixir = getResourceValue("elixir")
    dark_elixir = getResourceValue("dark_elixir")
    bShouldAttack = False
    
    if gold is None or elixir is None or dark_elixir is None:
        return False

    if gold >= 500000 and elixir >= 500000 and dark_elixir >= 6000:
        bShouldAttack = True

    if gold >= 300000 and elixir >= 1000000 and dark_elixir >= 6000:
        bShouldAttack = True

    if gold >= 1000000 and elixir >= 300000 and dark_elixir >= 6000:
        bShouldAttack = True

    if gold >= 300000 and elixir >= 300000 and dark_elixir >= 10000:
        bShouldAttack = True

    return bShouldAttack