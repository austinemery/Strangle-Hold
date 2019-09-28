# =============================================================================
# Name: gui.py
# Date Created: 8/11/2019
# Purpose: Define a gui class for the Strangle Hold
# =============================================================================

# =============================================================================
# IMPORTS
# =============================================================================

from PIL import Image
import pytesseract
import queue
import threading

# =============================================================================
# GLOBALS
# =============================================================================

# =============================================================================
# CLASS DEFINITION
# =============================================================================

class StateMachine:

    def __init__(self):
        self.thread = threading.Thread(target=self.statethread)

    def start(self):
        self.thread.start()

    def end(self):
        self.thread.join()

    def statethread(self):
        print(pytesseract.image_to_string(Image.open("bin/test_image_1.png")))
