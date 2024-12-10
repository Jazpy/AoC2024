import sys
from collections import defaultdict
from copy import deepcopy


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
        return 100
    return mat[y][x]


def count_trail(mat, pos, l):
    curr_val = smart_get(mat, pos.x, pos.y)
    if curr_val == 9:
        l.add(pos)
        return 1

    count = 0
    if smart_get(mat, pos.x + 1, pos.y) == curr_val + 1:
        count += count_trail(mat, vec2(pos.x + 1, pos.y), l)
    if smart_get(mat, pos.x - 1, pos.y) == curr_val + 1:
        count += count_trail(mat, vec2(pos.x - 1, pos.y), l)
    if smart_get(mat, pos.x, pos.y + 1) == curr_val + 1:
        count += count_trail(mat, vec2(pos.x, pos.y + 1), l)
    if smart_get(mat, pos.x, pos.y - 1) == curr_val + 1:
        count += count_trail(mat, vec2(pos.x, pos.y - 1), l)

    return count


def count_trailheads(mat):
    silver = 0
    gold = 0

    trailheads = set()
    for x in range(len(mat[0])):
        for y in range(len(mat)):
            if smart_get(mat, x, y) == 0:
                trailheads.add(vec2(x, y))

    for head in trailheads:
        curr_set = set()
        gold += count_trail(mat, head, curr_set)
        silver += len(curr_set)

    return silver, gold


with open(sys.argv[1]) as in_f:
    mat = [[int(y) for y in x.strip()] for x in in_f.readlines()]

silver, gold = count_trailheads(mat)
print(silver)
print(gold)
