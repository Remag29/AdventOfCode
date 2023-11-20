def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    # load data
    board = load_data()

    # Slopes
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    trees_by_slope = []

    for slope in slopes:

        # Set the starting position
        position_x = 0
        position_y = 0

        # Get the last position of each axis
        lasty = len(board)
        lastx = len(board[0]) - 1  # -1 because of the \n, there is just 31 characters not 32

        # Move the toboggan and count the trees until the last position
        trees = 0
        while position_y < lasty:
            position_x = (position_x + slope[0]) % lastx
            position_y = position_y + slope[1]

            if position_y >= lasty:
                break

            if board[position_y][position_x] == '#':
                trees += 1

        trees_by_slope.append(trees)
        print("The toboggan hit", trees, "trees")

    print("Trees hit by each slope:", trees_by_slope)
    print("Multiplication of all trees:", trees_by_slope[0] * trees_by_slope[1] * trees_by_slope[2] * trees_by_slope[3] * trees_by_slope[4])
