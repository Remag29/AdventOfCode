def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def count_Cube(subgame):
    color = ['red', 'green', 'blue']
    count_red = 0
    count_green = 0
    count_blue = 0

    cubes = subgame.split(',')
    for cube in cubes:
        # cube text example " 2 red"
        cube = cube.strip()
        number = int(cube.split(' ')[0])
        color_cube = cube.split(' ')[1]

        if color_cube == color[0]:
            count_red += number
        elif color_cube == color[1]:
            count_green += number
        elif color_cube == color[2]:
            count_blue += number

    return {'red': count_red, 'green': count_green, 'blue': count_blue}


def get_subgames(line):
    id = int(line.split(':')[0].split(' ')[1].strip())
    line = line.split(':')[1]
    subgames = line.split(';')
    # get subgames with count_cube
    for i in range(len(subgames)):
        subgames[i] = count_Cube(subgames[i])

    return {'id': id, 'subgames': subgames}


def test_subgame(subgame):
    max_number = [12, 13, 14]

    if subgame['red'] > max_number[0]:
        return False
    elif subgame['green'] > max_number[1]:
        return False
    elif subgame['blue'] > max_number[2]:
        return False
    else:
        return True


if __name__ == '__main__':
    # import data
    lines = load_data()

    valid_games = []

    for line in lines:
        game = get_subgames(line)
        validation_table = []
        for subgame in game.get('subgames'):
            validation_table.append(test_subgame(subgame))

        if False in validation_table:
            print('Game ' + str(game.get('id')) + ' is not valid')
        else:
            valid_games.append(game.get('id'))
            print('Game ' + str(game.get('id')) + ' is valid')

    # sum valid games id
    print('Sum of valid games id: ' + str(sum(valid_games)))
