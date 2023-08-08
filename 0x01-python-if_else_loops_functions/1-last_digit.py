#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulus = abs(number) % 10
if modulus > 5:
    print(f"Last digit of {number:d} is {modulus:d} and is greater than 5")
elif modulus in range(1,6):
    print(f"Last digit of {number:d} is {modulus:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {modulus:d} and is 0")
