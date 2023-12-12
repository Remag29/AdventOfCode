def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def read_line(line):
    # read line
    line = line.strip()
    placement = line.split(' ')[0]
    numbers = line.split(' ')[1].split(',')
    numbers = [int(number) for number in numbers]

    return placement, numbers


def get_possible_positions(placement, possible_positions):
    replacement = ['.', '#']

    if '?' in placement:
        for i in range(2):
            new_placement = placement.replace('?', replacement[i], 1)
            possible_positions = get_possible_positions(new_placement, possible_positions)
        return possible_positions
    else:
        possible_positions.add(placement)
        return possible_positions


def get_matching_positions(possible_positions, numbers):
    solutions = set()
    for position in possible_positions:
        blocks = position.split('.')
        counts = [block.count('#') for block in blocks if block.count('#') > 0]
        if counts == numbers:
            solutions.add(position)

    return solutions


if __name__ == '__main__':
    # laod data
    lines = load_data()

    final_result = 0

    for line in lines:
        placement, numbers = read_line(line)
        possible_positions = get_possible_positions(placement, set())
        matching_positions = get_matching_positions(possible_positions, numbers)
        final_result += len(matching_positions)

    print(final_result)
