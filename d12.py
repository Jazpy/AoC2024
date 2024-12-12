import sys
from collections import defaultdict


class vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, o):
        return abs(self.x - o.x) + abs(self.y - o.y)

    def colinear(self, o0, o1):
        return (self.y - o0.y) * (self.x - o1.x) == (self.y - o1.y) * (self.x - o0.x)

    def __add__(self, o):
        return vec2(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return vec2(self.x - o.x, self.y - o.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __repr__(self):
        return f'({self.x}, {self.y})'


def smart_get(mat, x, y):
    if x < 0 or x >= len(mat[0]) or y < 0 or y >= len(mat):
        return '!'
    return mat[y][x]


def color_region(mat, visited, flower, region, curr_p):
    if curr_p in visited:
        return

    visited.add(curr_p)
    region.append(curr_p)

    if flower == smart_get(mat, curr_p.x + 1, curr_p.y):
        color_region(mat, visited, flower, region, vec2(curr_p.x + 1, curr_p.y))
    if flower == smart_get(mat, curr_p.x - 1, curr_p.y):
        color_region(mat, visited, flower, region, vec2(curr_p.x - 1, curr_p.y))
    if flower == smart_get(mat, curr_p.x, curr_p.y + 1):
        color_region(mat, visited, flower, region, vec2(curr_p.x, curr_p.y + 1))
    if flower == smart_get(mat, curr_p.x, curr_p.y - 1):
        color_region(mat, visited, flower, region, vec2(curr_p.x, curr_p.y - 1))


def get_gold_price(mat, region):
    n_map = {'R': [vec2(0, 1), vec2(0, -1)],
             'L': [vec2(0, 1), vec2(0, -1)],
             'D': [vec2(1, 0), vec2(-1, 0)],
             'U': [vec2(1, 0), vec2(-1, 0)]}
    sides = set()
    flower = region[0]
    points = region[1]
    area = len(points)
    gold = 0
    for p in points:
        curr_sides = set()
        if flower != smart_get(mat, p.x + 1, p.y):
            curr_sides.add(('R', p))
        if flower != smart_get(mat, p.x - 1, p.y):
            curr_sides.add(('L', p))
        if flower != smart_get(mat, p.x, p.y + 1):
            curr_sides.add(('D', p))
        if flower != smart_get(mat, p.x, p.y - 1):
            curr_sides.add(('U', p))

        sides = sides.union(curr_sides)

    visited_sides = set()
    for side in sides:
        if side not in visited_sides:
            dir = side[0]
            pos = side[1]
            visited_sides.add(side)
            gold += 1

            for off_dir in n_map[dir]:
                curr_pos = pos + off_dir
                while (dir, curr_pos) in sides and (dir, curr_pos) not in visited_sides:
                    visited_sides.add((dir, curr_pos))
                    curr_pos += off_dir

    return gold * area


def get_price(mat, region):
    flower = region[0]
    points = region[1]
    area = len(points)
    perimeter = 0
    for p in points:
        if flower != smart_get(mat, p.x + 1, p.y):
            perimeter += 1
        if flower != smart_get(mat, p.x - 1, p.y):
            perimeter += 1
        if flower != smart_get(mat, p.x, p.y + 1):
            perimeter += 1
        if flower != smart_get(mat, p.x, p.y - 1):
            perimeter += 1

    return area * perimeter


def silver_solve(mat):
    ret = 0
    visited = set()
    regions = []

    for x in range(len(mat[0])):
        for y in range(len(mat)):
            curr_p = vec2(x, y)
            if curr_p in visited:
                continue
            new_region = (mat[y][x], [])
            color_region(mat, visited, new_region[0], new_region[1], curr_p)
            regions.append(new_region)

    for region in regions:
        ret += get_price(mat, region)

    return ret


def gold_solve(mat):
    ret = 0
    visited = set()
    regions = []

    for x in range(len(mat[0])):
        for y in range(len(mat)):
            curr_p = vec2(x, y)
            if curr_p in visited:
                continue
            new_region = (mat[y][x], [])
            color_region(mat, visited, new_region[0], new_region[1], curr_p)
            regions.append(new_region)

    for region in regions:
        ret += get_gold_price(mat, region)

    return ret


with open(sys.argv[1]) as in_f:
    mat = [x.strip() for x in in_f.readlines()]

print(silver_solve(mat))
print(gold_solve(mat))
