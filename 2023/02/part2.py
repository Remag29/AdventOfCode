from part1 import load_data, get_subgames


def get_game_min(subgames):
    max_red = 0
    max_green = 0
    max_blue = 0

    for subgame in subgames:
        if subgame['red'] > max_red:
            max_red = subgame['red']
        if subgame['green'] > max_green:
            max_green = subgame['green']
        if subgame['blue'] > max_blue:
            max_blue = subgame['blue']

    return {'red': max_red, 'green': max_green, 'blue': max_blue}


if __name__ == '__main__':
    # import data
    lines = load_data()

    # variables
    total_sum = 0

    for line in lines:
        # get subgames
        game = get_subgames(line)

        # get min of each color needed
        game_min = get_game_min(game['subgames'])

        # calculate the value of the game
        game_value = game_min['red'] * game_min['green'] * game_min['blue']

        # add to total sum
        total_sum += game_value

    print(total_sum)
