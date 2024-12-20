import sys
from utils import Vec2


def find_cheats(dists, paths, walls, skip, threshold):
    ret = 0
    for cheat in range(2, skip + 1):
        for p in paths:
            for n in p.manhattan_neighbors(cheat):
                if n in paths and dists[n] - (dists[p] + cheat) >= threshold:
                    ret += 1
    return ret


with open(sys.argv[1]) as in_f:
    mat = [x.strip() for x in in_f.readlines()]

paths = set()
walls = set()
for x in range(len(mat[0])):
    for y in range(len(mat)):
        if mat[y][x] == 'S':
            start = Vec2(x, y)
        elif mat[y][x] == 'E':
            end = Vec2(x, y)

        if mat[y][x] == '#':
            walls.add(Vec2(x, y))
        else:
            paths.add(Vec2(x, y))

dist = 0
dists = {}
stk = [start]
while stk:
    curr = stk.pop()
    dists[curr] = dist
    dist += 1

    for n in curr.manhattan_neighbors(1):
        if n in paths and n not in dists:
            stk.append(n)

print(find_cheats(dists, paths, walls, 2, 100))
print(find_cheats(dists, paths, walls, 20, 100))
