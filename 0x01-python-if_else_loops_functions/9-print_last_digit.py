#!/usr/bin/python3
def print_last_digit(number):
    drew = number % 10 if number > 10 else number * -1 % 10
    print("{:d}".format(drew), end="")
    return (drew)
