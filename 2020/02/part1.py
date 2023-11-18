def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

def decode_line(line):
    min_occurence = int(line.split('-')[0])
    max_occurence = int(line.split('-')[1].split(' ')[0])
    letter = line.split(' ')[1].replace(':', '')
    password = line.split(' ')[2]
    return min_occurence, max_occurence, letter, password


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Count are many passwords are valid
    valid_count = 0
    for line in lines:
        min_occurence, max_occurence, letter, password = decode_line(line)
        if min_occurence <= password.count(letter) <= max_occurence:
            valid_count += 1
    print("Number of valid passwords: ", valid_count)