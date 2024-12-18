import sys
from utils import Vec2
from queue import PriorityQueue
from collections import defaultdict


def get_neighbors(u, walls, size=71):
    dirs = [Vec2(1, 0), Vec2(0, 1), Vec2(-1, 0), Vec2(0, -1)]
    ret = []

    for d in dirs:
        cell = u + d
        if cell.x < size and cell.x > -1 and cell.y < size and cell.y > -1 and cell not in walls:
            ret.append((1, cell))

    return ret


def flood(s, walls):
    ret = set()
    stk = [s]

    while stk:
        curr = stk.pop()
        if curr in ret:
            continue
        ret.add(curr)
        for w, n in get_neighbors(curr, walls):
            stk.append(n)

    return ret


with open(sys.argv[1]) as in_f:
    all_walls = [Vec2(int(line.split(',')[0]), int(line.split(',')[1])) for line in in_f]

size = 71
q = PriorityQueue()
dists = {}
for x in range(size):
    for y in range(size):
        dists[Vec2(x, y)] = sys.maxsize
end = Vec2(size - 1, size - 1)
start = Vec2(0, 0)
dists[Vec2(0, 0)] = 0
q.put((0, start))

silver_walls = set(all_walls[:1024])
silver = sys.maxsize
while not q.empty():
    dist, u = q.get()

    for w, n in get_neighbors(u, silver_walls):
        alt = dists[u] + w
        if alt < dists[n]:
            if n == end:
                silver = alt
            dists[n] = alt
            q.put((alt, n))

gold_walls = silver_walls
for wall in all_walls[1024:]:
    gold_walls.add(wall)
    f = flood(start, gold_walls)
    if end not in f:
        gold = wall
        break

print(silver)
print(gold)
