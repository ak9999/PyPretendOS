"""
Author: Abdullah Khan
File: Signals.py
Description: Handles making sure system calls and interrupts are valid.
"""

import re
from PretendSystem import cleanup
from PCB import ProcessControlBlock as PCB


def leave():
    print()
    cleanup()
    exit()


def timer(system):
    if system.ready.cpu:
        print("How long has the current process been using the CPU?:", end=' ')
        try:
            t = float(input().strip())
            if t < 0:
                print("Can't be negative. Try again.")
                timer()
            else:
                system.ready.cpu[0].add_time(t)
        except ValueError:
            print("Error, try again.")
            timer(system)
        except KeyboardInterrupt:
            print()
            cleanup()
            exit()  # If Ctrl-C, just exit.
        except EOFError:
            print()
            cleanup()
            exit()  # If Ctrl-D, just exit.

def snapshot_mode(system):
    print("Valid inputs: c, d, p, r")
    while True:
        print("Options: c, d, p")
        print("S-", end="")
        try:
            command = input()
        except KeyboardInterrupt:
            leave()
        except EOFError:
            leave()

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
    timer(system)
    snapshot_mode(system)
    return


def terminate(system):
    timer(system)
    system.ready.remove()
    return


def arrival(system):
    timer(system)
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
        #print("Bad input.")  # maybe send to device here
        return


def send_to_device(command, system):
    if command[0] == 'c':
        timer(system)
        if system.ready.cpu_is_empty():
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
        timer(system)
        if system.ready.cpu_is_empty():
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
        timer(system)
        if system.ready.cpu_is_empty():
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
        timer(system)
        try:
            if int(command[1:]) > system.get_num_cdrw() - 1:
                print("Bad index. Remember we count from 0.")
            elif not system.discs[int(command[1:])]:
                print("Nothing in queue!")
                return
            else:
                process = system.discs[int(command[1:])].top()
                process.set_rw('')
                system.ready.add(process)
                if system.discs[int(command[1:])].remove() is not False:
                    print("Process complete! Moved to back of ready queue.")
                else:
                    print("No process in queue!")
        except AttributeError:
            pass
    if command[0] == 'D':
        timer(system)
        try:
            if int(command[1:]) > system.get_num_cdrw() - 1:
                print("Bad index. Remember we count from 0.")
            elif not system.discs[int(command[1:])]:
                print("Nothing in queue!")
                return
            else:
                process = system.disks[int(command[1:])].top()
                process.set_rw('')
                system.ready.add(process)
                if system.disks[int(command[1:])].remove() is not False:
                    print("Process complete! Moved to back of ready queue.")
                else:
                    print("No process in queue!")
        except AttributeError:
            pass
    if command[0] == 'P':
        timer(system)
        try:
            if int(command[1:]) > system.get_num_cdrw() - 1:
                print("Bad index. Remember we count from 0.")
            elif not system.printers[int(command[1:])]:
                print("Nothing in queue!")
            else:
                process = system.discs[int(command[1:])].top()
                process.set_rw('')
                system.ready.add(process)
                if system.printers[int(command[1:])].remove() is not False:
                    print("Process complete! Moved to back of ready queue.")
                else:
                    print("No process in queue!")
        except AttributeError:
            pass

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
