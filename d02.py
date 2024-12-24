import sys


def safe(s):
    descending = s[0] - s[1] > 0

    for i in range(len(s) - 1):
        s0 = s[i]
        s1 = s[i + 1]

        if s0 == s1 or abs(s0 - s1) > 3:
            return 0, i

        if descending and s1 > s0:
            return 0, i
        if not descending and s1 < s0:
            return 0, i

    return 1, None


def safe_gold(s):
    success, idx = safe(s)

    if not success:
        tries = [s[1:], s[:idx + 1] + s[idx + 2:]]
        if not idx == 0:
            tries.append(s[:idx] + s[idx + 1:])

        for t in tries:
            new_s, _ = safe(t)

            if new_s:
                return 1
        return 0

    return 1


silver = 0
gold = 0
with open(sys.argv[1]) as in_f:
    for line in in_f:
        toks = [int(x) for x in line.split()]
        silver += safe(toks)[0]
        gold += safe_gold(toks)

print(silver)
print(gold)
