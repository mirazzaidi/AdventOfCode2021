from utils.utils import get_lines_from_file

if __name__ == "__main__":
    lines = get_lines_from_file('day-8/input')

    # strip the part before |
    lines = [line.split('|')[1].lstrip() for line in lines]
    print("Total words: ", len(
        [word for line in lines for word in line.split() if len(word) in [2, 3, 4, 7]]))
