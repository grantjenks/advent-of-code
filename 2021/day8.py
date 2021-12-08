# Part 1
lines = text.splitlines()
lines = [line.split(' | ') for line in lines]
lines = [[left.split(), right.split()] for left, right in lines]
sum(1 for _, right in lines for token in right if len(token) in {2, 4, 3, 7})

# Part 2
def codings(nums):
    nums = list(map(frozenset, nums))
    one = next(num for num in nums if len(num) == 2)
    four = next(num for num in nums if len(num) == 4)
    seven = next(num for num in nums if len(num) == 3)
    eight = next(num for num in nums if len(num) == 7)
    three = next(num for num in nums if len(num) == 5 and one < num)
    five = next(num for num in nums if len(num) == 5 and (four - one) < num)
    six = next(num for num in nums if len(num) == 6 and not (one < num))
    nine = next(num for num in nums if len(num) == 6 and one < num and four < num)
    zero = next(num for num in nums if len(num) == 6 and num != six and num != nine)
    two = next(iter(set(nums) - {zero, one, three, four, five, six, seven, eight, nine}))
    return {zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9}

def parse(left, right):
    codes = codings(left)
    return int(''.join(map(str, list(map(codes.get, map(frozenset, right))))))

sum(parse(left, right) for left, right in lines)
