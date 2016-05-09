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
        block.set_memstart()
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
        #  Need read/write head at position 0.
        self.head = 0

    def set_num_cylinders(self, num):
        print("Disk " + str(num) + ": Enter number of disk cylinders:", end=' ')
        try:
            self.num_cylinders = int(input().strip())
            if self.num_cylinders <= 0:
                print("Number of cylinders must be greater than 0!")
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
        if not self.q and not self.r:
            print("Nothing in device queue.")

        if self.q:
            print("Currently seeking:")
            for block in self.q:
                block.print_disk_queue()
        if self.r:
            print("Requests:")
            for block in self.r:
                block.print_disk_queue()

    def fscan_sort(self):
        # Get a list of all requests ahead of where the head currently is.
        forward = [idx for idx in self.r if self.r[-1].get_cylinder >= self.head]
        # Now sort by PID, tie-breaker taken care of.
        forward.sort(key=lambda pcb: pcb.pid)
        # Sort by cylinder
        forward.sort(key=lambda pcb: pcb.get_cylinder)
        # Now we do the same for requests behind the head.
        backward = [idx for idx in self.r if self.r[-1].get_cylinder < self.head]
        backward.sort(key=lambda pcb: pcb.pid)
        '''
        Sort in reverse this time because these should always go to the back of the queue.
        When we reach the last job going towards the end of the disk, we should
        begin handling the requests in reverse order. This is why I sort in
        reverse.
        '''
        backward.sort(key=lambda pcb: pcb.get_cylinder, reverse=True)
        # We can clear the requests queue now.
        self.r.clear()
        # Fill the primary queue with the sorted requests.
        # deque takes iterables
        self.q = deque(forward + backward)


    def add(self, block):
        self.r.append(block)
        if not self.q:
            self.fscan_sort()

    def pop(self):
        if self.q:
            self.head = self.q[0].get_cylinder
            if not self.q:
                self.fscan_sort()
            return self.q.pop()

class PrinterQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p"
