"""
Author: Abdullah Khan
File: PCB.py
Description: The PCB class implements the Process Control Block.
The PCB includes:
    process state
    process number (PID)
    memory address, etc.
"""

import random  # to generate memory address
from PretendSystem import cleanup

"""
PCB class definiton.
"""


class ProcessControlBlock:
    def __init__(self):
        self.pid = None
        self.memstart = None
        self.rw = None
        self.filename = None
        self.file_length = None
        create_block(self)

    def get_pid(self):
        return self.pid

    def get_memstart(self):
        return self.memstart

    def get_filename(self):
        return self.filename

    def get_file_length(self):
        return self.file_length

    def get_rw(self):
        return self.rw

    def set_memstart(self):
        self.memstart = random.randint(100, 32000)

    def set_pid(self):
        self.pid = random.randint(2, 300)

    def set_rw(self, operation):
        self.rw = operation

    def set_file_length(self):
        print("File length: ", end=" ")
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
        print("File name: ", end=" ")
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
        representation = ("%s\t %s\t\t %s\t\t %s\t %s\t"
                          % (str(self.get_pid()),
                             str(self.get_filename()),
                             str(self.get_memstart()),
                             str(self.get_rw()),
                             str(self.get_file_length()))
                          )
        return representation


def create_block(block):
    block.set_file_name()
    block.set_file_length()
    block.set_memstart()
    block.set_pid()

    return block
