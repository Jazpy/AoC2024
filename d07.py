import sys
import functools


@functools.cache
def satisfied(test, ops, curr, gold=False):
    if curr > test:
        return False

    if not ops:
        return curr == test

    new_ops = ops[1:]
    p0 = satisfied(test, new_ops, curr + ops[0], gold)
    p1 = satisfied(test, new_ops, curr * ops[0], gold)
    p2 = satisfied(test, new_ops, int(str(curr) + str(ops[0])), gold) if gold else False

    return p0 or p1 or p2


eqs = []
with open(sys.argv[1]) as in_f:
    for line in in_f:
        toks = line.split(':')
        ops = tuple([int(x) for x in toks[1].split()])
        eqs.append((int(toks[0]), ops))

silver = 0
gold = 0
for test, ops in eqs:
    if satisfied(test, ops[1:], ops[0]):
        silver += test
    if satisfied(test, ops[1:], ops[0], gold=True):
        gold += test

print(silver)
print(gold)
