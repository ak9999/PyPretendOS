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
In the C++ STL they just call it 'front' and 'back' like normal human beings.
"""

class ReadyQueue(object):
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
        if not other == None:
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
        if self.cpu_is_empty() and not self.queue_is_empty():
            try:
                self.cpu.append(self.rq[0])
                self.rq.popleft()
                self.size -= 1
            except IndexError:
                print("No processes to add!", end="\n")
        else:
            try:  # We should only ever need to try once.
                self.cpu.pop()
                self.size -= 1
            except IndexError:  # We have a serious problem if this happens.
                print("No processes!", end="\n")

    def print_queue(self):
        print("Ready Queue")
        print("PID\t Filename\t Memstart\t R/W\t File Length\t")
        for blocks in self.rq:
            print(blocks)
