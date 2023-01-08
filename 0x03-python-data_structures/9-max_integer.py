#!/usr/bin/python3

def max_integer(my_list=[]):
    L = len(my_list)
    if L == 0:
        return None
    Max = my_list[0]
    for elem in my_list:
        if elem > Max:
            Max = elem
    return 
