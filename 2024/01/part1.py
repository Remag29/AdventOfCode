def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def do_the_thing(left, right):
    total_distance = 0
    for index in range(len(left)):
        total_distance += abs(left[index] - right[index])

    return total_distance


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

    # Order lists
    left_list.sort()
    right_list.sort()

    # Do the math
    result = do_the_thing(left_list, right_list)

    print("The result is : ", result)
