"""
Author: Abdullah Khan
File: Signals.py
Description: Handles making sure system calls and interrupts are valid.
"""

import re
import DeviceQueue
import ReadyQueue

def terminate(cpu):
    cpu.remove()

def arrival(cpu):
    cpu.add()

def signal(letter):
    """
    Python does not have switch/cases like C++, but we can
    use dictionaries to mimic that functionality.
    """
    switch_case = \
        {
            "A": arrival(cpu),  # put PCB into ready queue
            "S": snapshot(cpu),
            "t": terminate(cpu)
        }

    #  Get function from the switch_case dictionary
    function = switch_case.get(letter)

    return function(cpu)  # Return the function and execute it.


def snap_signal(letter):
    switch_case = \
        {
            #  Print respective queues, where dq is a device queue
            "c" : print(dq),
            "d" : print(dq),
            "p" : print(dq),
            "r" : print(dq)           
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
    function = switch_case.get(pattern)

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
    return re.compile(r"^[cdp][0-9]{1}$").match(pattern) is not None

def valid_snapshot(pattern):
    return re.compile(r"^[cdpr]{1}$").match(pattern) is not None

def valid_complete(pattern):
    return re.compile(r"^[CDP][0-9]{1}$").match(pattern) is not None

def valid_readwrite(pattern):
    return re.compile(r"^[rw][0-9]{1}$").match(pattern) is not None
