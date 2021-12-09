#!/usr/bin/env python3

import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent

from functools import reduce

#COMMON
visited = set()
grid = []
n, m = 0, 0

def parse_line(line):
    return [int(c) for c in line.strip()]

def check_low(row, col):
    minimum = sys.maxsize
    height = grid[row][col]
    neighbors = ((row + 1, col), (row - 1, col) , (row, col + 1), (row, col - 1))
    for ni, nj in neighbors:
        if 0 <= ni < n and 0 <= nj < m:
            minimum = min(minimum, grid[ni][nj])
            if minimum <= height:
                return 0
    
    return height + 1

def risk_levels(): 
    total = 0
    for i in range(n):
        for j in range(m):
            total += check_low(i, j)
    return total

def dfs(row, col):
    area = 1
    neighbors = ((row + 1, col), (row - 1, col) , (row, col + 1), (row, col - 1))

    for ni, nj in neighbors:
        if 0 <= ni < n and 0 <= nj < m and (ni,nj) not in visited and grid[ni][nj] != 9:
            visited.add((ni, nj))
            area += dfs(ni, nj)
    return area
        
def max_basins():
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 9 and (i,j) not in visited:
                visited.add((i, j))
                result.append(dfs(i,j))

    return reduce((lambda x, y: x * y), sorted(result)[-3:])

if __name__ == '__main__':

    grid = advent.parse_input("input", parse_line)
    n, m = len(grid), len(grid[0])

    example_grid = advent.parse_input("example", parse_line)

    part_one = risk_levels()
    advent.print_answer(1, part_one)

    part_two = max_basins()
    advent.print_answer(2, part_two)