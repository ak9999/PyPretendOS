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
                self.cpu.append(self.rq.popleft())
            except IndexError:
                print("ReadyQueue is empty.")

    def remove(self):
        if self.cpu_is_empty():
            print("No process to terminate!")
            return
        else:
            self.cpu.pop()
            if not self.queue_is_empty():
                self.add(self.rq.popleft())
        return

    def print_queue(self):
        self.print_cpu()
        print("Ready Queue")
        print("PID\tMemstart CPU Time\tBurst")
        for blocks in self.rq:
            blocks.print_ready()


    def print_cpu(self):
        print("Current job in CPU")
        print("PID\tCPU Time\tBurst")
        try:
            string = ("%s\t%s\t%s"
                      % (str(self.cpu[0].pid).rjust(3),
                         str(self.cpu[0].cpu_total).rjust(8),
                         str(self.cpu[0].avg_burst).rjust(3)))
            print(string)
        except IndexError:
            return

    def sjf_sort(self, alpha, tau):
        ready_list = list(self.rq)
        for pcb in range(1, len(ready_list)):
            if ready_list[pcb-1].cpu_total < ready_list[pcb].cpu_total:
                ready_list[pcb-1], ready_list[pcb] = ready_list[pcb], ready_list[pcb-1]
            elif ready_list[pcb-1].cpu_total == ready_list[pcb].cpu_total:
                ready_list[pcb-1].pid, ready_list[pcb].pid = ready_list[pcb], ready_list[pcb-1]
