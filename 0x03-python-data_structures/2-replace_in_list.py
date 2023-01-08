#!/usr/bin/python3
def replace_in_list(my_list, idx, elem):
    """
    replace an elment from a list at index idx with elem
    Args:
        my_list - list to search
        idx - the position to access
        elem - new elem to swap with
    Return:
        my_list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = elem
    return my_list
