#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of addition of arguments"""
    from sys import argv  

    arguments = len(argv) - 1

    if arguments == 0:
        print("{}".format(arguments))
    else:
        total = 0
        for i in range(1, arguments + 1):
            total += int(argv[i])
        print("{}".format(total))
