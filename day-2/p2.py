
def fun(lines):
    hp = 0
    dp = 0
    aim = 0
    for line in lines:
        direction, value = line.split(' ')
        value = int(value)
        if direction == 'down':
            # dp += value
            aim += value
        elif direction == 'up':
            # dp -= value
            aim -= value
        elif direction == 'forward':
            hp += value
            # It increases your depth by your aim multiplied by X.
            dp += aim * value
    
    return hp*dp






if __name__ == "__main__":
    lines = []
    with open('input') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    # lines = [
    #     'forward 5',
    #     'down 5', 
    #     'forward 8',
    #     'up 3',
    #     'down 8',
    #     'adds 8',
    #     'forward 2'
    #     ]
    ans = fun(lines)
    print(ans)



        