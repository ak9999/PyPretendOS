"""
Author: Abdullah Khan
File: ReadyQueue.py
Description: It's just a queue that will hold PCBs.
"""

from collections import deque

"""
Information about Python 3's deques (pronounced 'decks'):
https://docs.python.org/3.3/library/collections.html#collections.deque
We append to the right side of the queue, but pop from the left side.
The left side is the 'front' of the queue.
Why don't they just use front and back like everybody else?
Why don't they include a empty() function to check if it's empty?
"""


class ReadyQueue:
    def __init__(self):
        self.rq = deque()  # Just make a deque.
        self.size = 0
        self.cpu = deque(maxlen=1)

    def queue_is_empty(self):
        if self.rq:  # If the deque is not empty
            return False
        else:
            return True

    def cpu_is_empty(self):
        if self.cpu:  # If the deque is not empty
            return False
        else:
            return True

    def add(self, other=None):
        if other is not None:
            self.rq.append(other)
            self.size += 1
        else:
            print("Nothing was added.")
        if self.cpu_is_empty():
            try:
                self.cpu.append(self.rq[0])
                self.rq.popleft()
            except IndexError:
                print("ReadyQueue is empty.")

    def remove(self):
        if self.cpu_is_empty():
            print("No process to terminate!")
            return
        else:
            self.cpu.pop()
            if not self.queue_is_empty():
                self.add(self.rq[0])
                self.rq.popleft()
        return

    def print_queue(self):
        self.print_cpu()
        print("Ready Queue")
        print("PID\t Memstart\t File Length\t")
        for blocks in self.rq:
            blocks.print_ready()

    def print_cpu(self):
        print("Current job in CPU")
        print("PID\t Memstart\t File Length\t")
        try:
            print(self.cpu[0])
        except IndexError:
            return
