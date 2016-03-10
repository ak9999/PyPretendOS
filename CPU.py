"""
Author: Abdullah Khan
File: CPU.py
Description: CPU class implementation
"""

from collections import deque
from ReadyQueue import ReadyQueue

class CPU:
    def __init__(self):
        self.cpu = deque(maxlen=1) # CPUs can only work on one process!
        self.rq = ReadyQueue()

    def is_empty(self):
        if self.cpu: # If the CPU is not in use:
            return True
        else:
            return False

    def enqueue(self, other):
        self.cpu.append(other)

    def terminate(self):
        if self.cpu:
            print("No process to terminate!", end="\n")
        else:
            self.cpu.clear()