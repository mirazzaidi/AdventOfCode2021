
from utils.utils import get_lines_from_file

fuel = 999999999 # inf

lines = get_lines_from_file('day-7/input')
input = lines[0].split(',')
input = [int(x) for x in input]

for i in range(len(input)):
    cost = 0

    for j in range(len(input)):
        cost += sum(range(1+abs(input[j]-i)))
    if cost < fuel:
        fuel = cost
        pos = i

print(f"fuel: {fuel}")
