#!/usr/bin/env python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem as pos
from ReadyQueue import ReadyQueue as rq
from DeviceQueue import *
from PCB import ProcessControlBlock as pcb
from PretendSystem import cleanup
from Signals import *


def leave():
    print()
    cleanup()
    exit()


def running():
    global totally_real_system
    while True:
        print("C:\\>", end=" ")
        try:
            command = input()
        except KeyboardInterrupt:
            leave()
        except EOFError:
            leave()

        if valid_signal(command):
            signal(command, totally_real_system)
        elif valid_device(command):
            send_to_device(command, totally_real_system)
        elif valid_complete(command):
            complete_process(command, totally_real_system)
        else:
            running()

totally_real_system = pos()
print("Reminder: We count devices starting with 0.\n")
running()

cleanup()
exit()
