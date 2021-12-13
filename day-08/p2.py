from typing import List
from utils.utils import get_lines_from_file


def sorted_str(s):
    return ''.join(sorted(s))


def remove_overlapping_chars(s1, s2):
    s1 = sorted_str(s1)
    s2 = sorted_str(s2)
    return sorted_str(''.join([ch for ch in s1 if ch not in s2] + [ch for ch in s2 if ch not in s1]))


def check(s1, s2):
    return all([ch in s2 for ch in s1])


if __name__ == "__main__":
    lines = get_lines_from_file('day-8/input')

    sum = 0
    for line in lines:

        left, right = line.split('|')
        words_on_left = [sorted_str(w) for w in left.rstrip().split()]
        words_on_right = [sorted_str(w) for w in right.lstrip().split()]

        one = ''
        four = ''
        seven = ''
        wires = dict()

        for word in words_on_left:
            if len(word) == 2:
                wires[word] = 1
                one = word
            elif len(word) == 3:
                wires[word] = 7
                seven = word
            elif len(word) == 4:
                wires[word] = 4
                four = word
            elif len(word) == 7:
                wires[word] = 8

        # remove 1,4,7,8
        words_on_left = [w for w in words_on_left if len(w) not in [2, 3, 4, 7]]

        for word in words_on_left:
            word = sorted_str(word)
            sz = len(word)

            #  now we have a word for one of 0,2,3,5,6,or 9
            if sz == 6:  # Could be any of (0,6,9)
                # Check for zero first.
                if check(seven, word) and check(one, word) and not check(four, word):
                    wires[word] = 0
                # now check for 9
                elif check(seven, word) and check(one, word) and check(four, word):
                    wires[word] = 9
                else:
                    wires[word] = 6
            else:  # sz == 5: (2, 3, 5)
                # Check for 3
                if check(seven, word):  # and check(one, word):
                    wires[word] = 3
                elif check(remove_overlapping_chars(four, seven), word):
                    wires[word] = 5
                else:
                    wires[word] = 2

        num = int(''.join([str(wires[w]) for w in words_on_right]))
        sum += num

    print("Ans is: ", sum)
