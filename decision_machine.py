'''
    Filename: decision_machine.py
    Date: 8/10/2019
    Purpose: The main file for the decision machine thread.

    -----------------------------------------------------
    Version     Date        Author      Description
    -----------------------------------------------------
    <0.1>       8/10/19     A. Emery
'''

from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('bin/test_image_1.png')))
