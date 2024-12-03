import re

def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

def calc_mul(mul) -> int:
    mul_match = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", mul)
    return int(mul_match.group(1)) * int(mul_match.group(2))


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    matchs = []

    for line in lines:
        matchs += re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)

    print(matchs)

    result = 0
    process_mul = True

    for match in matchs:
        if re.match(r"do\(\)", match):
            process_mul = True
        elif re.match(r"don't\(\)", match):
            process_mul = False
        elif process_mul:
            result += calc_mul(match)

    print(f'The result is {result}')

    # 98044236 To High