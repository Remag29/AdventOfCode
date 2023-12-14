def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def roll_up(lines):
    # Transpose lines
    lines = list(map(list, zip(*lines)))

    new_lines = []
    for line in lines:
        new_line = []
        free_space = 0
        for char in line:
            if char == 'O':
                new_line.append(char)
            elif char == '#':
                for _ in range(free_space):
                    new_line.append('.')
                new_line.append(char)
                free_space = 0
            else:
                free_space += 1

        if free_space > 0:
            for _ in range(free_space):
                new_line.append('.')

        new_lines.append(new_line)

    # Un-transpose lines
    new_lines = list(map(list, zip(*new_lines)))

    return new_lines


if __name__ == '__main__':
    # Load data
    lines = load_data()

    # Roll up
    rolled_lines = roll_up(lines)

    # Count the weight
    weight = 0
    for line_index, line in enumerate(rolled_lines):
        # Count 'O' in line
        number_of_O = line.count('O')
        line_weight_index = len(rolled_lines) - line_index
        weight += number_of_O * line_weight_index

    print(weight)
