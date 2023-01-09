#!/usr/bin/python3
import calculator_1 as calc
import sys

if __name__ == '__main__':
    args = sys.argv
    pname = args.pop(0)
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[1] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(args[0])
    b = int(args[2])
    funcs = (calc.add, calc.sub, calc.mul, calc.div)
    for op, func in zip('+-*/', funcs):
        if op == args[1]:
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, func(a, b)))
            break
