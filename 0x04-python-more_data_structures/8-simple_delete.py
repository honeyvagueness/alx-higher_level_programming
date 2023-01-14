#!/usr/bin/python3

def simple_delete(a_dict, key=""):

    if a_dict is None:
        return None
    if key in a_dict:
        del a_dict[key]
    return a_dict
