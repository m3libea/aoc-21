#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from utils import advent

def parse_line(line):
    split = line.split(" ")
    return [split[0], int(split[1])]

def get_position(directions):
    horizontal, depth, aim = 0, 0 ,0

    for command, value in directions:
        match command:
            case "forward":
                horizontal += value
                depth += value * aim 
            case "down":
                aim += value
            case "up":
                aim -= value

    return horizontal, depth, aim

if __name__ == '__main__':

    directions = advent.parse_input("input", parse_line)
    horizontal, depth, aim = get_position(directions)

    #Part 1: What do you get if you multiply your final horizontal position by your final depth? 
    #On this case aim = depth
    advent.print_answer(1, horizontal * aim)

    #Part 2: What do you get if you multiply your final horizontal position by your final depth? (with Aim)
    advent.print_answer(2, horizontal * depth)
