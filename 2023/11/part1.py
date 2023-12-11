def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def expends_universe(lines):
    new_lines_y = []
    for line in lines:
        new_lines_y.append(line.strip('\n'))
        if '#' not in line:
            # Double the line
            new_lines_y.append(line.strip('\n'))

    # Create a numpy array from the new_lines_y
    from numpy import array
    new_lines_y = array(new_lines_y)
    new_lines_y = array([list(line) for line in new_lines_y])

    # Double the columns if no '#' in the column
    new_line_xy = []
    for column in range(new_lines_y.shape[1]):
        column = new_lines_y[:, column]
        new_line_xy.append(column)
        if '#' not in column:
            # duplicate the column
            new_line_xy.append(column)

    # Create a numpy array from the new_line_xy
    new_line_xy = array(new_line_xy).T
    return new_line_xy


def get_all_pairs(lines):
    # Get the number of '#' in the lines
    from numpy import where
    y, x = where(lines == '#')
    pairs_table = []
    for i in range(len(y)):
        for j in range(i + 1, len(y)):
            pairs_table.append(((y[i], x[i]), (y[j], x[j])))
    return pairs_table


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Expend the universe
    lines = expends_universe(lines)
    print(f'Number of lines after expending :', len(lines))
    print(f'Number of columns after expending :', len(lines[:, 0]))

    # Test pair distances
    pairs_table = get_all_pairs(lines)

    # Get the distances between all pairs
    distances = []
    for pair in pairs_table:
        distances.append(abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]))

    print(f'Number of pairs :', len(distances))
    print(f'Minimum distance :', min(distances))
    print(f'Maximum distance :', max(distances))
    print(f'Sum of distances :', sum(distances))
