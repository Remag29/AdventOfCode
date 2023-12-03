def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_symboles(lines):
    # get symbols
    symbols = []
    not_symbols = ['\n', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for line in lines:
        for char in line:
            if char not in symbols and char not in not_symbols:
                symbols.append(char)
    return symbols


if __name__ == '__main__':
    # load data
    lines = load_data()

    # variables
    symboles = ['*']
    print(symboles)
    actual_number = ''
    valid_numbers = []
    gears_position = []
    linked_gears_index = -1

    # loop through lines and chars
    for i in range(len(lines)):
        line = lines[i]
        numberIsValid = False
        for j in range(len(line)):
            char = line[j]

            if char.isdigit():
                actual_number += char

                # Improve speed if the number is already valid (not enter in the loop)
                if numberIsValid and actual_number != '':
                    continue

                # test if a symbol is next to number
                for test_line in range(i - 1, i + 2):
                    if test_line < 0 or test_line > len(lines) - 1:
                        continue
                    for test_char in range(j - 1, j + 2):
                        if test_char < 0 or test_char > len(lines[test_line]) - 1:
                            continue

                        # Test if the char is a gear '*'
                        if lines[test_line][test_char] in symboles:
                            # Test if the gear is already in the list
                            if (test_line, test_char) in gears_position:
                                # Link the number to the gear index
                                linked_gears_index = gears_position.index((test_line, test_char))
                            else:
                                # Save the gear position
                                gears_position.append((test_line, test_char))
                            numberIsValid = True
                            break

            # If not a number, we can clear the actual number and save it
            else:
                if actual_number != '':
                    if numberIsValid:
                        if linked_gears_index == -1:
                            valid_numbers.append([actual_number])
                        else:
                            valid_numbers[linked_gears_index].append(actual_number)
                    actual_number = ''
                    numberIsValid = False
                    linked_gears_index = -1

    print('Gear position:' + str(gears_position))
    print(valid_numbers)

    # Only heap groups with 2 numbers
    valid_numbers = [group for group in valid_numbers if len(group) == 2]
    print(valid_numbers)

    # Multiply the numbers of each group
    valid_numbers_multiplied = [int(group[0]) * int(group[1]) for group in valid_numbers]
    print(valid_numbers_multiplied)

    # Sum all the numbers
    result = sum(valid_numbers_multiplied)
    print(result)
