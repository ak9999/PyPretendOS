"""
Author: Abdullah Khan
File: PretendSystem.py
Description:
The PretendSystem class contains information like how many of each piece of
hardware (CPUs, printers, hard disks, CD/RW drives) are available.
"""


"""
cleanup() is needed because Python compiles imported files to bytecode and caches them.
These .pyc files are stored in __pycache__, we can just ignore them.
"""
def cleanup():  # Clean up the pycache
    import shutil
    try:
        shutil.rmtree("__pycache__")
    except FileNotFoundError:
        print("Failed to remove __pycache__ directory")

class PretendSystem:
    def __init__(self):
        self.disks = 0
        self.printers = 0
        self.disc_drives = 0
        self.CPUs = 1  # For now we assume there is only one CPU.
        self.num_processes = 0
        self.sys_gen()  # Call sys_gen upon construction

    '''
    get_num_disks: asks whoever is installing the system for the # of disks.
    If they input anything but a number, they will be prompted again.
    '''

    def get_num_disks(self):
        print("Enter the number of disks:", end=' ')
        try:
            self.disks = int(input())
            if self.disks <= 0:
                print("Can't have less than one.")
                self.get_num_disks()
        except ValueError:
            print("Error, try again.")
            self.get_num_disks()
        except KeyboardInterrupt:
            print()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            exit()  # If Ctrl-D, just exit.

    '''
    get_num_printers: same thing but for printers
    '''

    def get_num_printers(self):
        print("Enter the number of printers:", end=' ')
        try:
            self.printers = int(input())
            if self.printers <= 0:
                print("Can't have less than one.")
                self.get_num_printers()
        except ValueError:
            print("Error, try again.")
            self.get_num_printers()
        except KeyboardInterrupt:
            print()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            exit()  # If Ctrl-D, just exit.

    def get_num_cdrw(self):
        print("Enter the number of CD/RW drives:", end=' ')
        try:
            self.disc_drives = int(input())
            if self.disc_drives <= 0:
                print("Can't have less than one.")
                self.get_num_cdrw()
        except ValueError:
            print("Error, try again.")
            self.get_num_cdrw()
        except KeyboardInterrupt:
            print()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            exit()  # If Ctrl-D, just exit.

    '''
    This is the sysgen function, where I ask how many of each piece of hardware
    there is. For now I assume there is only ONE CPU.
    '''

    def sys_gen(self):
        print("Welcome to Totally Not UNIX!", end='\n')
        print()
        print("Starting setup...", end="\n")
        self.get_num_disks()
        self.get_num_printers()
        self.get_num_cdrw()

    def printsys(self):
        print("# CPUs:", self.CPUs)
        print("# disks:", self.disks)
        print("# printers:", self.printers)
        print("# CDRW drives:", self.disc_drives)
