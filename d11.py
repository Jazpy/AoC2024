import sys
import math
from functools import cache


@cache
def expand_stones(stone, blinks):
    if blinks == 0:
        return 1

    if stone == 0:
        return expand_stones(1, blinks - 1)
    elif (int(math.log10(stone)) + 1) % 2 == 0:
        str_ver = str(stone)
        x, y = int(str_ver[:len(str_ver) // 2]), int(str_ver[len(str_ver) // 2:])
        return expand_stones(x, blinks - 1) + expand_stones(y, blinks - 1)
    else:
        return expand_stones(stone * 2024, blinks - 1)


with open(sys.argv[1]) as in_f:
    input = [int(x) for x in in_f.readlines()[0].split()]

silver = sum([expand_stones(x, 25) for x in input])
gold = sum([expand_stones(x, 75) for x in input])

print(silver)
print(gold)
