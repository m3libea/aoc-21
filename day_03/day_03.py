#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from utils import advent

from trie import Trie

def parse_line(line):
    split = [int(char) for char in line.strip()]
    return split

def calculate_common(lines):
    number_size = len(lines[0])
    half = int(len(lines)/2)
    ones = [ 0 ] * number_size

    for line in lines:
        for i in range(number_size):
            ones[i] += line[i]  
    
    result = []
    for x in ones: 
        if(x >= half):
            result.append(1)
        else:
            result.append(0)

    return result

def power_consumption(lines):

    common = calculate_common(lines)  
    gamma = ""
    epsilon = ""

    for x in common: 
        if(x == 1):
            gamma += "1"
            epsilon += "0"
        else:
            epsilon += "1"
            gamma += "0"

    return int(gamma, 2) * int(epsilon, 2)

def oxygen_co2(lines):
    trie = Trie(lines)

    oxigen = search(trie.root, True)
    co2 = search(trie.root, False)

    return int(oxigen,2) * int(co2, 2)

def search(trienode, common):
    if trienode.isLeaf:
        return ""

    element = ""
    check = [0, 0] if common else [0, trienode.total]
    both = 0

    for i in range(2):
        child = trienode.children[i]
        if child != None:
            both +=1
            if common:
                if check[1] <= child.total:
                    check = [i, child.total]
            else:
                if check[1] >= child.total:
                    check = [i, child.total]

    bit = check[0]

    #Check when we have equal numbers on both sides.
    if both == 2 and check[1] == trienode.total/2:
        bit = 1 if common else 0  

    return str(bit) + search(trienode.children[bit], common)


if __name__ == '__main__':

    lines = advent.parse_input("input", parse_line)

    total = power_consumption(lines)
    advent.print_answer(1, total)

    result = oxygen_co2(lines)
    advent.print_answer(2, result)
