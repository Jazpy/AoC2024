import sys
from collections import deque, defaultdict


def evolve(n):
    n ^= n * 64
    n %= 16777216
    n ^= n // 32
    n %= 16777216
    n ^= n * 2048
    return n % 16777216


nums = [int(x) for x in open(sys.argv[1])]

silver = 0
gold = defaultdict(int)
for n in nums:
    seen = set()
    curr_price = n % 10
    pattern = deque()
    for _ in range(2000):
        n = evolve(n)
        new_price = n % 10
        pattern.append(new_price - curr_price)
        curr_price = new_price

        if len(pattern) == 5:
            pattern.popleft()
        if len(pattern) == 4 and str(pattern) not in seen:
            gold[str(pattern)] += new_price
            seen.add(str(pattern))
    silver += n

print(silver)
print(max(gold.values()))
