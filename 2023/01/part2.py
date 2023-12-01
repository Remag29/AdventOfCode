from part1 import load_data


def getDigits(line):
    # Valid digits
    valid_text_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    valid_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # get digits from line
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(int(line[i]))
        else:
            for valid_text_digit in valid_text_digits:
                if line[i:i + len(valid_text_digit)] == valid_text_digit:
                    digits.append(valid_digits[valid_text_digits.index(valid_text_digit)])
                    break

    digits = [digits[0], digits[-1]]
    digits = int(''.join(map(str, digits)))
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
