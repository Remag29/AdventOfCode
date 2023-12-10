def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_pipes_points(lines):
    from part1 import get_start_position

    pipes_points = set()
    start_position = get_start_position(lines)
    actual_position = start_position
    previous_position = (-1, -1)

    formats = {
        'u': ['|', 'J', 'L', 'S'],
        'r': ['-', 'F', 'L', 'S'],
        'd': ['|', 'F', '7', 'S'],
        'l': ['-', 'J', '7', 'S']
    }

    while True:

        # UP
        if lines[actual_position[0] - 1][actual_position[1]] in formats['d'] and lines[actual_position[0]][
            actual_position[1]] in formats['u'] and previous_position != (actual_position[0] - 1, actual_position[1]):
            pipes_points.add((actual_position[0] - 1, actual_position[1]))
            previous_position = actual_position
            actual_position = (actual_position[0] - 1, actual_position[1])
        # RIGHT
        elif lines[actual_position[0]][actual_position[1] + 1] in formats['l'] and lines[actual_position[0]][
            actual_position[1]] in formats['r'] and previous_position != (actual_position[0], actual_position[1] + 1):
            pipes_points.add((actual_position[0], actual_position[1] + 1))
            previous_position = actual_position
            actual_position = (actual_position[0], actual_position[1] + 1)
        # DOWN
        elif lines[actual_position[0] + 1][actual_position[1]] in formats['u'] and lines[actual_position[0]][
            actual_position[1]] in formats['d'] and previous_position != (actual_position[0] + 1, actual_position[1]):
            pipes_points.add((actual_position[0] + 1, actual_position[1]))
            previous_position = actual_position
            actual_position = (actual_position[0] + 1, actual_position[1])
        # LEFT
        elif lines[actual_position[0]][actual_position[1] - 1] in formats['r'] and lines[actual_position[0]][
            actual_position[1]] in formats['l'] and previous_position != (actual_position[0], actual_position[1] - 1):
            pipes_points.add((actual_position[0], actual_position[1] - 1))
            previous_position = actual_position
            actual_position = (actual_position[0], actual_position[1] - 1)

        if actual_position == start_position and len(pipes_points) > 0:
            return pipes_points


def update_class(point_class, char, previous_char):
    if previous_char is None and char == '|':
        return not point_class

    # WARNING : This is a hack because I know my 'S' point is similar to a '|' point
    elif char == 'S':
        return not point_class

    elif char == '|':
        return not point_class

    elif char == '7' and previous_char == 'L':
        return not point_class

    elif char == 'J' and previous_char == 'F':
        return not point_class

    return point_class


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Get all pipes points
    pipes_points = get_pipes_points(lines)
    print(f'Pipes length: {len(pipes_points)}')

    inside_points = 0
    for line_index, line in enumerate(lines):
        line = line.replace('\n', '')

        # To start, point class is 0 (outside)
        point_class = False
        previous_char = None

        for column_index, char in enumerate(line):
            # Test if part of the pipe
            if (line_index, column_index) in pipes_points:
                # Test if there is a change in class
                point_class = update_class(point_class, char, previous_char)
                if char != '-':
                    previous_char = char

            else:
                inside_points += 1 if point_class else 0

    print(f'Inside points: {inside_points}')
