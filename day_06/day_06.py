#!/usr/bin/env python3

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from utils import advent

def parse_line(line):
    return [int(fish) for fish in line.split(",") ]

def fish_after_days(initial_list, n):
    lives = [ 0 for i in range(9)]

    for fish in initial_list:
        lives[fish] += 1
    
    for i in range(n):
        aux = lives[0]

        for k in range(1,9):
            lives[k-1] = lives[k]
        
        lives[6] += aux
        lives[8] = aux

    return sum(fishes for fishes in lives)


if __name__ == '__main__':

    example = "3,4,3,1,2"

    line = parse_line(example)
    num = fish_after_days(line, 80)

    advent.print_answer(1, num)