#!/usr/bin/python3

def no_c(my_str):
    return "".join(filter(lambda x: x not in 'cC', my_str))
