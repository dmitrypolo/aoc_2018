from pathlib import Path


ROOT = Path(__file__).parents[0].resolve()
BOARD = [list('.' * 1000) for _ in range(1000)]


def puzzle1():
    with open(str(ROOT / 'day3_input.txt'), 'r') as fin:
        for line in fin:
            pieces = line.split()
            id_ = pieces[0]
            lpad, tpad = map(int, pieces[2].replace(':', '').split(','))
            x, y = map(int, pieces[3].split('x'))
            col = range(lpad, lpad + x)
            row = range(tpad, tpad + y)
            for c in col:
                for r in row:
                    if BOARD[c][r] == '.':
                        BOARD[c][r] = id_
                    else:
                        BOARD[c][r] = 'x'
    total = 0
    for row in BOARD:
        total += row.count('x')
    print('The total number of overlap is {}'.format(total))


def puzzle2():
    d = {}
    with open(str(ROOT / 'day3_input.txt'), 'r') as fin:
        for line in fin:
            pieces = line.split()
            id_ = pieces[0]
            x, y = map(int, pieces[-1].split('x'))
            d[id_] = x * y
    keys = d.keys()
    for key in keys:
        total = 0
        for row in BOARD:
            total += row.count(key)
            if total == d.get(key):
                print('The only id without overlap is {}'.format(key))
                return


if __name__ == '__main__':
    puzzle1()
    puzzle2()