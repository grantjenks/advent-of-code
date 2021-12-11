# Part 1
lines = text.splitlines()
from collections import defaultdict
grid = defaultdict(lambda: 0)
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        grid[row, col] = int(char)

neighbors = {(x, y) for x in range(-1, 2) for y in range(-1, 2)}
neighbors.remove((0, 0))

def step():
    for key, value in grid.items():
        grid[key] += 1
    flashers = set()
    found = True
    while found:
        found = False
        for row in range(10):
            for col in range(10):
                if grid[row, col] > 9 and (row, col) not in flashers:
                    found = True
                    pair = row, col
                    flashers.add(pair)
                    for x, y in neighbors:
                        grid[row+x, col+y] += 1
    for pair in flashers:
        grid[pair] = 0
    return len(flashers)

sum(step() for _ in range(100))

# Part 2
grid = defaultdict(lambda: 0)
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        grid[row, col] = int(char)

from itertools import count

next(n for n in count(1) if step() == 100)
