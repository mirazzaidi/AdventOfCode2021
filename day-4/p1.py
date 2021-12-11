# https://adventofcode.com/2021/day/4

from typing import List


def update_tables(tables: List[List[List[int]]], num):
    for table in tables:
        for row in range(len(table)):
            for col in range(len(table[0])):
                # print(table[row][col])
                if table[row][col] == num:
                    table[row][col] = -num


def check_tables(tables: List[List[List[int]]]):
    for index, table in enumerate(tables):
        # check rows
        for row in table:
            if all(col < 0 for col in row):
                return index

        for col in list(zip(*table)):
            if all(c < 0 for c in col):
                return index
    return -1


if __name__ == "__main__":
    markings: List[int] = []

    with open('input') as f:
        lines = f.readlines()
        lines = ''.join(lines).split('\n')
        lines = [line for line in lines if line]
    markings = [int(marking) for marking in lines[0].split(',')]

    tables: List[List[List[int]]] = []
    table = []
    for line in lines[1:]:
        row = [int(item) for item in line.split()]
        table.append(row)
        if len(table) == 5:
            tables.append(table)
            table = []
    winner_index = -1
    for num in markings:
        # print(num)
        update_tables(tables, num)
        winner_index = check_tables(tables)
        if winner_index >= 0:
            break

    sum = 0
    wt = tables[winner_index]
    for i in range(5):
        for j in range(5):
            if (v := wt[i][j]) >= 0:
                sum += v

    print(num * sum)
