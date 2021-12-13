#!/usr/bin/env python3

import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent
from collections import defaultdict


def parse_line(line):
    return line.strip().split("-")

def create_graph(input):
    connections = advent.parse_input(input, parse_line)

    g = defaultdict(list)

    for c in connections:
        g[c[0]].append(c[1])
        g[c[1]].append(c[0])

    return g

def count_paths(graph, fr, visited, twice, counter = 0):
    if fr == 'end': 
        return 1
    for neighbord in graph[fr]:
        if neighbord.isupper(): 
            counter += count_paths(graph, neighbord, visited, twice)
        else:
            if neighbord not in visited:
                counter += count_paths(graph, neighbord, visited | {neighbord}, twice)
            elif twice and neighbord not in {'start', 'end'}:
                counter += count_paths(graph, neighbord, visited, False)
    return counter

def solution(input):
    print("Solution for: " + input)
    g = create_graph(input)
    advent.print_answer(1, count_paths(g, "start", {"start"}, False))
    advent.print_answer(2, count_paths(g, "start", {"start"}, True))    

if __name__ == '__main__':
    solution("example")

    solution("input")

