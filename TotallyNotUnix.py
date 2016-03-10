"""
Author: Abdullah Khan
File: TotallyNotUnix.py
Description: This is what actually runs.
"""

import PretendSystem
import ReadyQueue
import CPU
import PCB

"""
This is the actual "Operating System" that calls all the other
functions.
"""

class TotallyNotUnix:
    def __init__(self):
        self.cpu = CPU
        self.rq = ReadyQueue
        #  Python doesn't have switch-cases so we can just create a dictionary
        #  of values we expect and map them to functions.
        self.options = { 'A' : self.arrival(),
                         't' : self.terminate(),
                         'S' : self.snapshot() }

    def arrival(self):
        new_process = PCB.ProcessControlBlock

    def terminate(self):
    def snapshot(self):