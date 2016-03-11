#!/usr/bin/python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem as pos
from ReadyQueue import ReadyQueue

totally_real_system = pos()  # Construct system!
print()

from PCB import ProcessControlBlock as pcb
from PretendSystem import cleanup

nah = pcb()
nah.filename = "executable"
nah.file_length = "7"
hey = pcb()
hey.filename = "why"
hey.file_length = "5"
print()

rq = ReadyQueue()
rq.add(hey)
print()
rq.add(nah)
rq.print_queue()

cleanup()