# Part 1
lines = text.splitlines()
position = 0
depth = 0
for line in lines:
    command, amount = line.split()
    amount = int(amount)
    if command == 'forward':
        position += amount
    elif command == 'down':
        depth += amount
    elif command == 'up':
        depth -= amount
    else:
        assert False, line
position * depth

# Part 2
position = depth = aim = 0
for line in lines:
    command, amount = line.split()
    amount = int(amount)
    if command == 'forward':
        position += amount
        depth += (aim * amount)
    elif command == 'down':
        aim += amount
    elif command == 'up':
        aim -= amount
    else:
        assert False, line
position, depth, position * depth
