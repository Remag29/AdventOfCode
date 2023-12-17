from part1 import load_data, is_in_board


if __name__ == '__main__':
    # load data
    lines = load_data()

    board = [list(line.strip().replace('\n', '')) for line in lines]

    # Get all start positions
    possible_starts = []

    # First row
    for i in range(len(board[0])):
        possible_starts.append(((0, i), 'D'))
    # Last row
    for i in range(len(board[-1])):
        possible_starts.append(((len(board) - 1, i), 'U'))
    # First column
    for i in range(len(board)):
        possible_starts.append(((i, 0), 'R'))
    # Last column
    for i in range(len(board)):
        possible_starts.append(((i, len(board[0]) - 1), 'L'))

    max_len = 0

    for start, direction in possible_starts:

        directions = [direction]
        node_to_move = [start]
        previous_seen = set()
        seen = set((start[0],start[1]))
        seen_verticaly = set()
        seen_horizontally = set()

        while node_to_move:
            x, y = node_to_move.pop(0)
            direction = directions.pop(0)

            if board[x][y] == '.':
                if direction == 'R':
                    nodes = [(x, y + 1)]
                    directions_temp = ['R']
                elif direction == 'L':
                    nodes = [(x, y - 1)]
                    directions_temp = ['L']
                elif direction == 'U':
                    nodes = [(x - 1, y)]
                    directions_temp = ['U']
                elif direction == 'D':
                    nodes = [(x + 1, y)]
                    directions_temp = ['D']

            elif board[x][y] == '-':
                if direction == 'R':
                    nodes = [(x, y + 1)]
                    directions_temp = ['R']
                    seen_horizontally.add((x, y))
                elif direction == 'L':
                    nodes = [(x, y - 1)]
                    seen_horizontally.add((x, y))
                    directions_temp = ['L']
                elif direction in ['U', 'D']:
                    nodes = [(x, y - 1), (x, y + 1)]
                    directions_temp = ['L', 'R']
                    seen_verticaly.add((x, y))

            elif board[x][y] == '|':
                if direction == 'U':
                    nodes = [(x - 1, y)]
                    seen_verticaly.add((x, y))
                    directions_temp = ['U']
                elif direction == 'D':
                    nodes = [(x + 1, y)]
                    seen_verticaly.add((x, y))
                    directions_temp = ['D']
                elif direction in ['R', 'L']:
                    nodes = [(x - 1, y), (x + 1, y)]
                    directions_temp = ['U', 'D']
                    seen_horizontally.add((x, y))

            elif board[x][y] == '/':
                if direction == 'R':
                    nodes = [(x - 1, y)]
                    directions_temp = ['U']
                elif direction == 'L':
                    nodes = [(x + 1, y)]
                    directions_temp = ['D']
                elif direction == 'U':
                    nodes = [(x, y + 1)]
                    directions_temp = ['R']
                elif direction == 'D':
                    nodes = [(x, y - 1)]
                    directions_temp = ['L']

            elif board[x][y] == '\\':
                if direction == 'R':
                    nodes = [(x + 1, y)]
                    directions_temp = ['D']
                elif direction == 'L':
                    nodes = [(x - 1, y)]
                    directions_temp = ['U']
                elif direction == 'U':
                    nodes = [(x, y - 1)]
                    directions_temp = ['L']
                elif direction == 'D':
                    nodes = [(x, y + 1)]
                    directions_temp = ['R']

            # Add new nodes to move
            for i, node in enumerate(nodes):
                if is_in_board(node, board) and node not in seen_verticaly and node not in seen_horizontally:
                    node_to_move.append(node)
                    seen.add(node)
                    directions.append(directions_temp[i])

            if node_to_move == []:
                break
        if len(seen) > max_len:
            max_len = len(seen)
            max_node = start
    print(max_len - 2) # Minus 2 because the seen set is including the start node int coord (why ??? cant figure out)
    print(max_node)