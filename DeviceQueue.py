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

    def add(self, block):  #  Add Process Control Blocks to queue.
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
            string = ("%s\t%s\t%s\t%s\t%s"
                  % (str(self.pid).rjust(3),
                     str(self.filename).rjust(8),
                     str(self.memstart).rjust(8),
                     str(self.rw).rjust(3),
                     str(self.file_length).rjust(11)))
        return string

    def __str__(self):
        print("=====%s" % self.device_name, end="\n")
        self.print_device_queue()


class DiscQueue(DeviceQueue):

    def __init__(self):
        DeviceQueue.__init__(self)
        self.add()
        self.device_name = "c%d" % str(self.get_number())


class DiskQueue(DeviceQueue):

    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "d%d" % str(self.get_number())


class PrinterQueue(DeviceQueue):

    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p%d" % str(self.get_number())
