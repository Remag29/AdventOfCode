def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def map_data(lines):
    # map data to dictionary
    map = {}
    for i, line in enumerate(lines):
        if i == 0:
            path = line.replace('\n', '')
        elif i == 1:
            continue
        else:
            name = line.split(' ')[0]
            left = line.split('(')[1].split(',')[0]
            right = line.split(' ')[-1].split(')')[0]
            map[name] = (left, right)
    return path, map


if __name__ == '__main__':
    # load data
    lines = load_data()

    # map data
    path, map = map_data(lines)
    print(path)
    print(map)

    # Find the path
    actual_key = 'AAA'
    path_index = 0
    steps = 0

    while actual_key != 'ZZZ':
        direction = path[path_index]

        if direction == 'L':
            actual_key = map[actual_key][0]
        elif direction == 'R':
            actual_key = map[actual_key][1]

        steps += 1
        path_index += 1
        path_index %= len(path)

    print(actual_key)
    print(path_index)
    print(steps)

