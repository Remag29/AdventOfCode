import re

import requests


def get_personal_leaderboard(year, cookies):
    url = f"https://adventofcode.com/{year}/leaderboard/self"
    r = requests.get(url, cookies=cookies)

    # Prettify the page with BeautifulSoup
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_dataframe(soup_page):
    import pandas as pd
    import io

    # Test if the page contains the text "You haven't collected any stars... yet."
    if soup_page.find(string=re.compile("You haven't collected any stars... yet.")):
        # If the text is found, return an empty dataframe
        df = pd.DataFrame(columns=['Day', 'Time1', 'Rank1', 'Score1', 'Time2', 'Rank2', 'Score2'])

        # Complete the table with the missing days until the 25th
        for day in range(1, 26):
            df.loc[len(df)] = [day] + ["-"] * 6

        return df

    # Get the table of the leaderboard in the <pre> tag
    table = soup_page.find('pre')

    # Extract the text from the <pre> tag
    table_text = table.text

    # Remove the two first line of the table
    table_text = table_text.split('\n', 2)[2].split('\n')
    table_text = table_text[:-1]

    # Replace spaces by commas
    table_text = [re.sub(r'\s+', ',', line) for line in table_text]
    table_text = [re.sub(r'^,', '', line) for line in table_text]

    # Lire le tableau avec pandas
    columns = ['Day', 'Time1', 'Rank1', 'Score1', 'Time2', 'Rank2', 'Score2']
    df = pd.read_csv(io.StringIO('\n'.join(table_text)), names=columns)

    # Complete the table with the missing days until the 25th
    days = df['Day'].tolist()

    for day in range(1, 26):
        if day not in days:
            df.loc[len(df)] = [day] + ["-"] * 6

    # Reorder the lines by day
    df = df.sort_values(by=['Day'])

    return df


def get_progression(df):
    # Get the progression
    progression = []
    for line in df.iterrows():
        if line[1]['Rank1'] != "-" and line[1]['Rank2'] != "-":
            progression.append('█')
        elif line[1]['Rank1'] != "-":
            progression.append('▄')
        else:
            progression.append('_')

    # Get the number rank1 != 0
    progress_number = 25 - progression.count('_')

    # Format the string
    progression = ''.join(progression)
    progression = f'Progression : {progression} {progress_number}/25'

    return progression


def update_md(year, progression_bar, md_table):
    md_path = f'{year}/README.md'
    with open(md_path, 'r') as f:
        lines = f.readlines()
        f.close()

    # Update the progression
    for i, line in enumerate(lines):
        if line.startswith('Progression : '):
            lines[i] = f'{progression_bar}\n'

    # Find the line number of the table
    table_line = -1
    for i, line in enumerate(lines):
        if line.startswith('|   Day |'):
            table_line = i
            break

    if table_line == -1:
        raise ValueError('Table not found')

    # Replace the table and remove the old one
    lines[table_line] = md_table + '\n'
    lines = lines[:table_line + 1]

    # Write the new README.md
    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        f.close()


def update_main_readme(year, progression_bar):
    md_path = f'README.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.close()

    progression_bar = progression_bar.replace('Progression : ', '')

    # Update the progression
    for i, line in enumerate(lines):
        if line.startswith(f'| [{year}]({year}/README.md) |'):
            language = line.split('|')[3].strip()
            lines[i] = f'| [{year}]({year}/README.md) | `{progression_bar}` | {language} |\n'

    # Write the new README.md
    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        f.close()


if __name__ == '__main__':
    # get environment variables from .env file
    import os
    from dotenv import load_dotenv
    from pathlib import Path

    load_dotenv()
    SESSION_COOKIE = os.getenv('SESSION_COOKIE')

    # Get all the folder names
    folders = [folder for folder in Path('.').iterdir() if folder.is_dir()]

    # Only keep the folder names that are numbers
    folders = [folder for folder in folders if folder.name.isnumeric()]

    # Update the README.md of each folder
    for folder in folders:
        # Get the folder name
        year = folder.name
        print(f'Updating {year}...')

        # Get the personal leaderboard
        page = get_personal_leaderboard(year, {'session': SESSION_COOKIE})

        # Get the dataframe from the page
        dataframe = get_dataframe(page)

        # Print the dataframe as a Markdown table
        md_table = dataframe.to_markdown(index=False)

        # Get the progression bar
        progression_bar = get_progression(dataframe)
        print("Detected progression :", progression_bar)

        # Update the README.md
        update_md(year, progression_bar, md_table)
        update_main_readme(year, progression_bar)
