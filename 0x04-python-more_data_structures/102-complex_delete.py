#!/usr/bin/python3

def complex_delete(a_dict, value):
   
    if a_dict is None:
        return None
    del_key = None
    keys = tuple(a_dict.keys())
    for key in keys:
        if a_dict[key] == value:
            del a_dict[key]
    return a_dict


if __name__ == '__main__':
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print(a_dictionary)
    print("--")
    print(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print(a_dictionary)
    print("--")
    print(new_dict)
