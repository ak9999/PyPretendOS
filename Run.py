#!/usr/bin/python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem as pos
from ReadyQueue import ReadyQueue

def leave():
    print()
    cleanup()
    exit()

def running_mode():
    while True:
        print("C:\\", end=" ")
        try:
            command = input()
        except KeyboardInterrupt:
            leave()
        except EOFError:
            leave()


from PCB import ProcessControlBlock as pcb
from PretendSystem import cleanup
from Signals import *

totally_real_system = pos()
print()
running_mode()

cleanup()
exit()
