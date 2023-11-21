def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Addition all numbers
    total = 0
    for number in lines:
        total += int(number)

    # Print result
    print(total)