"""
Author: Abdullah Khan
File: ReadyQueue.py
Description: It's just a queue that will hold PCBs.
"""
import traceback
from collections import deque
from PCB import ProcessControlBlock

"""
Information about Python 3's deques (pronounced 'decks'):
https://docs.python.org/3.3/library/collections.html#collections.deque
We append to the right side of the queue, but pop from the left side.
The left side is the 'front' of the queue.
"""


class ReadyQueue:
    def __init__(self):
        self.rq = deque()  # Just make a deque.
        self.cpu = deque(maxlen=1)
        self.banner = (" " * 4).join(["PID", "CPU Time", "# Bursts", "\t\tAVG"])

    def queue_is_empty(self):
        if self.rq:
            # Empty
            return False
        else:
            # Not empty
            return True

    def cpu_process(self):
        if self.cpu:
            # No job in CPU
            return False
        else:
            # CPU has job
            return True

    def add(self, other=None):
        if other is not None:
            self.rq.append(other)
            #  Lambdas are great.
            self.rq = deque(sorted(self.rq, key=lambda pcb: pcb.pid))
            self.rq = deque(sorted(self.rq, key=lambda pcb: pcb.total_cpu_time))
        else:
            print("Nothing was added.")
        if self.cpu_process():
            try:
                self.cpu.append(self.rq.popleft())
            except IndexError:
                print("ReadyQueue is empty.")
            except AttributeError:
                traceback.print_exc()

    def remove(self):
        if self.cpu_process():
            print("No process to terminate!")
            return
        else:
            self.cpu.popleft()
            if not self.queue_is_empty():
                self.cpu.append(self.rq[0])
                self.rq.popleft()
        return

    def print_queue(self):
        try:
            print(self.banner)
            print("CPU")
            try:
                print(self.cpu[0].print_ready_queue())
            except IndexError:
                print(end='')
            print("Ready Queue")
            for pcb in self.rq:
                pcb.print_ready_queue()
        except AttributeError:
            traceback.print_exc()
