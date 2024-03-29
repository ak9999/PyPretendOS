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
    def __init__(self, hist_parameter, init_tau):
        self.pid = None
        self.memstart = 0
        self.memend = 0
        self.rw = '-'
        self.filename = ''
        self.file_length = 0
        # This is the cylinder the data is on if PCB is going to disk.
        self.location = 0
        # For timing.
        self.num_bursts = 0
        self.sys_alpha = hist_parameter  # Get this from the system.
        self.tau = init_tau
        self.total_cpu_time = 0
        self.current_cpu_time = 0
        self.time_at_termination = 0
        self.preempt = True  # Flag set to true by default so we know whether to add init_tau to total_cpu_time
        self.proc_size = 0
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
        #global available_address
        #self.memstart = available_address
        print("Enter the starting location in memory:", end=' ')
        try:
            # Python lets me change base so easily.
            self.memstart = int(input().strip(), 16)
            if self.memstart < 1:
                print("Try again.")
                self.set_memstart()
        except ValueError:
            print("Try again.")
            self.set_memstart()

    def set_memend(self):
        self.memend = self.memstart
        global available_address
        available_address += 1

    def set_pid(self):
        global process_id
        process_id += 1
        self.pid = process_id

    def set_rw(self, operation):
        self.rw = operation

    def set_file_length(self):
        print("File length:", end=' ')
        try:
            self.file_length = int(input().strip())
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_file_length()

    def set_file_name(self):
        print("File name:", end=' ')
        try:
            self.filename = input().strip()
        except EOFError:
            print("You must input a filename.")
            self.set_file_name()

    def set_cylinder(self):
        print("Enter cylinder:", end=' ')
        try:
            self.location = int(input())
            if self.location < 0:
                print("You can't have a negative amount of cylinders.")
                self.set_cylinder()
        except (ValueError, EOFError):
            print("You must enter an integer.")
            self.set_cylinder()

    @property
    def get_cylinder(self):
        return self.location


    @property #  To treat avg_burst like a variable
    def avg_burst(self):
        if self.num_bursts > 0:
            return self.total_cpu_time / self.num_bursts
        else:
            return 0

    def pre(self):
        if self.preempt == True:
            print("Process PID: {} preempted.".format(self.pid), end=' ')
            self.preempt = False
            self.total_cpu_time += self.tau
            self.current_cpu_time += self.tau
            print("Current burst: ", self.current_cpu_time)
        else:
            pass

    def get_actual_burst(self):
        self.pre()
        print("Enter actual CPU burst time: ", end='')
        try:
            time_t = int(input().strip())
            if time_t < 0:
                print("Error, try again.")
                self.get_actual_burst()
            else:
                self.total_cpu_time += time_t
                self.current_cpu_time -= time_t
                self.num_bursts += 1
                # (1 - alpha) * self.tau + alpha * time_t
                self.tau = (1 - self.sys_alpha) * self.tau + self.sys_alpha * time_t
                print("Current burst: ", self.current_cpu_time)
        except(EOFError, ValueError):
            print("Error, try again.")
            self.get_actual_burst()

    def print_block(self):
        string = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(self.pid, hex(self.memstart), self.rw, self.filename,
                                                                 self.file_length, self.location,)
        print(string)

    def print_ready_queue(self):
        string = "{0}\t{1}\t{2}\t{3}".format(str(self.pid).ljust(3),
                                        str(self.current_cpu_time).ljust(8),
                                        str(self.num_bursts).ljust(8),
                                        str(round(self.avg_burst, 2)).ljust(3),)
        print(string)

    def print_device_queue(self):
        string = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(str(self.pid).ljust(3),
                                             str(hex(self.memstart)).ljust(3),
                                             str(self.rw).ljust(2),
                                             str(self.current_cpu_time).ljust(8),
                                             str(self.num_bursts).ljust(8),
                                             str(round(self.avg_burst, 2)).ljust(3),)
        print(string)

    def print_disk_queue(self):
        string = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(str(self.pid).ljust(3),
                                             str(hex(self.memstart)).ljust(3),
                                             str(self.rw).ljust(2),
                                             str(self.location).ljust(8),
                                             str(self.current_cpu_time).ljust(8),
                                             str(self.num_bursts).ljust(5),
                                             str(round(self.avg_burst, 2)).ljust(3),)
        print(string)

    def complete(self):
        print("Process PID: {0} terminating.".format(self.pid))
        print("Total CPU time: {0}\tAvg. Burst time: {1}".format(self.total_cpu_time, round(self.avg_burst, 2)))

    def set_size(self):
        print("Process size:", end=' ')
        try:
            self.proc_size = int(input().strip())
        except (ValueError, EOFError):
            print("Error, try again.")
            self.set_size()

    @property
    def get_size(self):
        return self.proc_size


def create_block(block):
    block.set_pid()
    block.set_size()
    block.set_memend()
    return block
