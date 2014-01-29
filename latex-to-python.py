#!/usr/bin/python3

import re
from functools import reduce, partial

def pattern_gen(s):
    """
    generate : r'\syntax{}' + r'%s'
    """

    #+?    : non-greedy of +
    #{.*}* : avoid match in the main {}

    return (r'%s{(.+?({.*})*)}%s' % (s[0], s[2]), s[1])

def replace(string, s_tuple):
    """
    string  : string to be used in replacement
    s_tuple : (pattern, repl)
    """
    return re.sub(s_tuple[0], s_tuple[1], string)

def convert(patterns, expression):
    return reduce(replace, patterns, expression)

def main():
    #(syntax, repl, addtional regex pattern)
    syntax = [(r'\\frac', '\g<1>/\g<3>', '{(.+?({.*})*)}'),
              ('\^', '**\g<1>', ''),]
    patterns = tuple(map(pattern_gen, syntax))

    to_python = partial(convert, patterns)
    while(True):
        expression = input("Please input your latex expression: ")
        print(to_python(expression))
        try:
            print(eval(to_python(expression)))
        except:
            print("expression not evaluatable")

if __name__ == '__main__':
    main()
