#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 0 else number % -10
if (last_digit > 5):
    result = "greater than 5"
elif (last_digit == 0):
    result = "is 0"
else:
    result = "less than 6 and not 0"
print("Last digit of %s is %s and is %s" %(number, last_digit, result))
