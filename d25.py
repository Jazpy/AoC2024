import sys
from itertools import product


def proc_block(block, l):
    s = set()
    block = block.strip().split('\n')
    for y in range(1, len(block) - 1):
        for x in range(len(block[0])):
            if block[y][x] == '#':
                s.add((x, y))
    l.append(s)


keys = []
locks = []
blocks = open(sys.argv[1]).read().split('\n\n')
[proc_block(block, keys if block[:5] == '.....' else locks) for block in blocks]

silver = 0
for key, lock in product(keys, locks):
    if len(key.intersection(lock)) == 0:
        silver += 1

print(silver)
