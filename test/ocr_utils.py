import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getGoldValue(image_path="test/img/screenshot.png"):
    img = cv2.imread(image_path)

    x, y, w, h = 60, 120, 260, 60
    crop = img[y:y+h, x:x+w]

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite("debug_gold_thresh.png", thresh)

    config = '--psm 6 -c tessedit_char_whitelist=0123456789 '
    text = pytesseract.image_to_string(thresh, config=config)

    text = text.replace(" ", "").strip()
    digits = ''.join(filter(str.isdigit, text))

    return int(digits) if digits else None
