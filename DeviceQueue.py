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
        print("Task completed.")
        self.remove()

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
        #  To implement FSCAN, we need two queues in the disk.
        self.q = deque()
        self.r = deque()
        #  Boolean flag determining if a queue is frozen.
        self.frozen = False
        self.first_request = True

    def add(self, block):
        """Runs the FSCAN function to order the PCBs and append them to the proper queues."""
        if not self.frozen:
            self.q.append(block)  # Add the PCB
            self.fscan_sort()     # Sort the queue
            self.on_request()     # Freeze the queue
            return True
        else:
            self.r.append(block)
            self.fscan_sort()
            return True

    def is_empty(self):
        """Return whether both deques are empty."""
        if not self.q and not self.r:
            return True
        else:
            return False

    def freeze(self):
        """Sets freeze to the opposite of whatever it was, so we know to use the other queue to collect requests."""
        if(not self.frozen and not self.r) or (self.frozen and not self.q):
            self.frozen = not self.frozen

    def on_request(self):
        """When we receive a request and both deques are empty, lock one queue and have the other take requests."""
        if self.first_request:
            self.freeze()
            self.first_request = False
        if not self.first_request and self.is_empty():
            self.frozen = True
            self.first_request = True

    def set_cylinders(self, num):
        print("Disk " + str(num) + ": Enter number of disk cylinders:", end=' ')
        try:
            self.cylinders = int(input().strip())
            if self.cylinders <= 1000:
                print("Must be greater than 1000.")
                self.set_cylinders(num)
        except ValueError:
            print("Error, try again.")
            self.set_cylinders(num)

    def get_num_cylinders(self):
        return int(self.cylinders)

    def get_cylinder(self, block):
        return block.get_cylinder()

    def get_PID(self, block):
        return block.get_pid()

    def print_device_queue(self):
        if not self.q:
            print("Nothing in device queue.")
            return
        for block in self.q:
            block.print_disk()

    def fscan_sort(self):
        q_list = list(self.q)
        q_len = len(q_list)
        r_list = list(self.r)
        r_len = len(r_list)

        j = 0
        if self.is_empty():
            return False  # In this case, we can't sort.
        if q_len > 1:
            for i in range(1, q_len):
                j = i
                while(j > 0 and self.get_cylinder(self.q_list[j]) <= self.get_cylinder(self.q_list[j-1])):
                    if self.get_cylinder(self.q_list[j]) == self.get_cylinder(self.q_list[j-1]) and self.get_PID(self.q_list[j]) < self.get_PID(self.q_list[j-1]):
                        self.q_list[j], self.q_list[j-1] = self.q_list[j-1], self.q_list[j]
                        j -= 1
                        continue
        if r_len > 1:
            for i in range(1, r_len):
                j = i
                while (j > 0 and self.get_cylinder(self.r_list[j]) <= self.get_cylinder(self.r_list[j - 1])):
                    if self.get_cylinder(self.r_list[j]) == self.get_cylinder(self.r_list[j - 1]) and self.get_PID(self.r_list[j]) < self.get_PID(self.r_list[j - 1]):
                        self.r_list[j], self.r_list[j - 1] = self.r_list[j - 1], self.r_list[j]
                        j -= 1
                        continue


class PrinterQueue(DeviceQueue):
    def __init__(self):
        DeviceQueue.__init__(self)
        self.device_name = "p"
