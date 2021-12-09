from collections import defaultdict
from heapq import nlargest
from math import prod


# Part 2
nums = defaultdict(lambda: 9)
lines = text.splitlines()

for row, line in enumerate(lines):
    for col, num in enumerate(line):
        nums[row, col] = int(num)

graph = nx.Graph()

for (row, col), value in list(nums.items()):
    if value == 9:
        continue
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y in offsets:
        if nums[row+x, col+y] != 9:
            graph.add_edge((row, col), (row+x, col+y))

lengths = (len(subgraph) for subgraph in nx.connected_components(graph))
prod(nlargest(3, lengths))
