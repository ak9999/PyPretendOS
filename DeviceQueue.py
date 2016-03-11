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

    def add(self, block):  #  Add Process Control Blocks to queue.
        self.q.append(block)

    def remove(self):
        self.q.popleft()

    def get_number(self):
        return self.number

    def set_number(self, num):
        self.number = num

    def task_complete(self):
        print("Task completed.")
        self.remove()

    def __str__(self):
        print("%s" % self.device, end="\n")

        for block in self.q:
            print("%s\t %s\t %s\t %s\t %s\t"
                   % (str(block.get_pid()),
                      str(block.get_filename()),
                      str(block.get_memstart()),
                      str(block.get_rw()),
                      str(block.get_filelength()))
                 )


class DiscQueue(DeviceQueue):

    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "c%d" % int(get_number())


class DiskQueue(DeviceQueue):

    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "d%d" % int(get_number())


class PrinterQueue(DeviceQueue):

    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p%d" % int(get_number())
