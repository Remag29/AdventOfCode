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


def move_element(update: list[int], origin_index: int, new_index: int) -> list[int]:
    element = update.pop(origin_index)
    update.insert(new_index, element)
    return update


def order_bad_update(bad_update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    all_rules_ok = False
    while not all_rules_ok:  # While at least one rule is KO
        all_rules_ok = True
        for rule in rules:
            if (rule[0] in bad_update) and (rule[1] in bad_update) and (
                    bad_update.index(rule[0]) > bad_update.index(rule[1])):  # The Rule is not respected
                move_element(bad_update, bad_update.index(rule[1]), len(bad_update) - 1)  # Move Y element to the end
                all_rules_ok = False  # Notice it still KO
                break

    return bad_update


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    # Get rules
    rule_list = extract_order_rules(lines)
    print(rule_list)

    # Get updates
    update_list = extract_update_list(lines)
    print(update_list)

    # Test all the updates
    bad_updates = []
    for update in update_list:
        if not inspect_update(update, rule_list):
            bad_updates.append(update)

    # Order all bad updates
    good_updates = []
    for bad_update in bad_updates:
        good_updates.append(order_bad_update(bad_update, rule_list))
    print(good_updates)
    # Add up the middle page number from those correctly ordered updates
    result = 0
    for good_update in good_updates:
        result += good_update[len(good_update) // 2]

    print(f'The result is {result}')