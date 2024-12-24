import re
import sys


silver = 0
with open(sys.argv[1]) as in_f:
    for line in in_f:
        matches = [x.group() for x in re.finditer('mul\((\d+),(\d+)\)', line)]
        for m in matches:
            toks = m.split(',')
            x, y = int(toks[0][4:]), int(toks[1][:-1])
            silver += x * y

print(silver)

gold = 0
with open(sys.argv[1]) as in_f:
    mul_switch = True
    for line in in_f:
        matches = [x.group() for x in re.finditer('mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', line)]
        for m in matches:
            if m == 'do()':
                mul_switch = True
                continue
            elif m == 'don\'t()':
                mul_switch = False
                continue

            if mul_switch:
                toks = m.split(',')
                x, y = int(toks[0][4:]), int(toks[1][:-1])
                gold += x * y
print(gold)
