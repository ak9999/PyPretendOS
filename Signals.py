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

def snapshot(rq):
    #  Enter snapshot mode
    #rq.print_queue()
    snapshot_mode(rq)
    return

def terminate(rq):
    rq.remove()
    return

def arrival(rq):
    pcb = PCB()
    rq.add(pcb)
    return

def signal(letter, rq):
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
            print("Bad input.")
            return
    except TypeError:
        print("You broke it.")
        leave()

    return function(rq)  # Return the function and execute it.


def snap_signal(letter, dq):
    switch_case = \
        {
            #  Print respective queues, where dq is a device queue
            "c" : print,
            "d" : print,
            "p" : print,
            "r" : print           
        }

    #  Get function from the switch_case dictionary
    function = switch_case.get(letter)

    return function(dq)  # Return the function and execute it.

def complete_signal(pattern):
    switch_case = \
        {
            #  Print respective queues
            r"^[C][0-9]{1}$" : task_complete,
            r"^[D][0-9]{1}$" : task_complete,
            r"^[P][0-9]{1}$" : task_complete       
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

def valid_complete(pattern):
    return re.compile(r"^[CDP][0-9]{1}$").match(pattern) is not None

def valid_readwrite(pattern):
    return re.compile(r"^[rw]{1}$").match(pattern) is not None

def snapshot_mode(q):
    print("Entering snapshot mode.")
    print("Hit the wrong button to leave.")
    while True:
        print("S:\\>", end=" ")
        try:
            command = input()
        except KeyboardInterrupt:
            leave()
        except EOFError:
            leave()

        if valid_signal(command):
            if command[0] == "r":
                q.print_queue()
            else:
                #  device queues
                return

        else:
            return