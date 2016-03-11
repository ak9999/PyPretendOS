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

"""
ReadyQueue has to take an `object` parameter, so that it can handle the PCBs.
Surprisingly, I don't have to include the ProcessControlBlock class at the top
of the file like you would do in other languages like C and C++.
"""

class ReadyQueue(object):
    def __init__(self):
        self.rq = deque()  # Just make a deque.
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
        #other.set_state("READY")  # Set process state
        if not self.cpu:
            try:
                self.cpu.append(self.rq.popleft())
            except IndexError:
                print("Nothing to add!")
        else:
            if other == None:
                return
            else:
                self.rq.append(other)

    def remove(self):
        if self.cpu_is_empty() and not self.queue_is_empty():
            try:
                self.cpu.append(self.rq.popleft())
            except IndexError:
                print("No processes to add!", end="\n")
        else:
            try:  # We should only ever need to try once.
                self.cpu.pop()
            except IndexError:  # We have a serious problem if this happens.
                print("No processes!", end="\n")

    """
    __str__: a standard function provided by Python to convert an object to
    a string for printing.
    I'm using this so that I can just call print(ReadyQueue)
    """
    def __str__(self):
        print("Ready Queue")
        print()
        for blocks in self.rq:
            print \
            ("%s\t %s\t %s\t %s\t %s\t"
             %  (
                str(blocks.get_pid()),
                str(blocks.get_filename()),
                str(blocks.get_memstart()),
                str(blocks.get_rw()),
                str(blocks.get_filelength())
                )
            )
        return
