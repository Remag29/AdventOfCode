def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()
    # print(lines[0])

    # Make left list and right list
    right_list = []
    left_list = []

    for line in lines:
        left_list.append(int(line.split("   ")[0].strip()))
        right_list.append(int(line.split("   ")[1].strip()))

    # Do the math
    similarity_score = 0

    for number in left_list:
        similarity_score += number * right_list.count(number)

    print("The result is : ", similarity_score)
