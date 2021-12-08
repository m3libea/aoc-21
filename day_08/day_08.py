#!/usr/bin/env python3
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent

def parse_line(line):
    split = line.strip().split(" | ")

    return [split[0].split(), split[1].split()]

def get_dictionary():
    digits = {}

    digits[2] = 2
    digits[4] = 4
    digits[3] = 7
    digits[7] = 8

    return digits

def get_easy_digits(input, dictionary):
    total = 0
    for pattern, output in input:
        for num in output:
            if len(num) in dictionary:
                total +=1
    
    return total

if __name__ == '__main__':

    lines = advent.parse_input("input", parse_line)

    total = get_easy_digits(lines, get_dictionary())
    advent.print_answer(1, total)