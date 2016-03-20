"""
Author: Abdullah Khan
File: Signals.py
Description: Handles making sure system calls and interrupts are valid.
"""

import re
import DeviceQueue
from ReadyQueue import *
from PretendSystem import cleanup
from PCB import ProcessControlBlock as PCB

def leave():
    print()
    cleanup()
    exit()


def snapshot_mode(system):
    print("Valid inputs: c, d, p, r")
    while True:
        print("Options: c-#, d-#, p-#")
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
            else:
                return
        elif valid_device(command):
            if command[0] == "c":
                system.print_device(system.discs)
                return
            elif command[0] == "d":
                system.print_device(system.disks)
                return
            elif command[0] == "p":
                system.print_device(system.printers)
                return
            else:
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

    try:
        if letter in switch_case:
            #  Get function from the switch_case dictionary
            function = switch_case.get(letter)
        else:
            print("Bad input.") #maybe send to device here
            return
    except TypeError:
        print("You broke it.")
        leave()

    return function(system)  # Return the function and execute it.


def send_to_device(command, system):
    if command[0] == 'c':
        if system.ready.cpu_is_empty():
            print("There isn't a process running.")
        elif int(command[1:]) > system.get_num_cdrw() - 1:
            print("Bad index. Remember we count from 0.")
        else:
            process = system.ready.cpu[0]
            system.discs[int(command[1:])].add(process)
            print("Process sent to %s." % command)
    elif command[0] == 'd':
        if system.ready.cpu_is_empty():
            print("There isn't a process running.")
        elif int(command[1:]) > system.get_num_disks() - 1:
            print("Bad index. Remember we count from 0.")
        else:
            process = system.ready.cpu[0]
            system.disks[int(command[1:])].add(process)
            print("Process sent to %s." % command)
    elif command[0] == 'p':
        if system.ready.cpu_is_empty():
            print("There isn't a process running.")
        elif int(command[1:]) > system.get_num_printers() - 1:
            print("Bad index. Remember we count from 0.")
        else:
            process = system.ready.cpu[0]
            system.printers[int(command[1:])].add(process)
            print("Process sent to %s." % command)
    else:
        print("Serious problem.")

"""
These are functions that will match inputs with regular expressions
to make sure the user doesn't break this program
"""


def valid_signal(pattern):
    """
    Return whether the pattern is a valid signal
    """
    return re.compile(r"^[AcdrSt]{1}$").match(pattern) is not None

def valid_device(pattern):
    """
    Return whether the pattern is a valid device
    """
    return re.compile(r"^[cdp][0-9]{1}$").match(pattern) is not None

def valid_complete(pattern):
    return re.compile(r"^[CDP][0-9]{1}$").match(pattern) is not None

def valid_readwrite(pattern):
    return re.compile(r"^[rw]{1}$").match(pattern) is not None