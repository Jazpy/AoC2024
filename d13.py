import sys


def parse_block(l):
    toks = l[0].split(',')
    ax = int(toks[0].split('+')[1])
    ay = int(toks[1].split('+')[1])
    toks = l[1].split(',')
    bx = int(toks[0].split('+')[1])
    by = int(toks[1].split('+')[1])
    toks = l[2].split(',')
    px = int(toks[0].split('=')[1])
    py = int(toks[1].split('=')[1])

    return (ax, ay, bx, by, px, py)


def solve(l):
    silver = 0
    gold = 0
    ax, ay, bx, by, px, py = parse_block(l)

    b = ((ax * py) - (ay * px)) / ((by * ax) - (ay * bx))
    a = (px - (b * bx)) / ax

    if b <= 100 and a <= 100 and b > 0 and a > 0 and a.is_integer() and b.is_integer():
        silver = int(a * 3 + b)

    px += 10000000000000
    py += 10000000000000
    b = ((ax * py) - (ay * px)) / ((by * ax) - (ay * bx))
    a = (px - (b * bx)) / ax

    if a.is_integer() and b.is_integer():
        gold = int(a * 3 + b)

    return silver, gold


silver = 0
gold = 0
with open(sys.argv[1]) as in_f:
    buffer = []
    for line in in_f:
        line = line.strip()
        buffer.append(line)
        if not line:
            s, g = solve(buffer)
            silver += s
            gold += g
            buffer = []
if buffer:
    s, g = solve(buffer)
    silver += s
    gold += g

print(silver)
print(gold)
