from typing import List, Set


def update_tables(tables: List[List[List[int]]], num):
    for table in tables:
        for row in range(len(table)):
            for col in range(len(table[0])):
                # print(table[row][col])
                if table[row][col] == num:
                    table[row][col] = -1 * num


def check_table(table: List[List[int]]):
    # check rows
    for row in table:
        if all(col <= 0 for col in row):
            return True

    for col in list(zip(*table)):
        if all(c <= 0 for c in col):
            return True
    return False


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
    winners: Set[int] = set()
    for num in markings:
        # print(num)

        update_tables(tables, num)
        for table_index, table in enumerate(tables):
            if check_table(table):
                winners.add(table_index)
                if len(winners) == len(tables):
                    winner_index = table_index
                    break
        if len(winners) == len(tables):
            break

    sum = 0
    if winner_index >= 0:
        wt = tables[winner_index]
        for i in range(5):
            for j in range(5):
                if wt[i][j] >= 0:
                    sum += wt[i][j]

    print(num * sum)
