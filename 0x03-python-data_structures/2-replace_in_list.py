#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
      return my_list[idx]
    if idx > len(my_list):
      return my_list[idx]
    my_list[idx] = elem
    return(my_list)
