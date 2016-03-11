"""
Author: Abdullah Khan
File: CPU.py
Description: CPU class implementation
"""

from collections import deque
from ReadyQueue import ReadyQueue
import ProcessControlBlock as PCB

class CPU(ReadyQueue):
    """
    CPUs can only have one job at a time.
    I want to be able to move PCBs from the ready queue to the CPU.
    """
    def __init__(self):
        self.cpu = deque(maxlen=1) # CPUs can only work on one process!
        self.rq = ReadyQueue()

    def is_empty(self):
        if self.cpu: # If the CPU is in use
            return False
        else:
            return True

    def add(self, other):
        if self.is_empty:
            self.cpu.append(self.rq.remove())
        else:
            self.rq.add(other)

    def remove(self):
        if self.is_empty():
            print("Nothing to remove!", end="\n")
        else:
            self.cpu.pop()
            if self.rq.is_empty():
                print("No more processes in queue.", end="\n")
                self.add(self.rq.remove())

    def to_printer(self):
        self.cpu.set_rw("w")

    def readwrite(self):
        print("Read or write? (r/w): ", end=" ")
        answer = input().strip()
        if(answer.lower() == "r"):
            self.cpu.set_rw("r")
        else:
            self.cpu.set_rw("w")