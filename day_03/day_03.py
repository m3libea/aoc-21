#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from utils import advent

def parse_line(line):
    split = [int(char) for char in line.strip()]
    return split

def power_consumption(lines):
    number_size = len(lines[0])
    half = int(len(lines)/2)
    ones = [ 0 ] * number_size

    gamma = ""
    epsilon = ""

    for line in lines:
        for i in range(number_size):
            ones[i] += line[i]     

    for x in ones: 
        if(x > half):
            gamma += "1"
            epsilon += "0"
        else:
            epsilon += "1"
            gamma += "0"

    return int(gamma, 2), int(epsilon, 2)

if __name__ == '__main__':

    lines = advent.parse_input("input", parse_line)

    gamma, epsilon = power_consumption(lines)
    advent.print_answer(1, gamma * epsilon)