#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulus = number % 10
print(f"Last digit of {number:d} is {modulus:d} and", end=" ")
if modulus > 5:
    print("is greater than 5")
elif modulus == 0:
    print("is less than 6 and not 0")
else:
    print("is less than 6 and not 0")
