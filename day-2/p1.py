# https://adventofcode.com/2021/day/2
from utils.utils import get_lines_from_file

if __name__ == "__main__":
    lines = get_lines_from_file('day-2/input')

    hp = 0
    dp = 0
    for line in lines:
        direction, value = line.split(' ')
        value = int(value)
        if direction == 'up':
            dp -= value
        elif direction == 'down':
            dp += value
        elif direction == 'forward':
            hp += value
    ans = hp*dp
    print(ans)
    assert ans == 1690020


        