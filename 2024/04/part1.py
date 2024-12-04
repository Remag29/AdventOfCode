import re


def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def obliques_45(tableau: list) -> list:
    n = len(tableau)
    diagonales = []

    # Parcourir les diagonales partant du bord supérieur
    for start_col in range(n):
        diagonale = [tableau[row][start_col + row] for row in range(n) if start_col + row < n]
        diagonales.append(diagonale)

    # Parcourir les diagonales partant du bord gauche (sauf la principale déjà incluse)
    for start_row in range(1, n):
        diagonale = [tableau[start_row + row][row] for row in range(n) if start_row + row < n]
        diagonales.append(diagonale)

    return diagonales


def obliques_minus_45(tableau: list) -> list:
    n = len(tableau)
    diagonales = []

    # Parcourir les diagonales partant du bord droit
    for start_col in range(n):
        diagonale = [tableau[row][start_col - row] for row in range(n) if 0 <= start_col - row < n]
        diagonales.append(diagonale)

    # Parcourir les diagonales partant du bord bas (sauf la principale déjà incluse)
    for start_row in range(1, n):
        diagonale = [tableau[start_row + row][n - 1 - row] for row in range(n) if
                     start_row + row < n and n - 1 - row >= 0]
        diagonales.append(diagonale)

    return diagonales


def find_xmas(row: str) -> int:
    regex_xmas = r'XMAS'
    regex_samx = r'SAMX'
    find_xmas = re.findall(regex_xmas, row)
    find_samx = re.findall(regex_samx, row)
    return len(find_samx + find_xmas)


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    # Make a big table
    base_table = []
    for line in lines:
        base_table.append(list(line.replace('\n', '')))

    # Make the transpose table
    transpose_table = list(map(list, zip(*base_table)))

    # Make the table for diagonal rows
    diagonal_45 = obliques_45(base_table)
    diagonal_minus_45 = obliques_minus_45(base_table)

    # Find XMAS on every table
    xmas_count = 0

    # 1 base table
    for line in base_table:
        string = ''.join(line)
        xmas_count += find_xmas(string)

    # 2 transpose table
    for line in transpose_table:
        string = ''.join(line)
        xmas_count += find_xmas(string)

    # 3 diagonal 45
    for line in diagonal_45:
        string = ''.join(line)
        xmas_count += find_xmas(string)

    # 4 diagonal minus 45
    for line in diagonal_minus_45:
        string = ''.join(line)
        xmas_count += find_xmas(string)

    print(f'The result is {xmas_count}')

# 2465 : To low