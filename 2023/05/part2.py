from part1 import *

if __name__ == '__main__':
    # Load data
    lines = load_data()

    # Get tables
    tables = get_tables(lines)
    print(tables)

    # Get seeds
    seeds = tables[0][0].split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    print('Get a total of ' + str(len(seeds)) + ' seeds')

    # Get the final position
    min_seed_pos = -1
    # Get seeds two by two
    for i in range(0, len(seeds), 2):
        init_seed_pos = seeds[i]
        step = seeds[i + 1]
        print('Seed part ' + str(i / 2) + '/' + str(len(seeds) / 2))

        for seed in range(init_seed_pos, init_seed_pos + step + 1):
            actual_pos = seed

            # Get the final position for the seed after each table
            for table in tables[1:]:
                actual_pos = get_new_position(actual_pos, table)

            # Test if the final position is the lowest
            if min_seed_pos == -1 or actual_pos < min_seed_pos:
                min_seed_pos = actual_pos

    # Get the lowest seed position
    print('-------------------')
    print('Lowest seed position : ' + str(min_seed_pos))
