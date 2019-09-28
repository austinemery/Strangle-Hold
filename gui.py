# =============================================================================
# Name: gui.py
# Date Created: 9/28/2019
# Purpose: Define a gui class for the Strangle Hold
# =============================================================================

# =============================================================================
# IMPORTS
# =============================================================================

import tkinter as tk
import threading

# =============================================================================
# GLOBALS
# =============================================================================

# =============================================================================
# CLASS DEFINITIONS
# =============================================================================

class Gui:

    def __init__(self):
        self.thread = threading.Thread(target=self.guithread)
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Hello, World!")
        self.label.pack()

    def start(self):
        self.thread.start()

    def end(self):
        self.thread.join()

    def guithread(self):
        print("Started GUI Thread")

        self.root.mainloop()
