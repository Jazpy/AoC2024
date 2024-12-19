import sys
from collections import defaultdict
from functools import cache


@cache
def possibilities(pattern):
    global tgrams
    if not pattern:
        return 1

    ret = 0
    for t in set(tgrams[pattern[:2]] + tgrams[pattern[:1]]):
        if len(pattern) >= len(t) and pattern.startswith(t):
            ret += possibilities(pattern[len(t):])
    return ret


with open(sys.argv[1]) as in_f:
    lines = in_f.readlines()
patterns = [x.strip() for x in lines[2:]]

tgrams = defaultdict(list)
for towel in [x.strip() for x in lines[0].split(',')]:
    tgrams[towel[:2]].append(towel)

silver = 0
gold = 0
for pattern in patterns:
    p = possibilities(pattern)
    if p:
        silver += 1
    gold += p

print(silver)
print(gold)
