#!/usr/bin/env python3

def print_answer(part, answer):
    print('Part {}: {}'.format(part, answer))

#Parse input line by line using a given function for the line
def parse_input(input, parse_line):
    with open(input, 'r') as file:
        lines = [parse_line(line) for line in file.readlines()]
    return lines