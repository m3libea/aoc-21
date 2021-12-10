#!/usr/bin/env python3

import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent
from stack import Stack

#Globals
symbols = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}

error_score = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

def parse_line(line):
    return line.strip()

def classify_lines(input):
    corrupted = []
    incomplete = []

    for i, line in enumerate(input):
        stack = Stack()
        corrupted_line = False
        for s in line:
            if s in symbols:
                stack.push(s)
            else:
                if s == symbols[stack.peek()]:
                    stack.pop()
                else:
                    corrupted.append(s)
                    corrupted_line = True
                    break
        
        if not corrupted and not stack.isEmpty():
            incomplete.append(i)
    return corrupted, incomplete
            
def calculate_score(corrupted):
    total = 0

    for symbol in corrupted:
        total += error_score[symbol]
    return total

if __name__ == '__main__':

    lines_example = advent.parse_input("example", parse_line)
    corrupted_e, incomplete_e = classify_lines(lines_example)    

    lines = advent.parse_input("input", parse_line)

    corrupted, incomplete = classify_lines(lines)    
    advent.print_answer(1, calculate_score(corrupted))