"""
The System class contains information like how many of each piece of hardware
(CPUs, printers, hard disks, CD/RW drives) are available.
"""


class System:
    def __init__(self):
        self.disks = 0
        self.printers = 0
        self.disc_drives = 0
        self.CPUs = 1  # For now we assume there is only one CPU.

    '''
    get_num_disks: asks whoever is installing the system for the # of disks.
    If they input anything but a number, they will be prompted again.
    '''

    def get_num_disks(self):
        print("Enter the number of disks:", end=' ')
        try:
            self.disks = int(input())
        except ValueError:
            print("Error, try again.")
            self.get_num_disks()
            exit()  # Exit program
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
        except ValueError:
            print("Error, try again.")
            self.get_num_printers()
            exit()  # Exit program
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
        except ValueError:
            print("Error, try again.")
            self.get_num_cdrw()
            exit()  # Exit program
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

    def sysgen(self):
        print("Welcome to Totally Not UNIX!", end='\n')
        print()
        self.get_num_disks()
        self.get_num_printers()
        self.get_num_cdrw()

        return
