#!/usr/bin/python3

def new_in_list(my_list, idx, elem):

    copy = my_list[:]
    if idx < 0 or idx >= len(copy):
        return copy
    copy[idx] = elem
    return copy
