# Part 1
lines = text.splitlines()
match = {')': '(', ']': '[', '}': '{', '>': '<'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0
for line in lines:
    stack = []
    for char in line:
        if char in match:
            prev = stack.pop()
            if prev != match[char]:
                total += points[char]
                break
        else:
            stack.append(char)
total

# Part 2
rematch = {value: key for key, value in match.items()}
subtotals = []
for line in lines:
    stack = []
    for char in line:
        if char in match:
            prev = stack.pop()
            if prev != match[char]:
                break
        else:
            stack.append(char)
    else:
        subtotal = 0
        table = '0)]}>'
        for char in reversed(stack):
            subtotal *= 5
            subtotal += table.index(rematch[char])
        subtotals.append(subtotal)
sorted(subtotals)[len(subtotals) // 2]
