#!/usr/bin/python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem as pos

import shutil

totally_real_system = pos()  # Construct system!
print()
totally_real_system.printsys()

# Clean up the pycache
try:
    shutil.rmtree("__pycache__")
except FileNotFoundError:
    print("Failed to remove __pycache__ directory")
