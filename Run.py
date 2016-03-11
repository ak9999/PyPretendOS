#!/usr/bin/python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem as pos

totally_real_system = pos()  # Construct system!
print()

from PCB import ProcessControlBlock as pcb
from PCB import create_block

new_item = pcb()
create_block(new_item)
print(new_item)
print()
