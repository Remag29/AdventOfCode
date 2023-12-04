def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_data(line):
    line = line.strip().split(':')
    # GET ID
    id = int(line[0].split(' ')[-1])

    # GET MY NUMBERS
    my_numbers = line[1].strip().split('|')[0].strip().split(' ')
    # remove empty string
    for number in my_numbers:
        if number == '':
            my_numbers.remove(number)
    # convert to int
    my_numbers = [int(number) for number in my_numbers]

    # GET WINNING NUMBERS
    winning_numbers = line[1].strip().split('|')[1].strip().split(' ')
    # remove empty string
    for number in winning_numbers:
        if number == '':
            winning_numbers.remove(number)
    # convert to int
    winning_numbers = [int(number) for number in winning_numbers]

    return id, my_numbers, winning_numbers


def check_win_count(my_numbers, winning_numbers):
    count = 0
    for number in my_numbers:
        if number in winning_numbers:
            count += 1
    return count


def calc_card_score(number_of_win):
    if number_of_win == 1:
        return 1
    elif number_of_win > 1:
        score = 1
        for i in range(1, number_of_win):
            score *= 2
        return score
    else:
        return 0


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Calculate cards score
    cards_score = []
    for card in lines:
        id, my_numbers, winning_numbers = get_data(card)
        number_of_win = check_win_count(my_numbers, winning_numbers)
        score = calc_card_score(number_of_win)
        cards_score.append(score)

    # Print cards score
    print(cards_score)

    # Calculate total score
    print(sum(cards_score))


