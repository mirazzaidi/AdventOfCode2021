from utils.utils import get_lines_from_file

if __name__ == "__main__":
    lines = get_lines_from_file('day-1/input')
    lines = [int(x) for x in lines]

    count = 0
    prev_window_sum = sum(lines[0:3])
    prev = int(lines[0])
    for i in range(3, len(lines)):
        next_element = lines[i]
        prev_element = lines[i - 3]
        new_window_sum = prev_window_sum + next_element - prev_element
        if new_window_sum > prev_window_sum:
            count += 1
        prev_window_sum = new_window_sum

    print(count)
