import copy


def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_antinode(position_a: tuple[int, int], position_b: tuple[int, int], len_table: int) -> list[tuple[int, int]]:
    antinode_a = (position_a[0] + (position_a[0] - position_b[0]), position_a[1] + (position_a[1] - position_b[1]))
    antinode_b = (position_b[0] + (position_b[0] - position_a[0]), position_b[1] + (position_b[1] - position_a[1]))

    correct_antinode = []
    if len_table >= antinode_a[0] >= 0 and len_table >= antinode_a[1] >= 0:
        correct_antinode.append(antinode_a)
    if len_table >= antinode_b[0] >= 0 and len_table >= antinode_b[1] >= 0:
        correct_antinode.append(antinode_b)

    return correct_antinode


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    position_dictionary = {}

    # Get and order all positions by character on a dictionary
    for x_index, line in enumerate(lines):
        for y_index, character in enumerate(line):
            if character not in ['.', '\n']:
                if character in position_dictionary:
                    position_dictionary[character].append((x_index, y_index))
                else:
                    position_dictionary[character] = [(x_index, y_index)]

    print(position_dictionary)

    antinode_positions = set()
    for character_type in position_dictionary.keys():  # For each type of antenna
        for current_position in position_dictionary[character_type]:  # Get a position
            positions = copy.deepcopy(position_dictionary[character_type])  # Get a copy of the positions list
            positions.pop(positions.index(current_position))  # Remove the current position

            for remaining_position in positions:
                antinode_positions.update(get_antinode(current_position, remaining_position, len(lines) - 1))

    print(f'The result is {len(antinode_positions)}')

    # 107 : To low
