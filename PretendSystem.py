"""
Author: Abdullah Khan
File: PretendSystem.py
Description:
The PretendSystem class contains information like how many of each piece of
hardware (CPUs, printers, hard disks, CD/RW drives) are available.
"""

from ReadyQueue import ReadyQueue as RQ
from DeviceQueue import *

"""
This is a large mess of functions that will handle the operating system.
"""


class PretendSystem:
    def __init__(self):
        #  Number of hardware devices
        self.num_disks = 0
        self.num_printers = 0
        self.num_disc_drives = 0
        self.num_CPUs = 1  # For now we assume there is only one CPU.
        self.num_processes = 0
        #  Initialize queues.
        self.printers = list()
        self.disks = list()
        self.discs = list()
        self.ready = RQ()
        #  System generation.
        self.sys_gen()  # Call sys_gen upon instantiation

    """
    Setter methods.
    """

    def set_tau(self, num):
        try:
            self.tau = num
            return True
        except ValueError:
            return False

    def set_init_burst(self):
        print("Enter the initial burst estimate in milliseconds:", end=' ')
        try:
            t = float(input().strip())
            if t < 0:
                print("Can't be negative. Try again.")
                self.set_init_burst()
            if self.set_tau(t) is False:
                print("Error setting initial burst.")
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_init_burst()

    def set_hist_param(self):
        print("Enter the history parameter (α, 0 ≤ α ≤ 1):", end=' ')
        try:
            self.alpha = float(input().strip())
            if self.alpha > 1 or self.alpha < 0:
                print("The history parameter must be α, 0 ≤ α ≤ 1. Try again.")
                self.set_hist_param()
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_hist_param()

    def set_num_disks(self):
        print("Enter the number of disks:", end=' ')
        try:
            self.num_disks = int(input().strip())
            if self.num_disks <= 0 or self.num_disks > 10:
                print("Must be between 1 and 10.")
                self.set_num_disks()
            else:
                for _ in range(0, self.num_disks):
                    dq = DiskQueue()
                    dq.set_number(_)
                    dq.set_cylinders(_)
                    self.disks.append(dq)
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_num_disks()

    def set_num_printers(self):
        print("Enter the number of printers:", end=' ')
        try:
            self.num_printers = int(input().strip())
            if self.num_printers <= 0 or self.num_printers > 10:
                print("Must be between 1 and 10.")
                self.set_num_printers()
            else:
                for _ in range(0, self.num_printers):
                    dq = PrinterQueue()
                    dq.set_number(_)
                    self.printers.append(dq)
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_num_printers()

    def set_num_cdrw(self):
        print("Enter the number of CD/RW drives:", end=' ')
        try:
            self.num_disc_drives = int(input().strip())
            if self.num_disc_drives <= 0 or self.num_disc_drives > 10:
                print("Must be between 1 and 10.")
                self.set_num_cdrw()
            else:
                for _ in range(0, self.num_disc_drives):
                    dq = DiscQueue()
                    dq.set_number(_)
                    self.discs.append(dq)
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_num_cdrw()

    '''
    This is the sys_gen function, where I ask how many of each piece of hardware
    there is. For now I assume there is only ONE CPU.
    '''

    def sys_gen(self):
        print("Starting setup...")
        print()
        self.set_num_disks()
        self.set_num_printers()
        self.set_num_cdrw()
        self.print_available_hardware()

    """
    This is so we can easily print out the system details.
    """

    def print_available_hardware(self):
        string = ""
        string += "# CPUs: " + str(self.num_CPUs) + "\n" \
            + "# disks: " + str(self.num_disks) + "\n" \
            + "# printers: " + str(self.num_printers) + "\n" \
            + "# CDRW drives: " + str(self.num_disc_drives)
        print(string)