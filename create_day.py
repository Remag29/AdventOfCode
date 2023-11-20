import os

if __name__ == '__main__':

    # Request the years and the day to the user
    year = int(input('Enter the year: '))
    day = int(input('Enter the day: '))

    # Ensure the year is valid
    if len(str(year)) != 4:
        print('Invalid year')
        exit()

    # Ensure the day is valid
    if day < 1 or day > 25:
        print('Invalid day')
        exit()
    else:
        day = f'{day:02d}'

    print(f'Creating day {day} of {year} ...')

    folder_path = f'./{year}/{day}'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print('The folder already exists')
        exit()

    # Create the files
    with open(f'{folder_path}/input.txt', 'w') as f:
        f.close()

    with open(f'{folder_path}/part1.py', 'w') as f:
        f.close()

    with open(f'{folder_path}/part2.py', 'w') as f:
        f.close()

    print(f'Day {day} of {year} created successfully')
