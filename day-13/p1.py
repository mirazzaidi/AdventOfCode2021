from utils.utils import get_lines_from_file


if __name__ == "__main__":
    lines = get_lines_from_file('day-13/input')
    cols = 1 + max([int(line.split(',')[0]) for line in lines if ',' in line])
    rows = 1 + max([int(line.split(',')[1]) for line in lines if ',' in line])

    grid = [['.' for i in range(cols)] for j in range(rows)]

    i = 0

    # Read coordinates
    for i, line in enumerate(lines):
        if line == '':
            break
        x, y = line.split(',')
        x = int(x)
        y = int(y)

        grid[y][x] = '#'

    # Read and process folding instructions
    for line in lines[i + 1 :]:

        direction, value = line.split('=')

        direction = direction.split()[2]
        value = int(value)

        if direction == 'x':  # Right to left

            row = 0
            for i in range(rows):
                left = value - 1
                right = value + 1
                while left >= 0 and right < cols:
                    grid[i][left] = '.' if grid[i][left] == '.' and grid[i][right] == '.' else '#'
                    left -= 1
                    right += 1

                grid[row] = grid[row][:value]  # fold
                row += 1
            cols = len(grid[0])

        else:  # Down to up.
            for i in range(cols):
                up = value - 1
                down = value + 1
                while up >= 0 and down < rows:
                    grid[up][i] = '.' if grid[down][i] == '.' and grid[up][i] == '.' else '#'
                    up -= 1
                    down += 1

            grid = grid[:value]  # fold
            rows = len(grid)
        break

    count = 0
    for i in range(len(grid)):
        count += grid[i].count('#')
    print(count)
