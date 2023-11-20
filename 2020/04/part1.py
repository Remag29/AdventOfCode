def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def sanitaze_data(lines):
    passports = []
    passport = {}

    for line in lines:
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
            line = line.replace('\n', '')
            line = line.split(' ')
            for field in line:
                field = field.split(':')
                passport[field[0]] = field[1]

    # append last passport
    passports.append(passport)
    
    return passports


def is_passport_valid(passport):
    if len(passport) == 8:
        return True
    elif len(passport) == 7 and 'cid' not in passport:
        return True
    else:
        return False


if __name__ == '__main__':
    # load data
    lines = load_data()

    # sanitaze data to get a list of passports
    passports = sanitaze_data(lines)
    print("Number of passports: ", len(passports))
    print("First passport: ")
    print(passports[0])
    print("Last passport: ")
    print(passports[-1])

    # check if passport is valid
    valid_passports = 0
    for passport in passports:
        if is_passport_valid(passport):
            valid_passports += 1

    print(valid_passports)
