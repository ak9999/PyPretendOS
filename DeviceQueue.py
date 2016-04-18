"""
Author: Abdullah Khan
File: CPU.py
Description: CPU class implementation
"""

from collections import deque

"""
This is the generic device queue that will be inherited by the actual devices.
"""


class DeviceQueue:
    def __init__(self):
        self.q = deque()
        self.number = None
        self.device_name = None

    def add(self, block):  # Add Process Control Blocks to queue.
        self.q.append(block)

    def remove(self):
        try:
            self.q.popleft()
            return True
        except IndexError:
            return False

    def top(self):
        try:
            return self.q[0]
        except IndexError:
            return False

    def is_empty(self):
        """Python 3 does not provide a method to return whether deques are empty."""
        if not self.q:
            return True
        else:
            return False

    def get_number(self):
        return self.number

    def set_number(self, num):
        self.number = num

    def task_complete(self):
        if self.remove() is True:
            print("Task completed.")
        else:
            print("Failure: Nothing to remove.")

    def print_device_queue(self):
        if not self.q:
            print("Nothing in device queue.")
            return
        for block in self.q:
            block.print_device()


class DiscQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "c"

class DiskQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "d"
        self.cylinders = None

    def set_cylinders(self, num):
        print("Disk " + str(num) + ": Enter number of disk cylinders:", end=' ')
        try:
            self.cylinders = int(input().strip())
            if self.cylinders < 0:
                print("Number of cylinders must be positive!")
                self.set_cylinders(num)
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_cylinders(num)


class PrinterQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p"
