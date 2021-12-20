# Part 1
from itertools import permutations, product
from operator import itemgetter, pos, neg, sub

chunks = text.split('\n\n')
scanners = {}

for chunk in chunks:
    header, *lines = chunk.splitlines()
    scanner = int(header.split()[2])
    coords = {tuple(map(int, line.split(','))) for line in lines}
    scanners[scanner] = coords

signers = list(product(*([[pos, neg]] * 3)))
indexers = list(permutations(list(map(itemgetter, range(3)))))
dist_from_0 = [(0,0,0)]

def compare(scan_a, scan_b):
    for signer, indexer in product(signers, indexers):
        transform_b = {
            tuple(sign(index(pos)) for sign, index in zip(signer, indexer))
            for pos in scan_b
        }
        for pos_a, pos_b in product(scan_a, transform_b):
            offsets = tuple(sub(*dims) for dims in zip(pos_b, pos_a))
            matches = 0
            pos_a_alts = set()
            for pos_b_alt in transform_b:
                pairs = zip(pos_b_alt, offsets)
                pos_a_alt = tuple(sub(*pair) for pair in pairs)
                if pos_a_alt in scan_a:
                    matches += 1
                pos_a_alts.add(pos_a_alt)
            if matches >= 12:
                print('Matched! Offsets:', offsets)
                dist_from_0.append(tuple(offsets))
                return pos_a_alts

aligned = {0: scanners[0]}
all_aligned = set(scanners[0])
misaligned = set()

while len(aligned) < len(scanners):
    for scanners_key in range(len(scanners)):
        if scanners_key in aligned:
            continue
        for aligned_key in aligned:
            pair = (scanners_key, aligned_key)
            print('Checking', pair)
            if pair in misaligned:
                continue
            scan = compare(aligned[aligned_key], scanners[scanners_key])
            if scan:
                aligned[scanners_key] = scan
                all_aligned.update(scan)
                break
            misaligned.add(pair)

print(len(all_aligned))

# Part 2
print(
    max(
        sum(abs(sub(*diff)) for diff in zip(dist_a, dist_b))
        for dist_a, dist_b in product(dist_from_0, dist_from_0)
    )
)
