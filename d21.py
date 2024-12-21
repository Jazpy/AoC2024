import sys
from utils import Vec2


def get_numpad_moves(code):
    move_dic = {'0': Vec2(1, 0), '1': Vec2(2, 1), '2': Vec2(1, 1), '3': Vec2(0, 1),
                '4': Vec2(2, 2), '5': Vec2(1, 2), '6': Vec2(0, 2),
                '7': Vec2(2, 3), '8': Vec2(1, 3), '9': Vec2(0, 3), 'A': Vec2(0, 0)}

    curr = Vec2(0, 0)
    ret = []
    for c in code + 'A':
        move = move_dic[c] - curr
        curr = move_dic[c]
        ret.append(move)
    return ret


def get_dirpad_moves(moves, depth=1):
    ret = []
    for m in moves:
        curr = 0
        # UP
        if m.y > 0:
            # LEFT
            if m.x > 0:
                curr += 1 + abs(m.y) + 2 + abs(m.x) + 4
                ret.append('<' + 'A' * abs(m.y) + 'v<' + 'A' * abs(m.x) + '>>^A')
            # RIGHT
            elif m.x < 0:
                curr += 1 + abs(m.x) + 2 + abs(m.y) + 2
                ret.append('v' + 'A' * abs(m.x) + '<^' + 'A' * abs(m.y) + '>A')
            # NEUTRAL
            elif m.x == 0:
                curr += 1 + abs(m.y) + 2
                ret.append('<' + 'A' * abs(m.y) + '>A')
        # DOWN
        elif m.y < 0:
            # LEFT
            if m.x > 0:
                curr += 3 + abs(m.x) + 1 + abs(m.y) + 3
                ret.append('v<<' + 'A' * abs(m.x) + '>' + 'A' * abs(m.y) + '>^A')
            # RIGHT
            elif m.x < 0:
                curr += 1 + abs(m.x) + 1 + abs(m.y) + 3
                ret.append('v' + 'A' * abs(m.x) + '<' + 'A' * abs(m.y) + '>^A')
            # NEUTRAL
            elif m.x == 0:
                curr += 2 + abs(m.y) + 3
                ret.append('<v' + 'A' * abs(m.y) + '>^A')
        # NEUTRAL
        elif m.y == 0:
            # LEFT
            if m.x > 0:
                curr += 3 + abs(m.x) + 4
                ret.append('v<<' + 'A' * abs(m.x) + '>>^A')
            # RIGHT
            elif m.x < 0:
                curr += 1 + abs(m.x) + 2
                ret.append('v' + 'A' * abs(m.x) + '^A')
            # NEUTRAL
            elif m.x == 0:
                curr += 1
                ret.append('A')
    ret = ''.join(ret)
    return ret


def expand_dirpad(s):
    move_dic = {'v': Vec2(1, 0), '^': Vec2(1, 1), '<': Vec2(2, 0),
                '>': Vec2(0, 0), 'A': Vec2(0, 1)}
    ret = []
    curr = Vec2(0, 1)
    for c in s:
        m = move_dic[c] - curr
        curr = move_dic[c]

        # UP
        if m.y > 0:
            h = ('<' if m.x > 0 else '>') * abs(m.x)
            v = '^'
            ret.append(h + v + 'A')
        # DOWN
        else:
            h = ('<' if m.x > 0 else '>') * abs(m.x)
            v = 'v' * abs(m.y)
            ret.append(v + h + 'A')
    return ''.join(ret)


with open(sys.argv[1]) as in_f:
    codes = [x[:-2] for x in in_f.readlines()]

silver = 0
for c in codes:
    a = get_numpad_moves(c)
    d0 = get_dirpad_moves(a)
    d1 = expand_dirpad(d0)
    silver += len(d1) * int(c)
    print(c)
    print(d0)
    print(d1, len(d1))
print(silver)
