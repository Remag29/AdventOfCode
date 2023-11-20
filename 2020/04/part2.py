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


def test_byr(byr):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if len(byr) != 4:
        return False
    elif int(byr) < 1920 or int(byr) > 2002:
        return False
    else:
        return True


def test_iyr(iyr):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if len(iyr) != 4:
        return False
    elif int(iyr) < 2010 or int(iyr) > 2020:
        return False
    else:
        return True


def test_eyr(eyr):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if len(eyr) != 4:
        return False
    elif int(eyr) < 2020 or int(eyr) > 2030:
        return False
    else:
        return True


def test_hgt(hgt):
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    if hgt[-2:] == 'cm':
        if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
            return False
        else:
            return True
    elif hgt[-2:] == 'in':
        if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
            return False
        else:
            return True
    else:
        return False


def test_hcl(hcl):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if hcl[0] != '#':
        return False
    elif len(hcl) != 7:
        return False
    else:
        for char in hcl[1:]:
            if char not in '0123456789abcdef':
                return False
        return True


def test_ecl(ecl):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    else:
        return True


def test_pid(pid):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(pid) != 9:
        return False
    else:
        for char in pid:
            if char not in '0123456789':
                return False
        return True


def test_all_fields(passport):
    if (test_byr(passport['byr']) and test_iyr(passport['iyr']) and test_eyr(passport['eyr']) and
            test_hgt(passport['hgt']) and test_hcl(passport['hcl']) and test_ecl(passport['ecl']) and
            test_pid(passport['pid'])):
        return True
    else:
        return False


def is_passport_valid(passport):
    if len(passport) == 8:
        # check if fields are valid
        if test_all_fields(passport):
            return True
        else:
            return False

    elif len(passport) == 7 and 'cid' not in passport:
        # check if fields are valid
        if test_all_fields(passport):
            return True
        else:
            return False
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
