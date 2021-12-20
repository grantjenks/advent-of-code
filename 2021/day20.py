# Part 1
from collections import defaultdict
from itertools import cycle

algo, lines = text.split('\n\n')
image = defaultdict(lambda: '.')

for row, line in enumerate(lines.splitlines()):
    for col, char in enumerate(line):
        image[col, row] = char

pixel_to_bit = {'.': '0', '#': '1'}

def get_num(x, y):
    pixels = [image[i, j] for j in range(y-1, y+2) for i in range(x-1, x+2)]
    bits = ''.join(map(pixel_to_bit.get, pixels))
    num = int(bits, 2)
    return num

def zoom(default):
    global image
    min_x, min_y = min(image)
    max_x, max_y = max(image)

    new_image = defaultdict(lambda: default)
    for x in range(min_x - 2, max_x + 3):
        for y in range(min_y - 2, max_y + 3):
            num = get_num(x, y)
            new_image[x, y] = algo[num]

    image = new_image

def show(grid):
    min_x, min_y = min(image)
    max_x, max_y = max(image)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(image[x, y], end='')
        print()

zoom('#')
zoom('.')
print(sum(1 for pixel in image.values() if pixel == '#'))

# Part 2
defaults = cycle([algo[0], algo[511]])
for i, default in zip(range(48), defaults):
    zoom(default)
print(sum(1 for pixel in image.values() if pixel == '#'))
