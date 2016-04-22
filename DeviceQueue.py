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
    # We need a banner at the top so we know what's going on.

    def __init__(self):
        self.q = deque()
        self.number = None
        self.device_name = None
        self.banner = (" " * 4).join(["PID", "MEM", "R/W", "\tCPU Time", "# Bursts", "\tAVG"])

    def __bool__(self):
        """Implements truth testing to see whether the DeviceQueue has elements or not."""
        return bool(self.q)

    def add(self, block):
        """Add Process Control Blocks to queue."""
        self.q.append(block)

    def pop(self):
        """Pop item from the front of DeviceQueue, and return it."""
        if self.q:
            return self.q.popleft()
        else:
            return False

    def top(self):
        """Return whatever is at the front of the DeviceQueue."""
        try:
            return self.q[0]
        except IndexError:
            pass

    def add_file_info(self, block):
        """Ask for additional attributes when moving process to DeviceQueue."""
        block.set_file_name()
        block.set_file_length()

    def get_number(self):
        return self.number

    def set_number(self, num):
        self.number = num

    def task_complete(self):
        if self.pop() is not False:
            print("Task completed.")
        else:
            print("Failure: Nothing to remove.")

    def print_device_queue(self):
        print(self.banner)
        if not self.q:
            print("Nothing in device queue.")
            return
        for block in self.q:
            block.print_device_queue()


class DiscQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "c"

class DiskQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "d"
        self.num_cylinders = None
        self.cylinders = deque(maxlen=self.num_cylinders)
        self.banner = (" " * 4).join(["PID", "MEM", "R/W", "Cylinder", "\tCPU Time", "# Bursts", "AVG"])

    def set_num_cylinders(self, num):
        print("Disk " + str(num) + ": Enter number of disk cylinders:", end=' ')
        try:
            self.num_cylinders = int(input().strip())
            if self.num_cylinders < 0:
                print("Number of cylinders must be positive!")
                self.set_num_cylinders(num)
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_num_cylinders(num)

    def add_file_info(self, block):
        """Ask for additional attributes when moving process to DeviceQueue."""
        block.set_file_name()
        block.set_file_length()
        block.set_cylinder()
        if block.location not in self.cylinders:
            if block.location < self.num_cylinders:
                self.cylinders.append(block.location)
            else:
                print("Exceeded limit.")
                self.add_file_info(block)
        else:
            print("That cylinder is not available.")
            self.add_file_info(block)

    def print_device_queue(self):
        print(self.banner)
        if not self.q:
            print("Nothing in device queue.")
            return
        for block in self.q:
            block.print_disk_queue()


class PrinterQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p"
