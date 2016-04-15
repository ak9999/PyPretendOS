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
cleanup() is needed because Python compiles imported files to bytecode and caches them.
These .pyc files are stored in __pycache__, we can just ignore them.
"""


def cleanup():  # Clean up the pycache
    import shutil
    try:
        shutil.rmtree("__pycache__")
    except FileNotFoundError:
        return

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
        self.alpha = None  # History parameter.
        self.tau = None
        #  Initialize queues.
        self.printers = list()
        self.disks = list()
        self.discs = list()
        self.ready = RQ()
        #  System generation.
        self.sys_gen()  # Call sys_gen upon instantiation

        self.total_cpu = 0

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
            if self.set_tau(t) is False:
                print("Error setting initial burst.")
        except ValueError:
            print("Error, try again.")
            self.set_init_burst()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

    def set_hist_param(self):
        print("Enter the history parameter (α, 0 ≤ α ≤ 1):", end=' ')
        try:
            self.alpha = float(input().strip())
            if self.alpha > 1 or self.alpha < 0:
                print("The history parameter must be α, 0 ≤ α ≤ 1. Try again.")
                self.set_hist_param()
        except ValueError:
            print("Error, try again.")
            self.set_hist_param()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

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
        except ValueError:
            print("Error, try again.")
            self.set_num_disks()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

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
        except ValueError:
            print("Error, try again.")
            self.set_num_printers()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

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
        except ValueError:
            print("Error, try again.")
            self.set_num_cdrw()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

    '''
    This is the sys_gen function, where I ask how many of each piece of hardware
    there is. For now I assume there is only ONE CPU.
    '''
    def sys_gen(self):
        print("Welcome to Totally Not UNIX!", end='\n')
        print()
        print("Starting setup...", end="\n")
        self.set_num_disks()
        self.set_num_printers()
        self.set_num_cdrw()
        self.set_hist_param()
        self.set_init_burst()

    """
    Getter methods.
    """
    def get_tau(self):
        return self.tau

    def get_hist_param(self):
        return self.alpha

    def get_num_disks(self):
        return self.num_disks

    def get_num_printers(self):
        return self.num_printers

    def get_num_cdrw(self):
        return self.num_disc_drives

    def get_discs(self):
        return self.discs

    def get_disks(self):
        return self.disks

    def get_printers(self):
        return self.printers

    def print_device(self, device):
        print("Enter the # of the device you'd like to view:", end=" ")
        try:
            number = int(input().strip())
            if number < 0:
                return
        except ValueError:
            print("Positive integers only.")
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

        try:
            device[number].print_device_queue()
        except IndexError:
            print("Bad index.")
            print(self)

    """
    This is so we can easily print out the system details.
    """
    def __str__(self):
        string = ""
        string += "# CPUs: " + str(self.num_CPUs) + "\n" \
            + "# disks: " + str(self.num_disks) + "\n" \
            + "# printers: " + str(self.num_printers) + "\n" \
            + "# CDRW drives: " + str(self.num_disc_drives)
        return string
