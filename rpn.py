#!/usr/bin/env python3

import sys
import operator
import readline
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def printInput(arg1,op,arg2,result):
    if arg1 < 0:
        arg1 = colored(arg1,'red')
    if arg2 < 0:
        arg2 = colored(arg2,'red')
    if result < 0:
        result = colored(result,'red')
    op = colored(op,'blue')
    print(arg1,op,arg2,"=",result)

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
            printInput(arg1,token,arg2,result)
    if len(stack) != 1:
        raise TypeError("Too many parametersss")
    return stack.pop()

def main():
    inp = ""
    while True:
        inp = input("rpn calc> ")
        if inp is "q":
            break
        result = calculate(inp)
       # print("Result: ", result)
    print("Thanks for using!")
if __name__ == '__main__':
    main()
