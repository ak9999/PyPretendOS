"""
Author: Abdullah Khan
File: Signals.py
Description: Handles making sure system calls and interrupts are valid.
"""

import re
import CPU
import DeviceQueue

def terminate(cpu):
    cpu.remove()

def arrival(cpu):
    cpu.add()

def snapshot(cpu):
    print("Select queue to display (c, d, p, r): ", end=" ")
    pattern = input()
    if valid_snapshot(pattern):
        snap_signal(pattern)
    else:
        print("Bad input, try again.")
        snapshot(cpu)

def signal(letter):
    """
    Python does not have switch/cases like C++, but we can
    use dictionaries to mimic that functionality.
    """
    switch_case = \
        {
            "A" : arrival(), #  put PCB into ready queue
            "S" : snapshot(),
            "t" : terminate()
        }

    #  Get function from the switch_case dictionary
    function = switch_case.get(letter)

    return function()  # Return the function and execute it.

def snap_signal(letter):
    switch_case = \
        {
            #  Print respective queues
            "c" : print(),
            "d" : print(),
            "p" : print(),
            "r" : print()           
        }

    #  Get function from the switch_case dictionary
    function = switch_case.get(letter)

    return function()  # Return the function and execute it.

def complete_signal(dq, pattern):
    switch_case = \
        {
            #  Print respective queues
            r"^[C][0-9]{1}$" : dq.task_complete(),
            r"^[D][0-9]{1}$" : dq.task_complete(),
            r"^[P][0-9]{1}$" : dq.task_complete()       
        }

    #  Get function from the switch_case dictionary
    function = switch_case.get(letter)

    return function()  # Return the function and execute it.


def valid_signal(pattern):
    """
    Return whether the pattern is a valid signal
    """
    return re.compile(r"^[AcdrSt]{1}$").match(pattern) is not None

def valid_device(pattern):
    """
    Return whether the pattern is a valid device
    """
    return re.compile(r"^[cdpr][0-9]{1}$").match(pattern) is not None

def valid_complete(pattern):
    """
    Return whether the pattern is a valid device
    """
    return re.compile(r"^[CDP][0-9]{1}$").match(pattern) is not None

def valid_snapshot(pattern):
    return re.compile(r"^[cdpr]{1}$").match(pattern) is not None

def valid_complete(pattern):
    return re.compile(r"^[CDP][0-9]{1}$").match(pattern) is not None
