def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_tables(lines):
    # get tables
    tables = []
    table = []
    for line in lines:
        if line == '\n':
            tables.append(table)
            table = []
        else:
            table.append(line)
    tables.append(table)
    return tables


def get_new_position(seed_pos, table):
    # Get the concerned line of the table
    for line in table[1:]:
        # Clean the line
        line = line.replace('\n', '')
        base_pos = int(line.split(' ')[1])
        transposed_pos = int(line.split(' ')[0])
        step = int(line.split(' ')[2])

        # Test if the seed is on the interval base_pos, base_pos + step
        if base_pos <= seed_pos <= base_pos + step:
            # Calculate the transposed position
            new_pos = (transposed_pos + seed_pos - base_pos)
            return new_pos

    # If not in the interval, return the seed position
    return seed_pos


if __name__ == '__main__':
    # Load data
    lines = load_data()

    # Get tables
    tables = get_tables(lines)
    print(tables)

    # Get seeds
    seeds = tables[0][0].split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    print(seeds)

    # Get the final position
    final_position = []
    for i, init_seed_pos in enumerate(seeds):
        print('-------------------')
        print('Seed ' + str(i) + ' : ' + str(init_seed_pos))
        actual_pos = init_seed_pos

        # Get the final position for the seed after each table
        for table in tables[1:]:
            actual_pos = get_new_position(actual_pos, table)
            print('|--> ' + table[0].replace('\n', '') + ' : ' + str(actual_pos))
        # Append the final position of the seed
        final_position.append(actual_pos)
        print('| -----> Final position : ' + str(actual_pos))

    # Get the lowest seed position
    lowest_seed_pos = min(final_position)
    print('-------------------')
    print('Lowest seed position : ' + str(lowest_seed_pos))
