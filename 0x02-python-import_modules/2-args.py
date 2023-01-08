#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv
    args.pop(0)
    argc = len(args)
    line1 = "{:d} argument".format(argc)
    if argc == 0:
        line1 += "s."
    elif argc == 1:
        line1 += ":"
    else:
        line1 += "s:"
    print(line1)
    for i, arg in enumerate(args):
        print("{:d}: {:s}".format(i+1, arg))
