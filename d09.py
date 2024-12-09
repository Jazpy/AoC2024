import sys
from copy import deepcopy


with open(sys.argv[1]) as in_f:
    seq = [int(x) for x in in_f.readlines()[0].strip()]

frees = []
files = []

id_ctr = 0
seq_len = 0
compacted_len = 0
for i, block in enumerate(seq):
    if i % 2 == 0:
        files.append([id_ctr, seq_len, block])
        compacted_len += block
        id_ctr += 1
    else:
        frees.append([seq_len, block])

    seq_len += block


def silver_solve(files, frees):
    silver = 0
    file_ptr = 0
    free_ptr = 0
    curr_block = files[file_ptr]
    cons_block = files.pop()
    pos = 0
    while pos < seq_len:
        if pos >= compacted_len:
            break
        if len(curr_block) == 3:
            for i in range(curr_block[2]):
                silver += pos * curr_block[0]
                pos += 1

            file_ptr += 1
            curr_block.append(True)
            curr_block = frees[free_ptr]
        else:
            for i in range(curr_block[1]):
                if pos >= compacted_len:
                    break

                silver += pos * cons_block[0]
                pos += 1
                cons_block[2] -= 1

                if cons_block[2] == 0:
                    cons_block = files.pop()

            free_ptr += 1
            if file_ptr >= len(files):
                break
            curr_block = files[file_ptr]

    if cons_block[2] != 0 and len(cons_block) != 4:
        for i in range(cons_block[2]):
            silver += pos * cons_block[0]
            pos += 1

    print(silver)


def gold_solve(files, frees):
    gold = 0

    for file in reversed(files):
        placed = False
        for free in frees:
            if placed or free[0] > file[1]:
                break
            if free[1] >= file[2]:
                for pos in range(free[0], free[0] + file[2]):
                    gold += pos * file[0]
                free[0] += file[2]
                free[1] -= file[2]
                placed = True
        if not placed:
            for pos in range(file[1], file[1] + file[2]):
                gold += pos * file[0]

    print(gold)


silver_solve(deepcopy(files), deepcopy(frees))
gold_solve(files, frees)
