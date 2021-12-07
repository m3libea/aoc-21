#!/usr/bin/env python3

import numpy as np
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent

def parse_line(line):
    return [int(position) for position in line.split(",") ]

def get_cost(input):
    median = int(np.median(input))
    total = sum(abs(position - median) for position in input)

    return total

# Fuel cost: n * (n+1)/2
def get_cost_part_two(input):
    average = int(np.mean(input))
   
    total = 0
    for num in input:
        n = abs(num - average)
        total += (n * (n + 1)) // 2
    return total

if __name__ == '__main__':

    example = "16,1,2,0,4,2,7,1,2,14"
    positions_example = parse_line(example)

    positions = advent.parse_input("input", parse_line)

    part_one = get_cost(positions[0])
    advent.print_answer(1, part_one)

    part_two = get_cost_part_two(positions[0])
    advent.print_answer(2, part_two)