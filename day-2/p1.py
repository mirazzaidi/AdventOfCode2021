# https://adventofcode.com/2021/day/2

if __name__ == "__main__":
    lines = []
    with open('input') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

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
    
    print(hp*dp)


        