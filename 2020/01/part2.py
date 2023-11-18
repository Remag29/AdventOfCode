def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

if __name__ == '__main__':
    # load data
    lines = load_data()

    # convert to int
    lines = [int(line.strip()) for line in lines]

    # Test if the sum of three numbers is 2020
    for i in range(len(lines)):
        num = lines[i]
        for j in range(i + 1, len(lines)):
            num2 = lines[j]
            for k in range(j + 1, len(lines)):
                num3 = lines[k]
                if num + num2 + num3 == 2020:
                    print("Found the three numbers: ", num, num2, num3)
                    print("The product is: ", num * num2 * num3)