# import data
def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def getDigits(line):
    # get digits from line
    digits = []

    # Take the first
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
            break

    # Take the last
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            digits.append(line[i])
            break

    # create int from digits
    digits = int(''.join(digits))
    return digits


if __name__ == '__main__':
    # load data
    lines = load_data()

    # get digits
    digits = []
    for line in lines:
        digits.append(getDigits(line))

    # get sum
    print(sum(digits))
