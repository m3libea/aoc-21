#!/usr/bin/env python3

import sys
sys.path.insert(0, '../')
from utils import advent
from board import Board

def parse_input(input):
    with open(input, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != ""]

    random_numbers = [int(num) for num in lines[0].split(",")]
    boards = []

    board_numbers = []
    for i in range(1,len(lines)):
        row = [int(num) for num in lines[i].split()]
        board_numbers.append(row)

        if i % 5 == 0:
            board = Board()
            board.add_numbers(board_numbers)
            boards.append(board)
            board_numbers = []

    return random_numbers, boards

def play_game(random_numbers, boards, first):
 
    min_pos = len(random_numbers)
    min_remaining = 0
    min_winning = 0

    max_pos = 0
    max_remaining = 0
    max_winning = 0

    for board in boards:
        for i in range(len(random_numbers)):
            num = random_numbers[i]
            winner = board.play_num(num)

            if winner:
                if i < min_pos:
                    min_pos = i 
                    min_remaining = board.calculate_remaining_sum()
                    min_winning = num
                    # print(min_pos)
                    # print(i)
                if i > max_pos:
                    max_pos = i
                    max_remaining = board.calculate_remaining_sum()
                    max_winning = num
                break

    if first:
        return min_winning, min_remaining
    else:
        return max_winning, max_remaining

if __name__ == '__main__':

    random_numbers, boards = parse_input("input")
    winning_num, remaining = play_game(random_numbers, boards, True)
    advent.print_answer(1, winning_num * remaining)

    random_numbers2, boards2 = parse_input("input")
    winning_num2, remaining2 = play_game(random_numbers2, boards2, False)
    advent.print_answer(2, winning_num2 * remaining2)