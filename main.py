'''
    Filename: main.py
    Date:     8/30/2019
    Purpose:  Start all threads
'''

import threading
import queue
import decision_machine
import gui
import state_machine

queueLock = threading.Lock()

# Start all of the threads


def main():

    maingui = gui.Gui()
    statemachine = state_machine.StateMachine()

    maingui.start()
    statemachine.start()

    maingui.end()
    statemachine.end()
# End main


if __name__ == "__main__":
    main()
