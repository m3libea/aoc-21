#!/usr/bin/env python3
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from utils import advent

easy_numers = {
    2 : 2,
    4 : 4,
    3 : 7,
    7 : 8
}

appareances = {
    6 : "b",
    4 : "e",
    9 : "f"
}

numbers = {
    "abcefg" : "0",
    "cf" : "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

def parse_line(line):
    split = line.strip().split(" | ")

    return [split[0].split(), split[1].split()]

def get_easy_digits(input):
    total = 0
    for pattern, output in input:
        for num in output:
            if len(num) in easy_numers:
                total +=1
    
    return total

def get_letters_wiring(numbers):

    easy_numers_local = {}
    letters_count = {}
    letter_wiring = {}

    for num in numbers:
        #Identify easy numbers 
        if len(num) in easy_numers:
            easy_numers_local[easy_numers[len(num)]] = num
        #count letters
        for l in num:
            if l in letters_count:
                letters_count[l] += 1
            else:
                letters_count[l] = 1
    
    #identify letters
    for letter, count in letters_count.items():
        #letter check on appareances
        if count in appareances:
            letter_wiring[letter] = appareances[count]
        else:
            if count == 7:
                #Check if b -> check if letter in 4
                if letter in easy_numers_local[4]:
                    letter_wiring[letter] = "d"
                else:
                    letter_wiring[letter] = "g"
            if count == 8:
                #Check a -> ! in 4 
                if letter not in easy_numers_local[4]:
                    letter_wiring[letter] = "a"
                else:
                    letter_wiring[letter] = "c"
    
    return letter_wiring

def get_number(line):
    wiring = get_letters_wiring(line[0])
    result = ""

    for num in line[1]:
        original = ""
        for l in num:
            original += wiring[l]
        
        result += numbers["".join(sorted(original))]
    
    return int(result)

def solution(input):
    total = 0

    for line in input:
        total += get_number(line)
    
    return total

if __name__ == '__main__':

    lines = advent.parse_input("input", parse_line)

    total = get_easy_digits(lines)
    advent.print_answer(1, total)

    total_part_two = solution(lines)
    advent.print_answer(2, total_part_two)
