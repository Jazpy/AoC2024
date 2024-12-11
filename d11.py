import sys
import math
from functools import cache


@cache
def blink(stone, blinks):
    if blinks == 0:
        return 1

    if stone == 0:
        return blink(1, blinks - 1)
    elif (int(math.log10(stone)) + 1) % 2 == 0:
        str_ver = str(stone)
        x, y = int(str_ver[:len(str_ver) // 2]), int(str_ver[len(str_ver) // 2:])
        return blink(x, blinks - 1) + blink(y, blinks - 1)
    else:
        return blink(stone * 2024, blinks - 1)


input = [int(x) for x in open(sys.argv[1]).readlines()[0].split()]

print(sum([blink(x, 25) for x in input]))
print(sum([blink(x, 75) for x in input]))
