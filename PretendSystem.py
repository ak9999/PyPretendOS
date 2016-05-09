# coding=utf-8
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
        #  Initial burst estimate
        self.init_tau = 0
        #  History parameter, alpha.
        self.alpha = 0
        #  Number of completed (re: terminated) processes
        self.terminated = 0
        #  System Total CPU time of completed (re: terminated) processes
        self.total_time = 0
        self.sys_avg = 0
        # Total memory
        self.total_memory = 0
        # Max process size
        self.proc_max_size = 0
        # Page size.
        self.page_size = 0
        # Number of pages
        self.npages = 0
        # Job pool.
        self.job_pool = list()
        #  System generation.
        self.sys_gen()  # Call sys_gen upon instantiation

    def power2(self, n):
        '''Returns boolean value'''
        return n != 0 and ((n & (n - 1)) == 0)

    """
    Setter methods.
    """

    def set_totalmem(self):
        try:
            print("Enter the amount of total memory in words:", end=' ')
            self.total_memory = int(input().strip())
            if self.total_memory < 1:
                print("You must have memory.")
                self.set_totalmem()
            # if self.total_memory % self.page_size != 0:
            #     print("Total memory must be a multiple of the page size!")
            #     self.set_totalmem()
            self.npages = self.total_memory // self.page_size
        except (ValueError, EOFError):
            print("You must have memory.")
            self.set_totalmem()

    def set_proc_size(self):
        try:
            print("Enter the maximum size of a process:", end=' ')
            self.proc_max_size = int(input().strip())
            if self.proc_max_size < 1:
                print("Processes do use memory.")
                self.set_proc_size()
        except (ValueError, EOFError):
            print("Processes do use memory.")
            self.set_proc_size()

    def set_page_size(self):
        try:
            print("Enter the size of pages:", end=' ')
            self.page_size = int(input().strip())
            if self.power2(self.page_size) == False:
                print("Page sizes must be a power of 2.")
                self.set_page_size()
        except (ValueError, EOFError):
            print("Page sizes must be a power of 2.")
            self.set_page_size()

    def set_tau(self, num):
        try:
            self.init_tau = num
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
        print("Enter the history parameter (alpha, 0 <= alpha <= 1):", end=' ')
        try:
            self.alpha = float(input().strip())
            if self.alpha > 1 or self.alpha < 0:
                print("The history parameter must be alpha, 0 <= alpha <= 1. Try again.")
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
                    dq.set_num_cylinders(_)
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

    """Getters."""

    def get_num_cdrw(self):
        return self.num_disc_drives

    def get_num_printers(self):
        return self.num_printers

    def get_num_disks(self):
        return self.num_disks


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
        # Added in project 2
        print()
        self.set_hist_param()
        self.set_init_burst()
        print()
        # Added in project 3
        self.set_page_size()
        self.set_totalmem()
        self.set_proc_size()
        print()
        self.print_mem_info()
        print()

    """
    This is so we can easily print out the system details.
    """
    def print_mem_info(self):
        print("Page size: " + str(self.page_size) + " word(s).")
        print("Total memory: " + str(self.total_memory) + " word(s) or " + str(self.npages) + " page(s).")
        print("Maximum process size is: " + str(self.proc_max_size) + " word(s).")

    def print_available_hardware(self):
        string = ""
        string += "# CPUs: " + str(self.num_CPUs) + "\n" \
            + "# disks: " + str(self.num_disks) + "\n" \
            + "# printers: " + str(self.num_printers) + "\n" \
            + "# CDRW drives: " + str(self.num_disc_drives)
        print(string)

    def print_device(self, device_list):
        for idx in range(len(device_list)):
            print("Device: " + device_list[idx].device_name + str(idx))
            device_list[idx].print_device_queue()

    def update_sys_avg(self, num):
        self.total_time += num
        self.terminated += 1
        self.sys_avg = self.total_time / self.terminated
        print("System average total CPU time: {0}".format(round(self.sys_avg)))
