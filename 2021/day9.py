from collections import defaultdict

# Part 1
lines = text.splitlines()
nums = defaultdict(lambda: 9)
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        nums[row, col] = char
for key, value in nums.items():
    nums[key] = int(value)
total = 0
for (row, col), value in list(nums.items()):
    low_point = (
        value < nums[row-1, col]
        and value < nums[row+1, col]
        and value < nums[row, col-1]
        and value < nums[row, col+1]
    )
    if low_point:
        total += value + 1
total

# Part 2
def basin_size(row, col):
    visited = set()
    count = 0
    def visit(row, col):
        nonlocal count
        if (row, col) in visited:
            return
        visited.add((row, col))
        if nums[row, col] == 9:
            return
        count += 1
        pairs = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for row, col in pairs:
            visit(row, col)
    visit(row, col)
    return count
sizes = []
for (row, col), value in list(nums.items()):
    low_point = (
        value < nums[row-1, col]
        and value < nums[row+1, col]
        and value < nums[row, col-1]
        and value < nums[row, col+1]
    )
    if low_point:
        sizes.append(basin_size(row, col))
sorted(sizes)[-3:]
114 * 116 * 121
