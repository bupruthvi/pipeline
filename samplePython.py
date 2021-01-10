#!/Users/Pruthvi/.virtualenvs/practicepython/bin/python

import argparse
import os
import sys

def get_user_inputs(inputs):
    return inputs

def get_top_ten_process(top):
    return top

def add_two_values(a,b):
    return a + b

def sub_two_values(a,b):
    return a - b

def mul_two_values(a,b):
    return a * b

def div_two_values(a,b):
    if b > 0:
        return a // b
    else:
        print('denominator should be greater than 0')
        sys.exit(1)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', default=1, type=int, help='add number1 to add to the other. Default is 1')
    parser.add_argument('-b', '--b', default=0, type=int, help='add number2 to add to the other. Default is 0 and this is optional')
    

    args = parser.parse_args()
    a, b = args.a, args.b

    if os.getenv('add').lower() == 'true':
        print(add_two_values(a,b))
    
    if os.getenv('subtract').lower() == 'true':
        print(sub_two_values(a,b))
    
    if os.getenv('divide').lower() == 'true':
        print(div_two_values(a,b))
    
    if os.getenv('multiply').lower() == 'true':
        print(mul_two_values(a,b))
    
    