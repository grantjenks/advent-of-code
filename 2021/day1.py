# Part 1
nums = list(map(int, text.splitlines()))
sum(1 for first, second in zip(nums, nums[1:]) if second > first)

# Part 2
def triplets(nums):
    return zip(nums, nums[1:], nums[2:])
iter1 = (sum(triplet) for triplet in zip(nums, nums[1:], nums[2:]))
iter2 = (sum(triplet) for triplet in zip(nums[1:], nums[2:], nums[3:]))
sum(1 for first, second in zip(iter1, iter2) if second > first)
