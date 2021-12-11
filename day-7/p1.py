# https://adventofcode.com/2021/day/7
from utils.utils import get_lines_from_file

lines = get_lines_from_file('day-7/input')
input = lines[0].split(',')
input = [int(x) for x in input]
fuel = 999999999  # inf

for i in range(len(input)):
    cost = 0

    for j in range(len(input)):
        cost += abs(i - input[j])
    if cost < fuel:
        fuel = cost
        pos = i

print(f"fuel: {fuel}")
