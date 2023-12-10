def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_start_position(lines):
    for i, line in enumerate(lines):
        if 'S' in line:
            return i, line.index('S')


if __name__ == '__main__':
    # load data
    lines = load_data()

    # get start position
    start_position = get_start_position(lines)
    print(start_position)

    # get the farthest distance inside the pipe
    actual_positions = [start_position, start_position]

    # Get starting movement
    previous_positon = ''
    choosen_move = []
    for i in range(len(actual_positions)):
        if lines[start_position[0] - 1][start_position[1]] in ['|', 'F', '7'] and 'u' not in choosen_move:  # Up
            actual_positions[i] = (start_position[0] - 1, start_position[1])
            choosen_move.append('u')
        elif lines[start_position[0]][start_position[1] + 1] in ['-', 'J', '7'] and 'r' not in choosen_move:  # Right
            actual_positions[i] = (start_position[0], start_position[1] + 1)
            choosen_move.append('r')
        elif lines[start_position[0] + 1][start_position[1]] in ['|', 'J', 'L'] and 'd' not in choosen_move:  # Down
            actual_positions[i] = (start_position[0] + 1, start_position[1])
            choosen_move.append('d')
        elif lines[start_position[0]][start_position[1] - 1] in ['-', 'F', 'L'] and 'l' not in choosen_move:  # Left
            actual_positions[i] = (start_position[0], start_position[1] - 1)
            choosen_move.append('l')
    print(actual_positions)

    farthest_distance = 1
    previous_move = [x for x in choosen_move]

    formats = {
        'u': ['|', 'J', 'L'],
        'r': ['-', 'F', 'L'],
        'd': ['|', 'F', '7'],
        'l': ['-', 'J', '7']
    }

    while True:

        for i in range(len(actual_positions)):

            # UP
            if lines[actual_positions[i][0] - 1][actual_positions[i][1]] in formats['d'] and \
                    lines[actual_positions[i][0]][actual_positions[i][1]] in formats['u'] and previous_move[i] != 'd':
                actual_positions[i] = (actual_positions[i][0] - 1, actual_positions[i][1])
                previous_move[i] = 'u'
            # RIGHT
            elif lines[actual_positions[i][0]][actual_positions[i][1] + 1] in formats['l'] and \
                    lines[actual_positions[i][0]][actual_positions[i][1]] in formats['r'] and previous_move[i] != 'l':
                actual_positions[i] = (actual_positions[i][0], actual_positions[i][1] + 1)
                previous_move[i] = 'r'
            # DOWN
            elif lines[actual_positions[i][0] + 1][actual_positions[i][1]] in formats['u'] and \
                    lines[actual_positions[i][0]][actual_positions[i][1]] in formats['d'] and previous_move[i] != 'u':
                actual_positions[i] = (actual_positions[i][0] + 1, actual_positions[i][1])
                previous_move[i] = 'd'
            # LEFT
            elif lines[actual_positions[i][0]][actual_positions[i][1] - 1] in formats['r'] and \
                    lines[actual_positions[i][0]][actual_positions[i][1]] in formats['l'] and previous_move[i] != 'r':
                actual_positions[i] = (actual_positions[i][0], actual_positions[i][1] - 1)
                previous_move[i] = 'l'

        farthest_distance += 1

        if actual_positions[0] == actual_positions[1]:
            print('Found start position')
            print(actual_positions)
            print(choosen_move)
            print(farthest_distance)
            exit()
