#!/usr/bin/python3

import re
from functools import reduce

class latex_to_python():

    #(syntax, repl, addtional regex pattern)
    syntax = [(r'\\frac', '\g<1>/\g<3>', '{(.+?({.*})*)}'),
              ('\^', '**\g<1>', ''),]
    patterns = []

    def __init__(self):
        self.patterns = tuple(map(self.pattern_gen, self.syntax))

    def pattern_gen(self, s):
        """
        generate : r'\syntax{}' + r'%s'
        """

        #+?    : non-greedy of +
        #{.*}* : avoid match in the main {}

        return (r'%s{(.+?({.*})*)}%s' % (s[0], s[2]), s[1])

    def replace(self, string, s_tuple):
        """
        string  : string to be used in replacement
        s_tuple : (pattern, repl)
        """
        return re.sub(s_tuple[0], s_tuple[1], string)

    def convert(self, expression):
        return reduce(self.replace, self.patterns, expression)

if __name__ == '__main__':
    to_python = latex_to_python().convert
    while(True):
        expression = input("Please input your latex expression: ")
        print(to_python(expression))
        try:
            print(eval(to_python(expression)))
        except:
            print("expression not evaluatable")
