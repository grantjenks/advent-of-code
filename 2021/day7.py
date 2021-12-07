# Part 1
nums = list(map(int, text.split(',')))
min(nums)
max(nums)
len(nums)
changes = []
for value in range(min(nums), max(nums) + 1):
    change = sum(abs(num - value) for num in nums)
    changes.append(change)
min(changes)

# Part 2
def cost(n):
    return n * (n + 1) // 2
changes = []
for value in range(min(nums), max(nums) + 1):
    change = sum(cost(abs(num - value)) for num in nums)
    changes.append(change)
min(changes)
