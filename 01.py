import sys
import bisect

from collections import Counter


l0, l1 = [], []
with open(sys.argv[1]) as in_f:
    for line in in_f:
        toks = line.split()
        x, y = int(toks[0]), int(toks[1])
        bisect.insort(l0, x)
        bisect.insort(l1, y)

silver = 0
for x, y in zip(l0, l1):
    silver += abs(x - y)

print(silver)

gold_ctr = Counter(l1)
gold = 0
for x in l0:
    gold += x * gold_ctr[x]

print(gold)
