import sys
from collections import defaultdict


def smart_get(mat, width, height, x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return None
    return mat[y][x]

def silver_walk(mat, guard_pos, width, height):
    dir_map = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}
    guard_dir = 0
    dir_dict = defaultdict(set)

    silver = set()

    while smart_get(mat, width, height, guard_pos[0], guard_pos[1]) is not None:
        silver.add((guard_pos[0], guard_pos[1]))

        next_pos = [guard_pos[0] + dir_map[guard_dir][0], guard_pos[1] + dir_map[guard_dir][1]]
        next_cell = smart_get(mat, width, height, next_pos[0], next_pos[1])

        if next_cell == '#':
            guard_dir = (guard_dir + 1) % 4
        else:
            guard_pos[0] = next_pos[0]
            guard_pos[1] = next_pos[1]

    return len(silver)

def loop_check(mat, guard_pos, width, height):
    dir_map = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}
    guard_dir = 0
    dir_dict = defaultdict(set)
    steps = 0

    while smart_get(mat, width, height, guard_pos[0], guard_pos[1]) is not None:
        steps += 1
        if steps > 10000:
            return 1

        next_pos = [guard_pos[0] + dir_map[guard_dir][0], guard_pos[1] + dir_map[guard_dir][1]]
        next_cell = smart_get(mat, width, height, next_pos[0], next_pos[1])

        if next_cell == '#':
            guard_dir = (guard_dir + 1) % 4
        else:
            guard_pos[0] = next_pos[0]
            guard_pos[1] = next_pos[1]

    return 0

with open(sys.argv[1]) as in_f:
    lines = in_f.readlines()
    mat = []
    for line in lines:
        mat.append([x for x in line.strip()])
    height = len(mat)
    width = len(mat[0])

for i in range(width):
    for j in range(height):
        if mat[j][i] == '^':
            guard_pos = [i, j]
            mat[j][i] = '.'
            break

silver = silver_walk(mat, list(guard_pos), width, height)
gold = 0

for i in range(width):
    for j in range(height):
        if mat[j][i] == '.':
            mat[j][i] = '#'
            gold += loop_check(mat, list(guard_pos), width, height)
            mat[j][i] = '.'

print(silver)
print(gold)
