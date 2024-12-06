import os
import sys
from datetime import datetime

if __name__ == '__main__':

    # Try the current day
    date = datetime.now().strftime("%Y/%d")
    user_choice = input(f'Create files for the {date} ? (y/n)\n')

    if user_choice not in ['y', 'Y']:
        # Request the years and the day to the user
        year = int(input('Enter the year: '))
        day = int(input('Enter the day: '))
    else:
        year = int(date.split('/')[0])
        day = int(date.split('/')[1])

    # Ensure the year is valid
    if len(str(year)) != 4:
        print('Invalid year')
        sys.exit()

    # Ensure the day is valid
    if day < 1 or day > 25:
        print('Invalid day')
        sys.exit()
    else:
        day = f'{day:02d}'

    print(f'Creating day {day} of {year} ...')

    folder_path = f'./{year}/{day}'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print('The folder already exists')
        sys.exit()

    # Content for part1.py and part2.py
    template_content = """def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()
    """

    with open(f'{folder_path}/input.txt', 'w') as f:
        pass

    with open(f'{folder_path}/part1.py', 'w') as f:
        f.write(template_content)

    with open(f'{folder_path}/part2.py', 'w') as f:
        f.write(template_content)

    print(f'Day {day} of {year} created successfully')
