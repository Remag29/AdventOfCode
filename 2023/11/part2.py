from part1 import load_data, get_all_pairs


def lines_to_graph(lines):
    # Create an array from lines
    from numpy import array
    global_list = []
    for line in lines:
        line = line.strip('\n')
        char_list = []
        for char in line:
            char_list.append(char)
        global_list.append(char_list)

    # Change value if line of 1
    for i, line in enumerate(global_list):
        if '#' not in line:
            global_list[i] = ['1000000' for _ in range(len(line))]

    # Change value if column of 1
    for i in range(len(global_list[0])):
        column = [line[i] for line in global_list]
        if '#' not in column:
            for j in range(len(global_list)):
                global_list[j][i] = '1000000'

    # Create a numpy array from the global_list
    global_list = array(global_list)

    # Replace all '.' with 1
    global_list[global_list == '.'] = 1

    return global_list


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Expend the universe
    graph = lines_to_graph(lines)

    # Test pair distances
    pairs_table = get_all_pairs(graph)

    # Get the distances between all pairs
    distances = []
    for pair in pairs_table:
        start_point = pair[0]
        end_point = pair[1]
        distance = 0

        # Add the score of each point between the start and the end
        while start_point != end_point:

            # Add the score of the point
            contant = graph[start_point[0], start_point[1]]
            if contant == '#':
                distance += 1
            else:
                distance += int(contant)

            # Move the start point
            if start_point[0] < end_point[0]:
                start_point = (start_point[0] + 1, start_point[1])
            elif start_point[0] > end_point[0]:
                start_point = (start_point[0] - 1, start_point[1])
            elif start_point[1] < end_point[1]:
                start_point = (start_point[0], start_point[1] + 1)
            elif start_point[1] > end_point[1]:
                start_point = (start_point[0], start_point[1] - 1)

        distances.append(distance)

    print(f'Number of pairs :', len(distances))
    print(f'Minimum distance :', min(distances))
    print(f'Maximum distance :', max(distances))
    print(f'Sum of distances :', sum(distances))
