#!/usr/bin/env python3

import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent

#global vars
flashed = set()
grid = []
n, m = 0, 0

def parse_line(line):
    return [int(c) for c in line.strip()]

def calculate_flashes(steps):
    flashes = 0
    
    for step in range(steps):
        flashed.clear()
        for i in range(n):
            for j in range(m):
                flashes += dfs(i,j)
    return flashes

def dfs(row, col):
    if grid[row][col] == 0 and (row, col) in flashed:
        return 0

    if grid[row][col] != 9:
        grid[row][col] += 1
        return 0
   
    grid[row][col] = 0
    flashed.add((row, col))
    flashes = 1

    neighbors = ((row + 1, col), (row - 1, col), (row + 1, col + 1), (row - 1, col + 1) , 
    (row, col + 1), (row, col - 1), (row + 1, col - 1), (row - 1, col - 1))

    for ni, nj in neighbors:
        if 0 <= ni < n and 0 <= nj < m:
            flashes += dfs(ni, nj)

    return flashes

if __name__ == '__main__':

    grid = advent.parse_input("input", parse_line)
    n, m = len(grid), len(grid[0])

    flashes = calculate_flashes(100)
    advent.print_answer(1, flashes)
    advent.print_grid(grid)