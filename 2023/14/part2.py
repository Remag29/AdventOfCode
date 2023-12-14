import itertools

from part1 import load_data


def transpose(matrix: tuple) -> tuple:
    return tuple(["".join(row) for row in zip(*matrix)])


def roll(lines):
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
    return new_lines


def roll_V2(lines):  # ~ 2x faster than roll, but not enough =/
    new_lines = []
    for line in lines:
        new_line = []
        splitted_line = line.split('#')
        for splitted_part in splitted_line:
            # Sort splitted_part : O first, . second
            new_line.append(''.join(sorted(splitted_part, key=lambda x: x == 'O', reverse=True)))
        new_lines.append('#'.join(new_line))
    return new_lines


def roll_V3(lines, reverse_bool):
    tilted = []
    for row in lines:
        row_split = [
            sorted(fragment, reverse=reverse_bool) for fragment in row.split('#')
        ]
        row_combined = "#".join("".join(fragment) for fragment in row_split)
        tilted.append(row_combined)
    return tuple(tilted)


def perform_cycle(lines):
    for order in [True, True, False, False]:
        lines = transpose(lines)
        lines = roll_V3(lines, order)
    return lines


if __name__ == '__main__':
    # Print time of start
    import datetime

    print(datetime.datetime.now())

    # Load data
    lines = load_data()

    # Reformat lines
    lines = [list(row.replace('\n', '')) for row in lines]

    # Roll
    actual_cycle = 0
    cycle = 1000000000

    final_board = None
    seen, order = {}, {}
    for counter in itertools.count(1):
        lines = perform_cycle(lines)
        if lines in seen:
            second_appearance, first_appearance = counter, seen[lines]
            index = (cycle - first_appearance) % (second_appearance - first_appearance) + first_appearance
            final_board = transpose(order[index])
            break
        seen[lines] = counter
        order[counter] = lines

    # Count the weight
    weight = sum(sum(len(row) - i for i, char in enumerate(row) if char == 'O') for row in final_board)

    print(weight)
