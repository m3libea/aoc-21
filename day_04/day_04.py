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

    winning_remaining = []
    winning_num = []

    winners = set()

    all_winners = False
    for num in random_numbers:
        #for board in boards:
        for i in range(len(boards)):
            board = boards[i]
            winner = board.play_num(num)

            if winner and i not in winners:
                winning_remaining.append(board.calculate_remaining_sum())
                winning_num.append(num)
                winners.add(i)

            if len(winning_remaining) == len(boards):
                all_winners = True
                break 
    
    position = 0 if first else (len(winning_remaining) - 1)

    return winning_num[position], winning_remaining[position]

if __name__ == '__main__':

    random_numbers, boards = parse_input("example")

    winning_num, remaining = play_game(random_numbers, boards, True)
    advent.print_answer(1, winning_num * remaining)

    random_numbers2, boards2 = parse_input("example")
    winning_num2, remaining2 = play_game(random_numbers2, boards2, False)
    advent.print_answer(2, winning_num2 * remaining2)