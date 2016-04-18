"""
Author: Abdullah Khan
File: PCB.py
Description: The PCB class implements the Process Control Block.
The PCB includes:
    process state
    process number (PID)
    memory address, etc.
"""

"""
PCB class definition.
"""

process_id = 0
available_address = 256


class ProcessControlBlock:
    def __init__(self):
        self.pid = None
        self.memstart = 0
        self.memend = 0
        self.rw = '-'
        self.filename = None
        self.file_length = 0
        # This is the cylinder the data is on if PCB is going to disk.
        self.location = 0
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
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_file_length()

    def set_file_name(self):
        print("File name:", end=' ')
        try:
            self.filename = input()
        except EOFError:
            print("You must input a filename.")
            self.set_file_name()

    def set_cylinder(self):
        print("Enter cylinder:", end=' ')
        try:
            self.location = int(input())
        except (ValueError, EOFError):
            print("You must enter an integer.")
            self.set_cylinder()

    def print_block(self):
        string = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(self.pid, self.memstart, self.rw, self.filename,
                                                                 self.file_length, self.location,)
        print(string)

def create_block(block):
    block.set_pid()
    block.set_file_length()
    block.set_file_name()
    block.set_memstart()
    block.set_memend()
    return block
