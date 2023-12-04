#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    operators = {'+': add, '-': sub, '*': mul,  '/': div}
    if sys.argv[2] in operators:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = operators[sys.argv[2]]
        print("{} {:s} {} = {}".format(a, sys.argv[2], b, op(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
