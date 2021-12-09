#!/usr/bin/env python3
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent



def parse_line(line):
    return [int(c) for c in line.strip()]

def check_low(grid, row, col):
    n, m = len(grid), len(grid[0])

    minimum = sys.maxsize
    height = grid[row][col]
    neighbors = ((row + 1, col), (row - 1, col) , (row, col + 1), (row, col - 1))
    for i, j in neighbors:
        if 0 <= i < n and 0 <= j < m:
            minimum = min(minimum, grid[i][j])
            if minimum <= height:
                return 0
    
    return height + 1

def risk_levels(grid): 
    n, m = len(grid), len(grid[0])
    visited = set()

    total = 0
    for i in range(n):
        for j in range(m):
            visited.add((i, j))
            total += check_low(grid,i, j)
    return total

def initialize(input):
    n = len(grid)
    m = len(grid[0])

if __name__ == '__main__':

    grid = advent.parse_input("input", parse_line)

    part_one = risk_levels(grid)
    advent.print_answer(1, part_one)