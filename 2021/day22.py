# Part 1
lines = text.splitlines()
steps = []

for line in lines:
    state, details = line.split(' ')
    state = {'on': 1, 'off': 0}.get(state)
    parts = [part[2:].split('..') for part in details.split(',')]
    pair = state, [tuple(map(int, part)) for part in parts]
    steps.append(pair)

from itertools import product

cubes = {}

for state, [(x_min, x_max), (y_min, y_max), (z_min, z_max)] in steps:
    iterator = product(
        range(max(x_min, -50), min(x_max, 50) + 1),
        range(max(y_min, -50), min(y_max, 50) + 1),
        range(max(z_min, -50), min(z_max, 50) + 1),
    )
    for x, y, z in iterator:
        cubes[x, y, z] = state

print('Part 1', sum(cubes.values()))

# Part 2 (copied)
from collections import Counter

cubes = Counter()

for state, [(nx0, nx1), (ny0, ny1), (nz0, nz1)] in steps:
    nsgn = 1 if state == 1 else -1
    update = Counter()

    for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cubes.items():
        ix0 = max(nx0, ex0); ix1 = min(nx1, ex1)
        iy0 = max(ny0, ey0); iy1 = min(ny1, ey1)
        iz0 = max(nz0, ez0); iz1 = min(nz1, ez1)

        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn

    if nsgn > 0:
        update[(nx0, nx1, ny0, ny1, nz0, nz1)] += nsgn

    cubes.update(update)

print(sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
          for (x0, x1, y0, y1, z0, z1), sgn in cubes.items()))
