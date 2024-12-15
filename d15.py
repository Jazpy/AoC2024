import sys
from utils import Vec2


def get_gold_mat(mat):
    ret = [[] for l in mat]

    for l0, l1 in zip(mat, ret):
        for c in l0:
            if c == '#':
                l1.extend(['#', '#'])
            if c == '.':
                l1.extend(['.', '.'])
            if c == 'O':
                l1.extend(['[', ']'])
            if c == '@':
                l1.extend(['@', '.'])

    return ret


def push(mat, d, p, all_boxes):
    if Vec2.vsmart_get(mat, p) == '#':
        return False
    elif Vec2.vsmart_get(mat, p) == '.':
        return True

    left = Vec2.vsmart_get(mat, p) == '['
    other = p + Vec2(1, 0) if left else p + Vec2(-1, 0)

    if d.y == 1 or d.y == -1:
        clear = push(mat, d, p + d, all_boxes) and push(mat, d, other + d, all_boxes)
    elif d.x == 1:
        clear = push(mat, d, other + d if left else p + d, all_boxes)
    else:
        clear = push(mat, d, p + d if left else other + d, all_boxes)

    all_boxes.append((p, other)) if left else all_boxes.append((other, p))
    return clear


def apply_gold_move(m, mat, r):
    d = {'v': Vec2(0, 1), '^': Vec2(0, -1), '<': Vec2(-1, 0), '>': Vec2(1, 0)}[m]

    new_pos = Vec2(r.x, r.y) + d
    boxes = []
    clear = push(mat, d, new_pos, boxes)

    if clear:
        r += d

        if boxes:
            moved_boxes = set()
            for box in boxes:
                if box in moved_boxes:
                    continue
                moved_boxes.add(box)
                left, right = box
                mat[left.y][left.x] = '.'
                mat[right.y][right.x] = '.'
                mat[left.y + d.y][left.x + d.x] = '['
                mat[right.y + d.y][right.x + d.x] = ']'

    return r


def apply_move(m, mat, r):
    d = {'v': Vec2(0, 1), '^': Vec2(0, -1), '<': Vec2(-1, 0), '>': Vec2(1, 0)}[m]
    boxes = []
    stop = None

    new_pos = Vec2(r.x, r.y) + d
    while Vec2.vsmart_get(mat, new_pos) not in ['.', '#']:
        boxes.append(Vec2(new_pos.x, new_pos.y))
        new_pos += d
    stop = Vec2.vsmart_get(mat, new_pos)

    if stop == '.':
        r += d

        if boxes:
            mat[new_pos.y][new_pos.x] = 'O'
            mat[r.y][r.x] = '.'

    return r


with open(sys.argv[1]) as in_f:
    lines = in_f.readlines()

mat = [list(x.strip()) for x in lines[:50]]
gold_mat = get_gold_mat(mat)
moves = ''.join([x.strip() for x in lines[51:]])

#Silver
width = len(mat[0])
height = len(mat)
robot = None
for x in range(width):
    for y in range(height):
        if mat[y][x] == '@':
            robot = Vec2(x, y)
            mat[y][x] = '.'

for move in moves:
    robot = apply_move(move, mat, robot)

silver = 0
for x in range(width):
    for y in range(height):
        if mat[y][x] == 'O':
            silver += (y * 100) + x

# Gold
width = len(gold_mat[0])
height = len(gold_mat)
for x in range(width):
    for y in range(height):
        if gold_mat[y][x] == '@':
            robot = Vec2(x, y)
            gold_mat[y][x] = '.'

for move in moves:
    robot = apply_gold_move(move, gold_mat, robot)

gold = 0
for x in range(width):
    for y in range(height):
        if gold_mat[y][x] == '[':
            gold += (y * 100) + x

print(silver)
print(gold)
