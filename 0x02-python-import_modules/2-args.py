#!/usr/bin/python3
from sys import argv
arguments = len(argv) - 1

if arguments == 1:
    print("{} argument".format(arguments))
else:
    print("{} arguments".format(arguments))

if arguments > 0:
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
