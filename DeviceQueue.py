"""
Author: Abdullah Khan
File: CPU.py
Description: CPU class implementation
"""

from collections import deque

"""
This is the generic device queue that will be inherited by the actual devices.
"""


class DeviceQueue(object):
    def __init__(self):
        self.q = deque()
        self.number = None
        self.device_name = None

    def add(self, block):  # Add Process Control Blocks to queue.
        self.q.append(block)

    def remove(self):
        try:
            self.q.popleft()
        except IndexError:
            print("Nothing to remove!")

    def get_number(self):
        return self.number

    def set_number(self, num):
        self.number = num

    def task_complete(self):
        print("Task completed.")
        self.remove()

    def print_device_queue(self):
        string = ""
        for block in self.q:
            string += str(block + "\n")
        return string

    def __str__(self):
        print("=====%s" % self.device_name, end="\n")
        self.print_device_queue()


class DiscQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "c" + str(self.get_number())


class DiskQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "d" + str(self.get_number())


class PrinterQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p" + str(self.get_number())
