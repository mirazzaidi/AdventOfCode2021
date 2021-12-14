from utils.utils import get_lines_from_file
from collections import Counter

if __name__ == "__main__":
    lines = get_lines_from_file('day-14/input')

    polymer = lines[0]
    rules = {}

    for line in lines[2:]:
        a, b = line.split(' -> ')
        rules[a] = b

    all_possible_pairs = Counter()

    for a, b in zip(polymer, polymer[1:]):
        all_possible_pairs[a + b] += 1

    for step in range(40):
        child_pairs = Counter()
        for parent_pair, count in all_possible_pairs.items():
            # both children pair will be as many times as there are parent pairs.
            child_pairs[parent_pair[0] + rules[parent_pair]] += count
            child_pairs[rules[parent_pair] + parent_pair[1]] += count
        all_possible_pairs = child_pairs

    char_counter = Counter()
    for pair, count in all_possible_pairs.items():
        char_counter[pair[0]] += count
        char_counter[pair[1]] += count

    # if we join all child pairs, only first and last characters in the original polymer will not be repeated.
    # So we increment them here, as we divide them later.
    char_counter[polymer[0]] += 1
    char_counter[polymer[-1]] += 1

    for k, v in char_counter.items():
        char_counter[k] = v // 2

    print("Ans is ", max(char_counter.values()) - min(char_counter.values()))
