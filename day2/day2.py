from pathlib import Path
from collections import Counter

ROOT = Path(__file__).parents[0].resolve()


def puzzle1():
    two = 0
    three = 0
    with open(str(ROOT / 'day2_input.txt'), 'r') as fin:
        for line in fin:
            counts = Counter(line)
            if 2 in counts.values():
                two += 1
            if 3 in counts.values():
                three += 1
    print('The final check sum is {}'.format(two * three))


def puzzle2():
    lines = []
    seen = []
    with open(str(ROOT / 'day2_input.txt'), 'r') as fin:
        for line in fin:
            lines.append(line.strip())
        for row in lines:
            seen.append(row)
            to_check = [line for line in lines if line not in seen]
            zipped = zip([row] * len(to_check), to_check)
            for z in zipped:
                zip_vals = list(zip(*z))
                check = sum([0 if i[0] == i[1] else 1 for i in zip_vals])
                if check == 1:
                    print(''.join([i[0] for i in zip_vals if i[0] == i[1]]))
                    return


if __name__ == '__main__':
    puzzle1()
    puzzle2()