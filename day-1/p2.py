
if __name__ == "__main__":
    lines = []
    with open('input') as f:
        lines = f.readlines()
        lines = [int(line.rstrip()) for line in lines]

    count = 0;
    prev_window_sum = sum(lines[0:3])
    prev = int(lines[0])
    for i in range(3, len(lines)):
        next_element = lines[i]
        prev_element = lines[i-3]
        new_window_sum = prev_window_sum + next_element - prev_element
        if new_window_sum > prev_window_sum:
            count += 1
        prev_window_sum = new_window_sum


    print(count)

