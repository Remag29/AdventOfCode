import re

def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

def calc_mul(mul) -> int:
    return int(mul[0]) * int(mul[1])


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    matchs = []

    for line in lines:
        matchs += re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)

    result = 0
    for match in matchs:
        result += calc_mul(match)

    print(f'The result is {result}')