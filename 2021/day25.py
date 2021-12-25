# Part 1
lines = text.splitlines()
grid = {}

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        grid[row, col] = char

max_row, max_col = max(grid)
max_row += 1
max_col += 1

def step():
    count = 0
    new_grid = grid.copy()
    # Move east
    moves = []
    for (row, col), char in new_grid.items():
        if char != '>':
            continue
        next_col = (col + 1) % max_col
        if new_grid[row, next_col] == '.':
            move = row, col, row, next_col
            moves.append(move)
    count += len(moves)
    for row, col, next_row, next_col in moves:
        new_grid[row, col] = '.'
        new_grid[next_row, next_col] = '>'
    # Move south
    moves = []
    for (row, col), char in new_grid.items():
        if char != 'v':
            continue
        next_row = (row + 1) % max_row
        if new_grid[next_row, col] == '.':
            move = row, col, next_row, col
            moves.append(move)
    count += len(moves)
    for row, col, next_row, next_col in moves:
        new_grid[row, col] = '.'
        new_grid[next_row, next_col] = 'v'
    return new_grid, count

from itertools import count

def show():
    print('Grid:')
    for row in range(max_row):
        for col in range(max_col):
            print(grid[row, col], end='')
        print()

for iteration in count(start=1):
    new_grid, count = step()
    if count == 0:
        break
    grid = new_grid

print(iteration)
