# https://adventofcode.com/2021/day/1


if __name__ == "__main__":
    lines = []
    with open('input') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    count = 0;
    prev = int(lines[0])
    for data in lines[1:]:
        if int(data) > prev:
            count += 1
        prev = int(data)
    print(count)