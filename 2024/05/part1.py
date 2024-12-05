from typing import List, Type

from numpy.f2py.auxfuncs import throw_error


def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def extract_order_rules(lines: list[str]) -> list[tuple[int, int]]:
    order_rule_list = []
    for line in lines:
        if line == '\n':
            return order_rule_list
        else:
            order_rule_list.append((int(line.split('|')[0]), int(line.split('|')[1])))

    raise ValueError("The blank line that separate rules and update not found")


def extract_update_list(lines: list[str]) -> list[list[int]]:
    update_list = []
    for line in lines:
        if ',' in line:
            update_list.append(line.split(','))

    # Convertion des chiffres en int
    update_list = [[int(valeur.replace('\n', '')) for valeur in sous_liste] for sous_liste in update_list]

    return update_list


def inspect_update(update: list[int], rules: list[tuple[int, int]]) -> bool:
    for rule in rules:
        if (rule[0] in update) and (rule[1] in update) and (update.index(rule[0]) > update.index(rule[1])):
            return False  # One rule is not respected

    return True  # All the rules are respected


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    rule_list = extract_order_rules(lines)
    print(rule_list)

    update_list = extract_update_list(lines)
    print(update_list)

    # Test all the updates
    good_updates = []
    for update in update_list:
        if inspect_update(update, rule_list):
            good_updates.append(update)

    # Add up the middle page number from those correctly ordered updates
    result = 0
    for good_update in good_updates:
        result += good_update[len(good_update) // 2]

    print(f'The result is {result}')
