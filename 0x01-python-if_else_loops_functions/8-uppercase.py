#!/usr/bin/python3
def uppercase(str):
    "A function that prints a string in uppercase "
    newStr = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            newStr += chr(ord(c) - 32)
        else:
            newStr += c
    print(newStr)
