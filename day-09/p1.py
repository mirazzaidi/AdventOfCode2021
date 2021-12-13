# https://adventofcode.com/2021/day/9
from utils.utils import get_lines_from_file


if __name__ == "__main__":
    lines = get_lines_from_file('day-9/input')

    rows = len(lines)
    cols = len(lines[0])
    mat = []
    for i, line in enumerate(lines):
        row_ = []
        for j, item in enumerate(line):
            row_.append(int(item))
        mat.append(row_)
    lows = []
    for i in range(rows):
        for j in range(cols):
            up = down = left = right = 10
            if i > 0:
                up = mat[i - 1][j]
            if i < rows - 1:
                down = mat[i + 1][j]
            if j > 0:
                left = mat[i][j - 1]
            if j < cols - 1:
                right = mat[i][j + 1]
            if mat[i][j] < up and mat[i][j] < down and mat[i][j] < left and mat[i][j] < right:
                lows.append(mat[i][j])
    lows = [low + 1 for low in lows]

    print(sum(lows))
