# https://adventofcode.com/2021/day/1
from utils.utils import get_lines_from_file


if __name__ == "__main__":
    lines = get_lines_from_file('day-1/input')
    lines = [int(x) for x in lines]

    count = 0
    prev = int(lines[0])
    for data in lines[1:]:
        if int(data) > prev:
            count += 1
        prev = int(data)
    print(count)