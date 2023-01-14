#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    s_xy = sum(map(lambda a: a[0] * a[1], my_list))
    s_x = sum(map(lambda a: a[1], my_list))
    return s_xy / s_x


if __name__ == '__main__':
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
