from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('bin/test_image_1.png')))
