#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number and list of arguments"""
    import sys  
    arguments = len(sys.argv) - 1

    if arguments == 0:
        print("{} arguments.".format(arguments))
    elif arguments == 1:
        print("{} argument:".format(arguments))
    else:
        print("{} arguments:".format(arguments))
    if arguments > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
