# Part 1
lines = text.splitlines()
folds = [line for line in lines if line.startswith('fold along ')]
len(folds)
coords = lines[:-13]
coords = {tuple(coord.split(',')) for coord in coords}
coords = {(int(x), int(y)) for x, y in coords}

def fold(coords, x_fold=None, y_fold=None):
    result = set()
    if y_fold is None:
        for x, y in coords:
            if x > x_fold:
                pair = (x_fold - (x - x_fold), y)
                result.add(pair)
            else:
                result.add((x, y))
    else:
        assert x_fold is None
        for x, y in coords:
            if y > y_fold:
                pair = (x, y_fold - (y - y_fold))
                result.add(pair)
            else:
                result.add((x, y))
    return result

coords0 = fold(coords, x_fold=655)
len(coords0)

# Part 2
folds = [fold[11:].split('=') for fold in folds]
folds = [{pos + '_fold': int(num)} for pos, num in folds]
make_fold = fold
result = set(coords)

for fold in folds:
    result = make_fold(result, **fold)

max(x for x, y in result)
max(y for x, y in result)
dots = {(x, y): ' ' for x in range(39) for y in range(6)}

for x, y in result:
    dots[x, y] = '*'

for y in range(6):
    for x in range(39):
        print(dots[x, y], end='')
    print()
