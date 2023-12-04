from part1 import load_data, get_data, check_win_count

if __name__ == '__main__':
    # load data
    lines = load_data()

    # Get the card
    cards = []
    for line in lines:
        cards.append(get_data(line))

    # Scratch the card
    for card in cards:
        card_id, my_numbers, winning_numbers = card
        number_of_win = check_win_count(my_numbers, winning_numbers)
        for i in range(number_of_win):
            copy = cards[card_id + i]
            cards.append(copy)

    # Calculate cards score
    print(len(cards))
