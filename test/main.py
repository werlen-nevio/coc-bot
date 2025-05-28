from ocr_utils import getGoldValue

gold = getGoldValue()

if gold is not None:
    print(f"Goldwert erkannt: {gold}")
else:
    print("❌ Kein Goldwert erkannt.")
