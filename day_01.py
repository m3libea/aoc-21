#!/usr/bin/env python3

import advent

with open('input/day_01.txt', 'r') as submarine_report:
    depths = [int(line) for line in submarine_report.readlines()]

def solution(input, window): 
    return sum(b > a for a, b in zip(input, input[window:]))

#Question 1 - Total measurements larger than the previous measurement
advent.print_answer(1, solution(depths, 1))

#Question 2 - The number of times the sum of measurements in this sliding window increases
advent.print_answer(2, solution(depths, 3))
