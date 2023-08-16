#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number and list of arguments"""
    from sys import argv
    arguments = len(argv) - 1

    if arguments == 0:
        print("{} arguments.".format(arguments))
    elif arguments == 1:
        print("{} argument:".format(arguments))
    else:
        print("{} arguments:".format(arguments))
    if arguments > 0:
        for i in range(arguments):
            print("{}: {}".format(i + 1, argv[i + 1]))
