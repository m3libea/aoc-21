#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from utils import advent

def parse_input(input):
    with open(input, 'r') as file:
        lines = [parse_line(line) for line in file.readlines()]
    return lines

def parse_line(line):
    splitted = line.split(" ")
    return [splitted[0], int(splitted[1])]

def get_position(directions):
    horizontal = 0
    depth = 0
    for move in directions:
        if move[0] == "forward":
            horizontal += move[1]
        else:
            direction = 1 if move[0] == "down" else -1
            depth += direction * move[1] 

    return [horizontal, depth]


if __name__ == '__main__':

    directions = parse_input("input")
    position = get_position(directions)

    total = position[0] * position[1]

    advent.print_answer(1, total)
