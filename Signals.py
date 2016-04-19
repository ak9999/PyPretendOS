"""
Author: Abdullah Khan
File: Signals.py
Description: Handles making sure system calls and interrupts are valid.
"""

import re
from PCB import ProcessControlBlock as PCB


def snapshot_mode(system):
    print("Valid inputs: c, d, p, r")
    while True:
        print("S-", end="")
        command = input()

        if valid_signal(command):
            if command[0] == "r":
                system.ready.print_queue()
                return
            elif command[0] == "c":
                system.print_device(system.discs)
                return
            elif command[0] == "d":
                system.print_device(system.disks)
                return
            elif command[0] == "p":
                system.print_device(system.printers)
                return
            else:
                print("Invalid option.")
                return
        else:
            return


def snapshot(system):
    snapshot_mode(system)
    return


def terminate(system):
    system.ready.remove()
    return


def arrival(system):
    pcb = PCB()
    system.ready.add(pcb)
    return


def signal(letter, system):
    """
    Python does not have switch/cases like C++, but we can
    use dictionaries to mimic that functionality.
    """
    switch_case = \
        {
            "A": arrival,  # put PCB into ready queue
            "S": snapshot,
            "t": terminate
        }
    if letter in switch_case:
        #  Get function from the switch_case dictionary
        function = switch_case.get(letter)
        return function(system)  # Return the function and execute it.
    else:
        pass


def send_to_device(command, system):
    if command[0] == 'c':
        if system.ready.cpu_process():
            print("There isn't a process running.")
        elif int(command[1:]) > system.get_num_cdrw() - 1:
            print("Bad index. Remember we count from 0.")
        else:
            process = system.ready.cpu[0]
            process.set_file_name()
            print("Is this a read or write?:", end=" ")
            operation = str(input().strip()).lower()
            if not valid_readwrite(operation):
                print("Bad input.")
                return
            process.set_rw(operation)
            system.discs[int(command[1:])].add(process)
            print("Process sent to %s." % command)
            system.ready.remove()
    elif command[0] == 'd':
        if system.ready.cpu_process():
            print("There isn't a process running.")
        elif int(command[1:]) > system.get_num_disks() - 1:
            print("Bad index. Remember we count from 0.")
        else:
            process = system.ready.cpu[0]
            process.set_file_name()
            process.set_cylinder()
            print("Is this a read or write?:", end=" ")
            operation = str(input().strip()).lower()
            if not valid_readwrite(operation):
                print("Bad input.")
                return
            process.set_rw(operation)
            system.disks[int(command[1:])].add(process)
            print("Process sent to %s." % command)
            system.ready.remove()
    elif command[0] == 'p':
        if system.ready.cpu_process():
            print("There isn't a process running.")
        elif int(command[1:]) > system.get_num_printers() - 1:
            print("Bad index. Remember we count from 0.")
        else:
            process = system.ready.cpu[0]
            process.set_file_name()
            process.set_rw("w")
            system.printers[int(command[1:])].add(process)
            print("Process sent to %s." % command)
            system.ready.remove()
    else:
        print("Serious problem.")


def complete_process(command, system):
    if command[0] == 'C':
        if int(command[1:]) > system.get_num_cdrw() - 1:
            print("Bad index. Remember we count from 0.")
        elif not system.discs[int(command[1:])]:
            print("Nothing in queue!")
            return
        else:
            process = system.discs[int(command[1:])].top()
            # Set all the stuff back to default values.
            # CPU knows nothing of file sizes and read/write.
            process.filename = None
            process.file_length = 0
            process.set_rw('-')
            system.ready.add(process)
            if system.discs[int(command[1:])].pop() is not False:
                print("Process complete! Moved to back of ready queue.")
            else:
                print("No process in queue!")
    if command[0] == 'D':
        if int(command[1:]) > system.get_num_disks() - 1:
            print("Bad index. Remember we count from 0.")
        elif not system.disks[int(command[1:])]:
            print("Nothing in queue!")
            return
        else:
            process = system.disks[int(command[1:])].top()
            # Set all the stuff back to default values.
            # CPU knows nothing of file sizes and cylinders.
            process.filename = None
            process.file_length = 0
            process.location = 0
            process.set_rw('-')
            system.ready.add(process)
            if system.disks[int(command[1:])].pop() is not False:
                print("Process complete! Moved to back of ready queue.")
            else:
                print("No process in queue!")
    if command[0] == 'P':
        if int(command[1:]) > system.get_num_printers() - 1:
            print("Bad index. Remember we count from 0.")
        elif not system.printers[int(command[1:])]:
            print("Nothing in queue!")
        else:
            process = system.printers[int(command[1:])].top()
            # Set all the stuff back to default values.
            # CPU knows nothing of file sizes and read/write.
            process.filename = None
            process.file_length = 0
            process.set_rw('-')
            system.ready.add(process)
            if system.printers[int(command[1:])].pop() is not False:
                print("Process complete! Moved to back of ready queue.")
            else:
                print("No process in queue!")

"""
These are functions that will match inputs with regular expressions
to make sure the user doesn't break this program
"""


def valid_signal(pattern):
    """
    Return whether the pattern is a valid signal
    """
    return re.compile(r"^[AcdrStp]{1}$").match(pattern) is not None


def valid_device(pattern):
    """
    Return whether the pattern is a valid device
    """
    return re.compile(r"^[cdp][0-9]{1}$").match(pattern) is not None

def valid_complete(pattern):
    return re.compile(r"^[CDP][0-9]{1}$").match(pattern) is not None


def valid_readwrite(pattern):
    return re.compile(r"^[rw]{1}$").match(pattern) is not None
