#!/usr/bin/env python3

with open('input/day_01.txt', 'r') as submarine_report:
    depths = [int(line) for line in submarine_report.readlines()]


prev = int(depths[0])
total = 0
for depth in depths[1:]:
    if prev < depth:
        total += 1
    prev = int(depth)

#Question 1 - Total measurements larger than the previous measurement
print("Solution: " + str(total))