'''
    Filename: state_machine.py
    Date:     8/11/2019
    Purpose:  To control the state and transitions requirements for those states.

    -----------------------------------------------------
    Version     Date        Author      Description
    -----------------------------------------------------
    <0.1>       8/11/2019   A.Emery
'''

from PIL import Image
import pytesseract
import queue
import threading


def run(data_queue, lock):
    flag = True

    while flag:
        if not data_queue.empty():

            lock.acquire()
            name = data_queue.get()
            lock.release()
            print(pytesseract.image_to_string(Image.open(str(name))))
            flag = False

# End run
