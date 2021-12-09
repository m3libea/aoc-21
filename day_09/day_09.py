#!/usr/bin/env python3
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent

def parse_line(line):
    return line.split("")

if __name__ == '__main__':
    lines = advent.parse_input("example", parse_line)
    advent.print_answer(1, lines)