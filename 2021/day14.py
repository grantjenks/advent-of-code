# Part 1
lines = text.splitlines()
code = lines[0]
rules = lines[2:]
rules = [rule.split(' -> ') for rule in rules]

def expand(code, rules):
    prev = code[0]
    result = [prev]
    for i in range(1, len(code)):
        pair = code[i-1:i+1]
        middle = rules[pair]
        result.append(middle)
        result.append(code[i])
    return ''.join(result)

rules = dict(rules)
result = code

for i in range(10):
    result = expand(result, rules)

from collections import Counter
pairs = Counter(result).most_common()
print(pairs[0][1] - pairs[-1][1])

# Part 2
from collections import defaultdict

def expand(counts):
    new_counts = defaultdict(int)
    for pair, num in counts.items():
        a, b = pair
        new_counts[a + rules[pair]] += num
        new_counts[rules[pair] + b] += num
    return dict(new_counts)

counts = Counter(code[i-1:i+1] for i in range(1, len(code)))

for i in range(40):
    counts = expand(counts)

result = Counter()

for key, num in counts.items():
    for letter in key:
        result[letter] += num

result[code[0]] += 1
result[code[-1]] += 1

for key, num in result.items():
    result[key] = num // 2

pairs = result.most_common()
print(pairs[0][1] - pairs[-1][1])
