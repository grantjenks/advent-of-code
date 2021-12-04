# Part 1
lines = text.splitlines()
from collections import Counter
most_commons = []
least_commons = []
for index in range(12):
    most_common = Counter(line[index] for line in lines).most_common(1)[0][0]
    most_commons.append(most_common)
    least_common = Counter(line[index] for line in lines).most_common()[-1][0]
    least_commons.append(least_common)
most_commons, least_commons
int(''.join(most_commons), 2) * int(''.join(least_commons), 2)

# Part 2
subset = list(lines)
for index in range(12):
    most_common = Counter(line[index] for line in subset).most_common()
    most_common = sorted(most_common, key=lambda pair: (pair[1], pair[0]), reverse=True)
    print(most_common)
    common = most_common[0][0]
    subset = [line for line in subset if line[index] == common]
int(subset[0], 2)
subset = list(lines)
for index in range(12):
    most_common = Counter(line[index] for line in subset).most_common()
    most_common = sorted(most_common, key=lambda pair: (pair[1], pair[0]), reverse=True)
    print(most_common)
    common = most_common[-1][0]
    subset = [line for line in subset if line[index] == common]
int(subset[0], 2)
781 * 2734
