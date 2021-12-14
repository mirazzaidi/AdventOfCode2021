from typing import List

from collections import defaultdict, Counter


def get_lines_from_file(filename: str) -> List[str]:
    lines = []
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


if __name__ == "__main__":

    lines = get_lines_from_file('day-14/input')

    polymer = lines[0]
    rules = {}

    for line in lines[2:]:
        a, b = line.split(' -> ')
        rules[a] = b

    for step in range(10):
        s = ''
        for a, b in zip(polymer[0:], polymer[1:]):
            w = a + b
            if d := rules.get(w):
                s += a + d
        s += b
        polymer = s

    char_counter = Counter(polymer)

    print("Ans is ", max(char_counter.values()) - min(char_counter.values()))
