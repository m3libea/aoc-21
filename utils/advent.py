#!/usr/bin/env python3

def print_answer(part, answer):
    print('Part {}: {}'.format(part, answer))

def read_numbers_lines(input):
    with open(input, 'r') as file:
        lines = [int(line) for line in file.readlines()]
    return lines

#Parse input line by line using a given function for the line
def parse_input(input, parse_line):
    with open(input, 'r') as file:
        lines = [parse_line(line) for line in file.readlines()]
    return lines