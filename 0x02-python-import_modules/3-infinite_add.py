#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv
    args.pop(0)
    print(sum(map(int, args)))
