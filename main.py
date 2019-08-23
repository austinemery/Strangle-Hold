# Pyglet
# python threads
# py tesseract

import threading
import queue
import decision_machine
import gui
import state_machine

queueLock = threading.Lock()

# Start all of the threads


def main():

    data_queue = queue.Queue()

    state_thread = threading.Thread(target=state_machine.run, args=(data_queue, queueLock))
    state_thread.start()

    queueLock.acquire()
    data_queue.put('bin/test_image_1.png')
    queueLock.release()

    state_thread.join()
# End main


if __name__ == "__main__":
    main()
