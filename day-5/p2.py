from typing import List


def get_coords_from_str(line: str):
    p1, p2 = line.split(' -> ')
    x1, y1 = p1.split(',')
    x2, y2 = p2.split(',')

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    return x1, y1, x2, y2


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    w, h = 1000, 1000
    Matrix = [[0 for x in range(w)] for y in range(h)]

    # horizontal/vertical
    for line in lines:
        x1, y1, x2, y2 = get_coords_from_str(line)
        if x1 != x2 and y1 != y2:
            continue
        if x1 > x2 or y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                Matrix[i][j] += 1
    # Diagonals
    for line in lines:
        x1, y1, x2, y2 = get_coords_from_str(line)
        if x1 == x2 or y1 == y2 or abs(x1 - x2) != abs(y1 - y2):  # not a 45 degree diagonal
            continue
        x = x2 - x1
        y = y2 - y1

        range_of_movement = []

        if x > 0 and y < 0:
            x_range = range(x1, x2 + 1)
            y_range = range(y1, y2 - 1, -1)
        elif x > 0 and y > 0:
            x_range = range(x1, x2 + 1)
            y_range = range(y1, y2 + 1)
        elif x < 0 and y > 0:
            x_range = range(x1, x2 - 1, -1)
            y_range = range(y1, y2 + 1)
        else:  # x<0 and y<0:
            x_range = range(x1, x2 - 1, -1)
            y_range = range(y1, y2 - 1, -1)

        for i, j in zip(x_range, y_range):
            Matrix[i][j] += 1
    ans = 0
    for i in range(0, w):
        for j in range(0, h):
            if Matrix[i][j] > 1:
                ans += 1
    print(ans)
