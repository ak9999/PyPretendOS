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
        self.memstart = None
        self.memend = None
        self.rw = None
        self.filename = None
        self.file_length = None
        create_block(self)

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
        print(str(self.memstart) + "," + str(self.memend))

    def set_memstart(self):
        global available_address
        self.memstart = available_address

    def set_memend(self):
        self.memend = self.memstart + self.file_length
        global available_address
        available_address += self.file_length

    def set_pid(self):
        global process_id
        process_id += 1
        self.pid = process_id

    def set_rw(self, operation):
        self.rw = operation

    def set_file_length(self):
        print("File length:", end=" ")
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
        print("File name:", end=" ")
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

    def __str__(self):
        string = ("%s\t%s\t%s\t%s\t%s"
                  % (str(self.pid).rjust(3),
                     str(self.filename).rjust(8),
                     str(self.memstart).rjust(8),
                     str(self.rw).rjust(3),
                     str(self.file_length).rjust(11)))
        return string


def create_block(block):
    block.set_file_name()
    block.set_file_length()
    block.set_memstart()
    block.set_memend()
    block.set_pid()

    return block
