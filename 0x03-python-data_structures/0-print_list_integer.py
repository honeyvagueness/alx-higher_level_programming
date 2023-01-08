#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints integers in a list
    Args:
        my_list - list of integers defauult []
    """
    for i in my_list:
        print("{:d}".format(i))
