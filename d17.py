import sys


def apply_op(inp, op, operand, output):
    global A
    global B
    global C
    combo_dic = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}

    if op == 0:
        A = A // 2 ** combo_dic[operand]
    elif op == 1:
        B = B ^ operand
    elif op == 2:
        B = combo_dic[operand] % 8
    elif op == 3 and A != 0:
        return operand
    elif op == 4:
        B = B ^ C
    elif op == 5:
        output.append(combo_dic[operand] % 8)
    elif op == 6:
        B = A // 2 ** combo_dic[operand]
    elif op == 7:
        C = A // 2 ** combo_dic[operand]

    return inp + 2


def solve(digits, curr_solution, solutions):
    if not digits:
        solutions.add(curr_solution)
        return

    o = digits[-1]
    new_candidates = []
    curr_solution <<= 3
    for c in range(2 ** 3):
        new_candidates.append(curr_solution + c)

    for new_candidate in new_candidates:
        b = (new_candidate % 8) ^ 1
        c = new_candidate >> b
        b = ((b ^ c) ^ 4) % 8

        if b == o:
            solve(digits[:-1], new_candidate, solutions)


with open(sys.argv[1]) as in_f:
    lines = in_f.readlines()
    A = int(lines[0].split(':')[1])
    B = int(lines[1].split(':')[1])
    C = int(lines[2].split(':')[1])
    program = [int(x) for x in lines[4].split(':')[1].split(',')]

inp = 0
output = []
while inp < len(program):
    inp = apply_op(inp, program[inp], program[inp + 1], output)
print(','.join([str(x) for x in output]))

gold = set()
solve(program, 0, gold)
print(min(gold))
