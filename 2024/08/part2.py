import copy


def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def node_on_the_map(position: tuple[int, int], len_table: int):
    if len_table >= position[0] >= 0 and len_table >= position[1] >= 0:
        return True
    else:
        return False


def get_antinode(position_a: tuple[int, int], position_b: tuple[int, int], len_table: int) -> list[tuple[int, int]]:
    antinode_a = (position_a[0] + (position_a[0] - position_b[0]), position_a[1] + (position_a[1] - position_b[1]))
    antinode_b = (position_b[0] + (position_b[0] - position_a[0]), position_b[1] + (position_b[1] - position_a[1]))

    correct_antinode = []
    current_node = antinode_a
    while node_on_the_map(current_node, len_table):
        correct_antinode.append(current_node)
        current_node = (
            current_node[0] + (position_a[0] - position_b[0]), current_node[1] + (position_a[1] - position_b[1]))

    current_node = antinode_b
    while node_on_the_map(current_node, len_table):
        correct_antinode.append(current_node)
        current_node = (
            current_node[0] + (position_b[0] - position_a[0]), current_node[1] + (position_b[1] - position_a[1]))

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
            antinode_positions.update([current_position])
            positions = copy.deepcopy(position_dictionary[character_type])  # Get a copy of the position list
            positions.pop(positions.index(current_position))  # Remove the current position

            for remaining_position in positions:
                antinode_positions.update(get_antinode(current_position, remaining_position, len(lines) - 1))

    print(f'The result is {len(antinode_positions)}')
