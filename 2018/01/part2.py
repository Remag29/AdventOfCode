from part1 import load_data

if __name__ == '__main__':
    # Load data
    lines = load_data()

    total = 0
    frequencies = set()

    # Loop until we find a duplicate frequency
    while True:
        for number in lines:
            total += int(number)
            if total in frequencies:
                print("Found duplicate frequency: ", total)
                exit(0)
            else:
                frequencies.add(total)