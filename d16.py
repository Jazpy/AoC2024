import sys
from utils import Vec2
from queue import PriorityQueue
from collections import defaultdict


def get_neighbors(mat, u, d):
    dir_map = {0: Vec2(1, 0), 1: Vec2(0, 1), 2: Vec2(-1, 0), 3: Vec2(0, -1)}
    direction = dir_map[d]
    ret = []

    if Vec2.vsmart_get(mat, u + direction) != '#':
        ret.append((1, (u + direction, d)))
    ret.append((1000, (u, (d + 1) % 4)))
    ret.append((1000, (u, (d - 1) % 4)))

    return ret


with open(sys.argv[1]) as in_f:
    mat = [list(x.strip()) for x in in_f.readlines()]

width = len(mat[0])
height = len(mat)

q = PriorityQueue()
dists = {}
prev = defaultdict(list)
start = None
end = None
for x in range(width):
    for y in range(height):
        if mat[y][x] in ['E', '.']:
            for d in range(4):
                dists[(Vec2(x, y), d)] = sys.maxsize
        if mat[y][x] == 'E':
            end = Vec2(x, y)
        if mat[y][x] == 'S':
            start = Vec2(x, y)
            dists[(Vec2(x, y), 0)] = 0
            dists[(Vec2(x, y), 1)] = sys.maxsize
            dists[(Vec2(x, y), 2)] = sys.maxsize
            dists[(Vec2(x, y), 3)] = sys.maxsize
            q.put((0, (Vec2(x, y), 0)))


silver = sys.maxsize
while not q.empty():
    dist, (u, d) = q.get()

    for w, n in get_neighbors(mat, u, d):
        alt = dists[(u, d)] + w
        if alt <= dists[n]:
            prev[n].append((alt, (u, d)))
        if alt < dists[n]:
            if n[0] == end and alt < silver:
                silver = alt
            dists[n] = alt
            q.put((alt, n))

# Gold
for key, val in prev.items():
    prev[key] = [x for x in val if x[0] == min([x[0] for x in val])]

gold = set([end])
stk = prev[(end, 0)]
while stk:
    v = stk.pop()[1]
    gold.add(v[0])
    stk.extend(prev[v])

print(silver)
print(len(gold))
