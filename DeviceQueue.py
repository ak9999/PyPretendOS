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
        self.banner = (" " * 4).join(["PID", "MEM", "R/W", "Cylinder", "\tCPU Time", "# Bursts", "AVG"])
        #  We need a second queue for FSCAN.
        self.r = deque()
        #  We need to know whether the queue is frozen or not.
        #  We also need to know if this is the first request.
        self.frozen = False #  By default, no.
        self.first_request = True #  By default, yes.

    def __bool__(self):
        """Return whether both deques are empty."""
        if not self.q and not self.r:
            return True
        else:
            return False

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
        if block.location >= self.num_cylinders:
            print("There's only {0} cylinders. Try again. [0-{1}]".format(self.num_cylinders,
                                                                          self.num_cylinders - 1))
            self.add_file_info(block)

    def print_device_queue(self):
        print(self.banner)
        if not self.q:
            print("Nothing in device queue.")
            return
        if self.q:
            print("Seek:")
            for block in self.q:
                block.print_disk_queue()

    def add(self, block):
        """Runs FSCAN to put the PCBs in order."""
        if not self.frozen:
            self.q.append(block)  # Add the PCB
            self.fscan_sort()     # Sort the queue
            self.on_request()     # Freeze the queue
            return True
        else:
            self.r.append(block)
            self.fscan_sort()
            return True

    def pop(self):
        """Pop item from the front of DeviceQueue, and return it."""
        if self.q:
            if not self.q:
                self.fscan_sort()
            return self.q.popleft()
        else:
            return self.pop()

    def freeze(self):
        """Sets freeze to the opposite of whatever it was,
           so we know to use another queue to collect requests."""
        if(not self.frozen and not self.r) or (self.frozen and not self.q):
            self.frozen = not self.frozen

    def on_request(self):
        """When we receive a request and both deques are empty, lock one queue and have the other take requests."""
        if self.first_request:
            self.freeze()
            self.first_request = False
        if not self.first_request and self:
            self.frozen = True
            self.first_request = True

    def fscan_sort(self):
        """Sort by PID first, then sort by cylinder."""
        if not self:
            return False
        if len(self.q) > 1:
            self.q = deque(sorted(self.q, key=lambda pcb: pcb.pid))
            self.q = deque(sorted(self.q, key=lambda pcb: pcb.get_cylinder))
        if len(self.r) > 1:
            self.r = deque(sorted(self.r, key=lambda pcb: pcb.pid))
            self.r = deque(sorted(self.r, key=lambda pcb: pcb.get_cylinder))




class PrinterQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p"
