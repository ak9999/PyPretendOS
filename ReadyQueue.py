"""
Author: Abdullah Khan
File: ReadyQueue.py
Description: It's just a queue that will hold PCBs.
"""

from collections import deque
from PCB import ProcessControlBlock

class ReadyQueue:
    def __init__(self):
        self.rq = deque()

    def add(self, other):
        other.set_state("READY")
        self.rq.append(other)

