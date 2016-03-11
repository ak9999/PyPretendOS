#!/usr/bin/python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem as pos
import ReadyQueue

totally_real_system = pos()  # Construct system!
print()

from PCB import ProcessControlBlock as pcb
from PCB import create_block

nah = pcb()
create_block(nah)
print(nah)
print()

rq = ReadyQueue()
