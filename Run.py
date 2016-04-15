#!/usr/bin/env python3

"""
Author: Abdullah Khan
Program: Run.py
Description: Simulates an operating system and system hardware.
Build instructions: Make sure Run.py is executable and run it.
"""

from PretendSystem import PretendSystem
import Signals


def leave():
    print()
    Signals.cleanup()
    exit()


def running():
    totally_real_system = PretendSystem()
    while True:
        print('$', end=' ')
        try:
            command = input()
        except KeyboardInterrupt:
            Signals.leave()
        except EOFError:
            Signals.leave()

        if Signals.valid_signal(command):
            Signals.signal(command, totally_real_system)
            totally_real_system.sjf()
        elif Signals.valid_device(command):
            Signals.send_to_device(command, totally_real_system)
        elif Signals.valid_complete(command):
            Signals.complete_process(command, totally_real_system)
            totally_real_system.sjf()
            pass


def main():
    running()

if __name__ == '__main__':
    main()
