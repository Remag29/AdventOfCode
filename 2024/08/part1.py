def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


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

    antinode_positions = ()
    for character_type in position_dictionary.keys():

    