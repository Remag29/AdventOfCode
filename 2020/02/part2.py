def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def decode_line(line):
    position1 = int(line.split('-')[0])
    position2 = int(line.split('-')[1].split(' ')[0])
    letter = line.split(' ')[1].replace(':', '')
    password = line.split(' ')[2]
    return position1, position2, letter, password


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Count are many passwords are valid
    valid_count = 0

    for line in lines:
        position1, position2, letter, password = decode_line(line)
        if (password[position1-1] == letter) ^ (password[position2-1] == letter):
            valid_count += 1
    print("Number of valid passwords: ", valid_count)

