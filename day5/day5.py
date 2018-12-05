from pathlib import Path


ROOT = Path(__file__).parents[0].resolve()

with open(str(ROOT / 'day5_input.txt'), 'r') as fin:
        data = fin.read().strip()


def pred(now, next_):
    return now.lower() == next_.lower() and now.islower() != next_.islower()


def puzzle1(data):
        buff = []
        for char in data:
            if buff and pred(char, buff[-1]):
                buff.pop()
            else:
                buff.append(char)
        return len(buff)


def puzzle2():
    uniqs = set([char.lower() for char in data])
    return min([puzzle1(data.replace(char, '').replace(char.upper(), '')) for char in uniqs])


if __name__ == '__main__':
    print(puzzle1(data))
    print(puzzle2())