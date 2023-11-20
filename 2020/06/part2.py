from part1 import load_data, split_into_groups


def count_everyone_answer(group):
    everyone_answer = set()
    # get letter common to all answers
    for answer in group[0]:
        is_common = True
        for person in group:
            if answer not in person:
                is_common = False
                break
        if is_common:
            everyone_answer.add(answer)
    return len(everyone_answer)


if __name__ == '__main__':
    # load data
    lines = load_data()

    # split into groups
    groups = split_into_groups(lines)
    print("Number of groups: ", len(groups))

    # count unique answers
    total = 0
    for group in groups:
        total += count_everyone_answer(group)

    print("Total number of unique answers: ", total)
