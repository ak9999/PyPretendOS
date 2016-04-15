"""
Author: Abdullah Khan
File: PCB.py
Description: The PCB class implements the Process Control Block.
The PCB includes:
    process state
    process number (PID)
    memory address, etc.
"""

from PretendSystem import cleanup

"""
PCB class definiton.
"""

process_id = 0
available_address = 256


class ProcessControlBlock:
    def __init__(self):
        self.pid = None
        self.memstart = 0
        self.memend = 0
        self.rw = ''
        self.filename = None
        self.file_length = 0
        self.location = 0  # This is the cylinder the data is on if PCB is going to disk.
        self.cpu_total = 0
        self.avg_burst = 0
        self.bursts = list()
        create_block(self)

    def time_cpu(self):
        print("How long has the current process been in the CPU?:", end=' ')
        try:
            self.cpu_total = float(input())
            if self.cpu_total < 0:
                print("Negative numbers not possible. Try again.")
                self.time_cpu()
        except ValueError:
            print("Error, try again.")
            self.time_cpu()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()
        except EOFError:
            print()
            cleanup()
            exit()

    def add_time(self, time):
        self.cpu_total += time

    def get_total_cpu_time(self):
        return self.cpu_total

    def get_pid(self):
        return self.pid

    def get_memstart(self):
        return self.memstart

    def get_memend(self):
        return self.memend

    def get_filename(self):
        return self.filename

    def get_file_length(self):
        return self.file_length

    def get_rw(self):
        return self.rw

    def get_mem_block(self):
        print(str(self.memstart) + ',' + str(self.memend))

    def get_cylinder(self):
        return int(self.location)

    def set_memstart(self):
        global available_address
        self.memstart = available_address

    def set_memend(self):
        self.memend = self.memstart
        global available_address
        available_address += self.file_length

    def set_pid(self):
        global process_id
        process_id += 1
        self.pid = process_id

    def set_rw(self, operation):
        self.rw = operation

    def set_file_length(self):
        print("File length:", end=' ')
        try:
            self.file_length = int(input())
        except ValueError:
            print("Error, try again.")
            self.set_file_length()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()
        except EOFError:
            print()
            cleanup()
            exit()

    def set_file_name(self):
        print("File name:", end=' ')
        try:
            self.filename = input()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

    def set_cylinder(self):
        print("Enter cylinder:", end=' ')
        try:
            self.location = int(input())
        except ValueError:
            print("Error, try again.")
            self.set_cylinder()
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

    def get_avgburst(self):
        avgbursts = 0
        if len(self.bursts) > 0:
            for x in self.bursts:
                avgbursts += x
            avgbursts /= len(self.bursts)
        return avgbursts

    def print_ready(self):
        string = ("%s\t%s\t%s\t%s"
                  % (str(self.pid).rjust(3),
                     str(self.memstart).rjust(8),
                     str(self.cpu_total(3)),
                     str(self.avg_burst).rjust(3)))
        print(string)

    def print_device(self):
        string = ("%s\t%s\t%s\t%s\t%s\t%s\t%s"
                  % (str(self.pid).rjust(3),
                     str(self.filename).rjust(5),
                     str(self.memstart).rjust(5),
                     str(self.rw).rjust(3),
                     str(self.file_length).rjust(5),
                     str(self.cpu_total).rjust(3),
                     str(self.avg_burst).rjust(3),))

        print(string)

    def print_disk(self):
        string = ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"
                  % (str(self.pid).rjust(3),
                     str(self.filename).rjust(5),
                     str(self.memstart).rjust(5),
                     str(self.rw).rjust(3),
                     str(self.file_length).rjust(5),
                     str(self.cpu_total).rjust(3),
                     str(self.avg_burst).rjust(3),
                     str(self.location).rjust(3)))
        print(string)

def create_block(block):
    block.set_file_length()
    block.set_memstart()
    block.set_memend()
    block.set_pid()

    return block
