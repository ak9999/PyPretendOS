#!/usr/bin/python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem as pos
from ReadyQueue import ReadyQueue as rq

def leave():
    print()
    cleanup()
    exit()

def running_mode():
    global totally_real_system
    global sys_rq
    while True:
        print("C:\\>", end=" ")
        try:
            command = input()
        except KeyboardInterrupt:
            leave()
        except EOFError:
            leave()

        if valid_signal(command):
        	signal(command, sys_rq)
        else:
        	running_mode()


from PCB import ProcessControlBlock as pcb
from PretendSystem import cleanup
from Signals import *

totally_real_system = pos()
sys_rq = rq()
print()
print(totally_real_system)
running_mode()

cleanup()
exit()
