#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulus = abs(number) % 10
if number < 0:
    modulus = -modulus
print(f"Last digit of {number:d} is {modulus:d} and", end=" ")
if modulus > 5:
    print("is greater than 5")
elif modulus in range(1, 6):
    print("is less than 6 and not 0")
else:
    print("is 0")
