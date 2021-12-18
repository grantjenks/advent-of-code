# Part 1
parts = text.split()
x_lo, x_hi = map(int, parts[2][2:-1].split('..'))
y_lo, y_hi = map(int, parts[3][2:].split('..'))

def simulate(vx, vy):
    x = y = 0
    ys = []
    target = False
    while x <= x_hi and y >= y_lo:
        target |= (x_lo <= x <= x_hi) & (y_lo <= y <= y_hi)
        ys.append(y)
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
    ys.append(y)
    return target, max(ys)

max_ys = []
for vx in range(1, x_hi + 1):
    for vy in range(-y_lo + 1):
        x = y = 0
        target, max_y = simulate(vx, vy)
        if target:
            max_ys.append(max_y)

print(max(max_ys))

# Part 2
vs = []

for vx in range(1, x_hi + 1):
    for vy in range(y_lo, -y_lo + 1):
        target, max_y = simulate(vx, vy)
        if target:
            vs.append((vx, vy))

print(len(vs))
