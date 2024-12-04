def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def find_xmas(table: list[list]) -> int:
    count_xmas = 0
    for x in range(1, len(table) - 1):  # avoid up and down borders
        for y in range(1, len(table[0]) - 1):  # avoid right and left borders
            debug_middle = table[x][y]
            debug_UL = table[x - 1][y - 1]
            debug_DR = table[x + 1][y + 1]
            debug_UR = table[x - 1][y + 1]
            debug_DL = table[x + 1][y - 1]
            if (table[x][y] == 'A' and ((table[x - 1][y - 1] == 'M' and table[x + 1][y + 1] == 'S') or (
                    table[x - 1][y - 1] == 'S' and table[x + 1][
                y + 1] == 'M'))):  # The Middle is A and diagonal UL-DR is MAS or SAM
                if (table[x + 1][y - 1] == 'M' and table[x - 1][y + 1] == 'S') or (
                        table[x + 1][y - 1] == 'S' and table[x - 1][y + 1] == 'M'):  # diagonal UR-DL is MAS or SAM
                    count_xmas += 1
    return count_xmas


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    # Make a big table
    base_table = []
    for line in lines:
        base_table.append(list(line.replace('\n', '')))

    # Find XMAS on every table
    xmas_count = find_xmas(base_table)

    print(f'The result is {xmas_count}')
