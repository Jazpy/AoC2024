import sys
from collections import defaultdict
from functools import cmp_to_key


ruleset = defaultdict(set)
def sort_key(x, y):
    if y in ruleset[x]:
        return -1
    elif x in ruleset[y]:
        return 1
    return 0

rules = []
updates = []

l = rules
with open(sys.argv[1]) as in_f:
    for line in in_f:
        line = line.strip()
        if line == '':
            l = updates
            continue
        l.append(line)

for r in rules:
    x, y = tuple([int(x) for x in r.split('|')])
    ruleset[x].add(y)

silver = 0
gold = 0
for u in updates:
    ps = [int(x) for x in u.split(',')]
    valid = True
    for i in range(len(ps) - 1):
        for j in range(i + 1, len(ps)):
            if ps[j] not in ruleset[ps[i]]:
                valid = False
                break
        if not valid:
            break
    if valid:
        silver += ps[len(ps) // 2]
    else:
        s = sorted(ps, key=cmp_to_key(sort_key))
        gold += s[len(s) // 2]

print(silver)
print(gold)
