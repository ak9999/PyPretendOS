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


def snapshot_mode(q):
    print("Valid inputs: c, d, p, r")
    while True:
        print("S-", end="")
        try:
            command = input()
        except KeyboardInterrupt:
            leave()
        except EOFError:
            leave()

        if valid_signal(command):
            if command[0] == "r":
                q.print_queue()
                return
            elif command[0] == "c":
                #  print(queue)
                return  #  Gotta add device queues
            elif command[0] == "d":
                #  print(queue)
                return  #  Gotta add device queues
            elif command[0] == "p":
                #  print(queue)
                return  #  Gotta add device queues
            else:
                return

        else:
            return


def snapshot(rq):
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
            print("Bad input.") #maybe send to device here
            return
    except TypeError:
        print("You broke it.")
        leave()

    return function(rq)  # Return the function and execute it.


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