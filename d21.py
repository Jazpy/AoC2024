import sys
import itertools
from functools import cache
from utils import Vec2


def num_to_num(a, b):
    move_dic = {'0': Vec2(1, 0), '1': Vec2(2, 1), '2': Vec2(1, 1), '3': Vec2(0, 1),
                '4': Vec2(2, 2), '5': Vec2(1, 2), '6': Vec2(0, 2),
                '7': Vec2(2, 3), '8': Vec2(1, 3), '9': Vec2(0, 3), 'A': Vec2(0, 0)}

    a_p, b_p = move_dic[a], move_dic[b]
    x_off, y_off = b_p.x - a_p.x, b_p.y - a_p.y

    possibilities = set()
    x_char, y_char = '<' if x_off > 0 else '>', '^' if y_off > 0 else 'v'
    if not (x_off > 0 and a_p.y == 0 and a_p.x + x_off == 2):
        possibilities.add(x_char * abs(x_off) + y_char * abs(y_off) + 'A')
    if not (y_off < 0 and a_p.x == 2 and a_p.y + y_off == 0):
        possibilities.add(y_char * abs(y_off) + x_char * abs(x_off) + 'A')
    return list(possibilities)


def pad_to_pad(a, b):
    move_dic = {'v': Vec2(1, 0), '^': Vec2(1, 1), '<': Vec2(2, 0),
                '>': Vec2(0, 0), 'A': Vec2(0, 1)}

    a_p, b_p = move_dic[a], move_dic[b]
    x_off, y_off = b_p.x - a_p.x, b_p.y - a_p.y

    possibilities = set()
    x_char, y_char = '<' if x_off > 0 else '>', '^' if y_off > 0 else 'v'
    if not (x_off > 0 and a_p.y == 1 and a_p.x + x_off == 2):
        possibilities.add(x_char * abs(x_off) + y_char * abs(y_off) + 'A')
    if not (y_off > 0 and a_p.x == 2 and a_p.y + y_off == 1):
        possibilities.add(y_char * abs(y_off) + x_char * abs(x_off) + 'A')
    return list(possibilities)


@cache
def expand_dirpad(s, iters):
    if iters == 0:
        return len(s)

    chunks = []
    curr = 'A'
    for c in s:
        possibilities = pad_to_pad(curr, c)
        curr = c
        chunks.append(possibilities)

    ret = 0
    for chunk in chunks:
        ret += min([expand_dirpad(p, iters -1) for p in chunk])
    return ret


def solve(code, iters):
    code = 'A' + code + 'A'
    moves = [num_to_num(code[i], code[i + 1]) for i in range(len(code) - 1)]
    return sum([min([expand_dirpad(p, iters) for p in l]) for l in moves])


with open(sys.argv[1]) as in_f:
    codes = [x[:-2] for x in in_f.readlines()]

silver = 0
gold = 0
for c in codes:
    silver += solve(c, 2) * int(c)
    gold += solve(c, 25) * int(c)

print(silver)
print(gold)
