def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def testIfTwiceLetter(line):
    # check if there is a letter that appears twice
    for letter in line:
        if line.count(letter) == 2:
            return True
    return False


def testIfThriceLetter(line):
    # check if there is a letter that appears thrice
    for letter in line:
        if line.count(letter) == 3:
            return True
    return False


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Count Twice and Thrice letters
    twice = 0
    thrice = 0
    for line in lines:
        if testIfTwiceLetter(line):
            twice += 1
        if testIfThriceLetter(line):
            thrice += 1

    # Calculate checksum
    checksum = twice * thrice

    # Print result
    print("Checksum: " + str(checksum))
