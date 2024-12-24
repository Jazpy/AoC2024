import sys
from itertools import product, combinations
from collections import defaultdict


# Silver
def get_dependency(a, op, b):
    if op == 'AND':
        return (a, lambda x, y: x & y, b)
    elif op == 'OR':
        return (a, lambda x, y: x | y, b)
    elif op == 'XOR':
        return (a, lambda x, y: x ^ y, b)


def valid_depenencies(o, d, s):
    if o in s:
        return False
    if o not in d:
        return True
    s.add(o)
    a, _, b = d[o]
    return valid_dependencies(a, d, s) and valid_dependencies(b, d, s)


def calculate(o, v, d):
    if o in v:
        return v[o]

    a, f, b = d[o]
    a = calculate(a, v, d)
    b = calculate(b, v, d)
    v[o] = f(a, b)

    return v[o]


def get_z(v, d, zs):
    ret = 0
    for z in zs:
        ret <<= 1
        ret += calculate(z, v, d)
    return ret


zs = set()
vals = defaultdict(int)
dependencies = {}
with open(sys.argv[1]) as in_f:
    for line in [x.strip() for x in in_f]:
        if not line:
            continue
        if len(line) < 8:
            toks = line.split(':')
            vals[toks[0]] = int(toks[1])
            if toks[0][0] == 'z':
                zs.add(toks[0])
        else:
            toks = line.split()
            dependencies[toks[-1]] = get_dependency(toks[0], toks[1], toks[2])
            if toks[-1][0] == 'z':
                zs.add(toks[-1])

zs = sorted(list(zs), reverse=True)
print(get_z(vals, dependencies, zs))
# Pen and paper
print('cqr,ncd,nfj,qnw,vkg,z15,z20,z37')
