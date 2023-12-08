from part1 import load_data, map_data


# LCM to find the lowest common multiple of a list of numbers
def LCM(numbers):
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm * i // GCD(lcm, i)
    return lcm


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    # load data
    lines = load_data()

    # map data
    path, map = map_data(lines)
    print(path)
    print(map)

    # Find the path
    start_map = {k: v for k, v in map.items() if k.endswith('A')}
    print(start_map)

    steps = []

    for key in start_map.keys():
        actual_key = key
        path_index = 0
        step = 0

        while not actual_key.endswith('Z'):
            direction = path[path_index]

            if direction == 'L':
                actual_key = map[actual_key][0]
            elif direction == 'R':
                actual_key = map[actual_key][1]

            step += 1
            path_index += 1
            path_index %= len(path)

        steps.append(step)

    print(steps)
    print(LCM(steps))
