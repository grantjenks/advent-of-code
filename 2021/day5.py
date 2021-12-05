# Part 1
lines = text.splitlines()
pairs = [line.split(' -> ') for line in lines]
for index in range(len(pairs)):
    start, end = pairs[index]
    start_x, start_y = map(int, start.split(','))
    end_x, end_y = map(int, end.split(','))
    pairs[index] = ((start_x, start_y), (end_x, end_y))
subset = [pair for pair in pairs if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]]
from collections import Counter
def points(start, end):
    start, end = sorted([start, end])
    s_x, s_y = start
    e_x, e_y = end
    if s_x == e_x:
        yield from ((s_x, s_y + offset) for offset in range(e_y - s_y + 1))
    elif s_y == e_y:
        yield from ((s_x + offset, s_y) for offset in range(e_x - s_x + 1))
    else:
        assert False, (start, end)
counts = Counter(point for start, end in subset for point in points(start, end))
sum(1 for _, count in counts.most_common() if count >= 2)

# Part 2
from itertools import repeat
def nums(start, end):
    if start == end:
        yield from repeat(start)
    elif end > start:
        yield from range(start, end + 1)
    else:
        assert start > end
        yield from range(start, end - 1, -1)
def points(start, end):
    s_x, s_y = start
    e_x, e_y = end
    yield from ((x, y) for x, y in zip(nums(s_x, e_x), nums(s_y, e_y)))
counts = Counter(point for start, end in pairs for point in points(start, end))
sum(1 for _, count in counts.most_common() if count >= 2)
