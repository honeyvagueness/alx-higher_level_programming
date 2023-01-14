#!/usr/bin/python3

def print_sorted_dictionary(a_dict):

    if a_dict is None:
        return None
    for key in sorted(a_dict.keys()):
        print("{:s}: {}".format(key, a_dict[key]))


if __name__ == '__main__':
    a_dictionary = {
        'language': "C", 'Number': 89,
        'track': "Low level", 'ids': [1, 2, 3]
    }
    print_sorted_dictionary(a_dictionary)
