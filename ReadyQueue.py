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

    def add(self, other):
        #other.set_state("READY")  # Set process state
        self.rq.append(other)  # Now we can add it!

    def is_empty(self):
        if self.rq: #  If the deque is not empty
            return False
        else:
            return True

    def remove(self):
        if self.is_empty():
            print("No processes to remove!", end="\n")
        else:
            try:  # We should only ever need to try once.
                return self.rq.popleft()
            except IndexError:  # We have a serious problem if this happens.
                print("No processes to remove from queue???", end="\n")

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
             %  ( \
                str(blocks.get_pid()),
                str(blocks.get_filename()),
                str(blocks.get_memstart()),
                str(blocks.get_rw()),
                str(blocks.get_filelength())
                )
            )
