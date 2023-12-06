def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_data(lines):
    time = lines[0].split(':')[1].strip().split(' ')
    time = [int(x) for x in time if x != '']
    distance = lines[1].split(':')[1].strip().split(' ')
    distance = [int(x) for x in distance if x != '']
    return time, distance


def calc_distance(pressed_time, race_time):
    return (pressed_time) * (race_time - pressed_time)


if __name__ == '__main__':
    # load data
    lines = load_data()

    # get data
    times, distances = get_data(lines)
    print(times, distances)

    result = 1

    for time_index, time_race in enumerate(times):
        win_press_time = []
        for time_pressed in range(1, time_race + 1):
            # calculate traveled distance of the boat
            boat_distance = calc_distance(time_pressed, time_race)

            if boat_distance > distances[time_index]:
                win_press_time.append(time_pressed)
        result *= len(win_press_time)

    print(result)
