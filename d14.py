import sys
from utils import Vec2


robots = []
with open(sys.argv[1]) as in_f:
    for line in in_f:
        toks = line.split()
        t0 = [int(x) for x in toks[0].split('=')[1].split(',')]
        t1 = [int(x) for x in toks[1].split('=')[1].split(',')]
        robots.append([Vec2(t0[0], t0[1]), Vec2(t1[0], t1[1])])

qs = [0, 0, 0, 0]
middle_x, middle_y = 50, 51
for t in range(1, 10000):
    uniques = set()
    for robot in robots:
        robot[0] += robot[1]
        robot[0] %= Vec2(101, 103)
        uniques.add(robot[0])

        if t == 100:
            if robot[0].x < middle_x and robot[0].y < middle_y:
                qs[0] += 1
            if robot[0].x > middle_x and robot[0].y < middle_y:
                qs[1] += 1
            if robot[0].x < middle_x and robot[0].y > middle_y:
                qs[2] += 1
            if robot[0].x > middle_x and robot[0].y > middle_y:
                qs[3] += 1
    if len(uniques) == len(robots):
        print(t)
        break
    if t == 100:
        print(qs[0] * qs[1] * qs[2] * qs[3])
