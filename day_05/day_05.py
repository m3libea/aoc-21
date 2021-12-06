#!/usr/bin/env python3

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from utils import advent
from line import Line
from collections import defaultdict


def parse_line(line):
    split = line.strip().split(" -> ") 
    start = [int(num) for num in split[0].split(",")]
    end = [int(num) for num in split[1].split(",")]

    return Line(start, end)
    
def calculate_overlap(lines, diagonals):
  grid = defaultdict(int)
  
  for line in lines:
    start = line.start
    end = line.end

    #Calculate line direction 
    x_step = (end[0] - start[0]) // max(1, abs(end[0] - start[0]))
    y_step = (end[1] - start[1]) // max(1, abs(end[1] - start[1]))

    if line.isVertical():
        for y in range(start[1], end[1] + y_step, y_step):
            grid[(start[0], y)] += 1

    elif line.isHorizontal():
        for x in range(start[0], end[0] + x_step, x_step):
            grid[(x, start[1])] += 1

    elif diagonals:
        #zip returns x,y that creates the lines
        for x, y in zip(range(start[0], end[0] + x_step, x_step), range(start[1], end[1] + y_step, y_step)):
            grid[(x, y)] += 1

  return sum(1 if x > 1 else 0 for x in grid.values())


if __name__ == '__main__':
    lines = advent.parse_input("input", parse_line)

    part1 = calculate_overlap(lines, False)
    advent.print_answer(1, part1)

    part2 = calculate_overlap(lines, True)
    advent.print_answer(2, part2)
    