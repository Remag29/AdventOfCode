def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def split_into_groups(lines):
    groups = []
    group = []
    for line in lines:
        if line == '\n':
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
    groups.append(group)
    return groups


def count_unique_answers(group):
    unique_answers = set()
    for person in group:
        for answer in person:
            unique_answers.add(answer)
    return len(unique_answers)


if __name__ == '__main__':
    # load data
    lines = load_data()

    # split into groups
    groups = split_into_groups(lines)
    print("Number of groups: ", len(groups))

    # count unique answers
    total = 0
    for group in groups:
        total += count_unique_answers(group)

    print("Total number of unique answers: ", total)
