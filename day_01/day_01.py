#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from utils import advent

def solution(input, window): 
    return sum(b > a for a, b in zip(input, input[window:]))

if __name__ == '__main__':

    depths = advent.read_numbers_lines("input")

    #Question 1 - Total measurements larger than the previous measurement
    advent.print_answer(1, solution(depths, 1))

    #Question 2 - The number of times the sum of measurements in this sliding window increases
    advent.print_answer(2, solution(depths, 3))