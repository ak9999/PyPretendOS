Author: Abdullah Khan
Assignment 3

How to run this program:
python3.4 __main__.py
or python3.3 __main__.py if running in the Linux Lab.

New:
* Added kill command.

Broken/absent:
* Frame list.
* Page table.

On every system call or interrupt, if there is a process in the CPU,
the timer (you) will have to say how long that process was using the CPU.

When you want to see what is in the queues, you type 'S', you may or may not
be prompted to enter the length of the CPU burst, and then you can type in which
queue you want to see, r (ready), c (disc), d (disk), p (printer).

When creating disk queues, you cannot have zero cylinders. When sending PCBs to
disk queues, when it comes to choosing a cylinder, multiple PCBs can be on the
same cylinder. When choosing a cylinder, you will choose between [0, size-1].

That is, if a disk queue has 3000 cylinders, you choose between 0 and 2999.

If you send a KeyboardInterrupt (^C) the program will stop and you will see a
Traceback message, and it will be a big mess. This is intended, I'm assuming
that if you hit Ctrl-C you want the program to stop and you don't care what
happens.
