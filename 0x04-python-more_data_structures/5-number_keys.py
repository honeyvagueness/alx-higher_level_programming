#!/usr/bin/python3

def number_keys(a_dict):

    if a_dict is None:
        return None
    return len(a_dict.keys())


if __name__ == '__main__':
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
