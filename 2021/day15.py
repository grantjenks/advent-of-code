# Part 1
lines = text.splitlines()

from collections import defaultdict

grid = defaultdict(lambda: float('inf'))

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        grid[row, col] = int(char)

cost = {}
heap = [(0, (0, 0))]

while heap:
    risk, xy = heapq.heappop(heap)
    prev = cost.get(xy, float('inf'))
    if risk < prev:
        cost[xy] = risk
        x, y = xy
        for dx, dy in diffs:
            neighbor = x + dx, y + dy
            pair = risk + grid[neighbor], neighbor
            heapq.heappush(heap, pair)

print(cost[max(cost)])

# Part 2
grid = defaultdict(lambda: float('inf'))

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        grid[row, col] = int(char)

max_x, max_y = max(grid)
max_x += 1
max_y += 1

for x in range(max_x, max_x * 5):
    for y in range(max_y):
        px = x - max_x
        grid[x, y] = grid[px, y] + 1
        if grid[x, y] == 10:
            grid[x, y] = 1

for y in range(max_y, max_y * 5):
    for x in range(max_x * 5):
        py = y - max_y
        grid[x, y] = grid[x, py] + 1
        if grid[x, y] == 10:
            grid[x, y] = 1

cost = {}
heap = [(0, (0, 0))]

while heap:
    risk, xy = heapq.heappop(heap)
    prev = cost.get(xy, float('inf'))
    if risk < prev:
        cost[xy] = risk
        x, y = xy
        for dx, dy in diffs:
            neighbor = x + dx, y + dy
            pair = risk + grid[neighbor], neighbor
            heapq.heappush(heap, pair)

print(cost[max(cost)])
