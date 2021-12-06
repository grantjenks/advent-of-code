# Part 1
nums = list(map(int, text.split(',')))
days = [0] * 9
for num in nums:
    days[num] += 1
for _ in range(80):
    spawn = days[0]
    days[:8] = days[1:]
    days[6] += spawn
    days[8] = spawn
sum(days)

# Part 2
days = [0] * 9
for num in nums:
    days[num] += 1
for _ in range(256):
    spawn = days[0]
    days[:8] = days[1:]
    days[6] += spawn
    days[8] = spawn
sum(days)
