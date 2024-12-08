import sys
from collections import defaultdict
from itertools import combinations


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
        return hash(tuple(self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'


with open(sys.argv[1]) as in_f:
    mat = [x.strip() for x in in_f.readlines()]
    height = len(mat)
    width = len(mat[0])

freqs = defaultdict(list)
for i in range(width):
    for j in range(height):
        if mat[j][i] != '.':
            freqs[mat[j][i]].append(vec2(i, j))

silver = 0
gold = 0
for i in range(width):
    for j in range(height):
        curr_pos = vec2(i, j)

        found = False
        gold_flag = False
        for freq, ps in freqs.items():
            if gold_flag and found:
                break

            for a0, a1 in combinations(ps, r=2):
                if gold_flag and found:
                    break

                d0 = curr_pos.distance(a0)
                d1 = curr_pos.distance(a1)
                colinear = curr_pos.colinear(a0, a1)

                if (d0 == d1 * 2 or d1 == d0 * 2) and colinear:
                    silver += 1
                    gold += 1
                    found = True

                if colinear:
                    gold_flag = True

        if gold_flag and not found:
            gold += 1

print(silver)
print(gold)
