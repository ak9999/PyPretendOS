"""
Author: Abdullah Khan
File: PCB.py
Description: The PCB class implements the Process Control Block.
The PCB includes:
    process state
    process number (PID)
    memory address, etc.
"""

import random

"""
PCB class definiton.
"""


class ProcessControlBlock:
    def __init__(self, PID=0):
        self.pid = PID
        self.state = None
        self.memstart = None

    def get_PID(self):
        return self.pid

    def get_state(self):
        return self.state

    def get_memstart(self):
        return self.memstart

    def set_state(self, new_state):
        self.state = new_state

    def set_memstart(self):
        self.memstart = random.randint(100, 32000)

    def set_PID(self):
        self.pid = random.randint(2, 300)