#!/usr/bin/python3

def print_list_integer(my_list=[]):
"""
    Prints integers in a list
    Arguments:
        my_list - list of integers default []
    """
    for i in my_list:
        print("{:d}".format(i))
