"""
Author: Abdullah Khan
File: PCB.py
Description: The PCB class implements the Process Control Block.
The PCB includes:
    process state
    process number (PID)
    memory address, etc.
"""

import random # to generate memory address
import re  # regex for matching strings

"""
PCB class definiton.
"""


class ProcessControlBlock:
    def __init__(self):
        self.pid = None
        self.state = None
        self.memstart = None
        self.rw = None
        self.file = None
        self.file_length = None

    def get_PID(self):
        return self.pid

    def get_state(self):
        return self.state

    def get_memstart(self):
        return self.memstart

    def get_filename(self):
        return self.file

    def get_file_length(self):
        return self.file_length

    def get_rw(self):
        return self.rw

    def set_state(self, new_state):
        self.state = new_state

    def set_memstart(self):
        self.memstart = random.randint(100, 32000)

    def set_PID(self):
        self.pid = random.randint(2, 300)

    def set_rw(self, operation):
        return  # come back later and add the regex stuff