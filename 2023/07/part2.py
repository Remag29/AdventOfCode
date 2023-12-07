from part1 import load_data, calc_final_score, order_type


def convert_to_number(hand):
    translated_hand = []
    translation = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}

    for card in hand['cards']:
        if card[0] in translation.keys():
            translated_hand.append(translation[card[0]])
        else:
            translated_hand.append(int(card[0]))

    hand['cards'] = translated_hand

    return hand


def classify_hand(hand, type_dict):
    cards = hand['cards']

    # Determine the rank of the hand
    if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]:
        # Test if all cards are the same
        type_dict['5ofakind'].append(hand)
        return type_dict

    # Test if 4 cards are the same
    for card in cards:
        if cards.count(card) == 4:
            if card == 1 or 1 in cards:
                type_dict['5ofakind'].append(hand)
                return type_dict

            type_dict['4ofakind'].append(hand)
            return type_dict

    # Test if 3 cards are the same and the 2 others are the same
    for card in cards:
        if cards.count(card) == 3:
            # Test if there is a pair
            for card2 in cards:
                if cards.count(card2) == 2:
                    if card == 1 or card2 == 1:
                        type_dict['5ofakind'].append(hand)
                        return type_dict
                    else:
                        type_dict['fullhouse'].append(hand)
                        return type_dict
            # If there is no pair
            if card == 1 or 1 in cards:
                type_dict['4ofakind'].append(hand)
                return type_dict
            else:
                type_dict['3ofakind'].append(hand)
                return type_dict

    # Test if there are 2 pairs
    pair = 0
    used_cards = []
    for card in cards:
        if cards.count(card) == 2 and card not in used_cards:
            pair += 1
            used_cards.append(card)

    # Test if there is a pair
    if pair == 1:
        if 1 in cards:
            type_dict['3ofakind'].append(hand)
            return type_dict
        else:
            type_dict['1pair'].append(hand)
            return type_dict

    # Test if there are 2 pairs
    if pair == 2:
        if 1 in cards:
            # if there is a pair of J
            if cards.count(1) == 2:
                type_dict['4ofakind'].append(hand)
                return type_dict
            else:
                type_dict['fullhouse'].append(hand)
                return type_dict
        else:
            type_dict['2pairs'].append(hand)
            return type_dict

    # If there is no pair
    if 1 in cards:
        type_dict['1pair'].append(hand)
        return type_dict
    else:
        type_dict['highcard'].append(hand)
        return type_dict


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Get the final score
    final_score = 0
    type_dict = {'highcard': [], '1pair': [], '2pairs': [], '3ofakind': [], 'fullhouse': [], '4ofakind': [],
                 '5ofakind': []}

    for line in lines:
        # Get the hand and the score if win
        hand = {'cards': line.replace('\n', '').split(' ')[0],
                'score_if_win': line.replace('\n', '').split(' ')[1],
                'order_score': 0
                }

        # Convert the hand to a list of numbers
        hand = convert_to_number(hand)

        # Classify the hand by type
        type_dict = classify_hand(hand, type_dict)

    # Order the hands by type
    type_dict = order_type(type_dict)

    # Get the final score
    final_score = calc_final_score(type_dict)
    print(f'Final score: {final_score}')
