import operator
from pathlib import Path
from collections import defaultdict


ROOT = Path(__file__).parents[0].resolve()


def mdist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def puzzle1():
    with open(str(ROOT / 'day6_input.txt'), 'r') as fin:
        coordinates = []
        for line in fin:
            coordinates.append(tuple(map(int, line.strip().split(','))))
    grid = defaultdict(int)
    max_x = max(map(lambda c: c[0], coordinates))
    max_y = max(map(lambda c: c[1], coordinates))
    for x in range(max_x):
        for y in range(max_y):
            dists = sorted([(c, mdist(c, (x, y))) for c in coordinates], key=operator.itemgetter(1))
            if x in (0, max_x) or y in (0, max_y):
                grid[dists[0][0]] = -1
            elif dists[0][1] < dists[1][1]:
                if grid.get(dists[0][0]) == -1:
                    continue
                else:
                    grid[dists[0][0]] += 1
            else:
                continue

    print('The answer to puzzle 1 is {}'.format(max(grid.values())))


def puzzle2():
    with open(str(ROOT / 'day6_input.txt'), 'r') as fin:
        coordinates = []
        for line in fin:
            coordinates.append(tuple(map(int, line.strip().split(','))))

    region = 0
    max_x = max(map(lambda c: c[0], coordinates))
    max_y = max(map(lambda c: c[1], coordinates))
    for x in range(max_x):
        for y in range(max_y):
            region += int(sum(mdist(c, (x, y)) for c in coordinates) < 10000)

    print('The answer to puzzle 2 is {}'.format(region))
