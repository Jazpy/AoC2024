import sys


def smart_get(mat, width, height, x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return '.'
    return mat[y][x]

def find_xmas(mat, width, height, x, y):
    ret = 0

    # RIGHT
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x + i, y)
    ret += 1 if s == 'MAS' else 0
    # LEFT
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x - i, y)
    ret += 1 if s == 'MAS' else 0
    # UP
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x, y - i)
    ret += 1 if s == 'MAS' else 0
    # DOWN
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x, y + i)
    ret += 1 if s == 'MAS' else 0
    # UP RIGHT
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x + i, y - i)
    ret += 1 if s == 'MAS' else 0
    # UP LEFT
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x - i, y - i)
    ret += 1 if s == 'MAS' else 0
    # DOWN RIGHT
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x + i, y + i)
    ret += 1 if s == 'MAS' else 0
    # DOWN LEFT
    s = ''
    for i in range(1, 4):
        s += smart_get(mat, width, height, x - i, y + i)
    ret += 1 if s == 'MAS' else 0

    return ret

def find_xmas_p(mat, width, height, x, y):
    diag_0 = smart_get(mat, width, height, x - 1, y - 1) + smart_get(mat, width, height, x + 1, y + 1)
    diag_1 = smart_get(mat, width, height, x - 1, y + 1) + smart_get(mat, width, height, x + 1, y - 1)

    if diag_0 in ['MS', 'SM'] and diag_1 in ['MS', 'SM']:
        return 1
    return 0

with open(sys.argv[1]) as in_f:
    mat = in_f.readlines()
    height = len(mat)
    width = len(mat[0])

xs = []
ys = []
for i in range(width):
    for j in range(height):
        if mat[j][i] == 'X':
            xs.append((i, j))
        if mat[j][i] == 'A':
            ys.append((i, j))

silver = 0
for (x, y) in xs:
    silver += find_xmas(mat, width, height, x, y)

gold = 0
for (x, y) in ys:
    gold += find_xmas_p(mat, width, height, x, y)

print(silver)
print(gold)
