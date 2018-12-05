import re
import operator
from pathlib import Path
from itertools import chain

ROOT = Path(__file__).parents[0].resolve()
ex = r'\d{2}-\d{2}-\d{2} \d{2}:\d{2}'


def puzzle1():
	lines = []
	d = {}
	with open(str(ROOT / 'day4_input.txt'), 'r') as fin:
		for line in fin:
			ts = re.search(ex, line).group(0)
			l = line.strip('\n').split()
			lines.append([ts, *l[2:]])
	slines = sorted(lines, key=operator.itemgetter(0))
	guard = None
	for line in slines:
		if "Guard" in line:
			guard = line[2]
			if not d.get(guard):
				d[guard] = []
		else:
			d[guard].append(int(line[0].split()[-1].split(':')[-1]))
	sleepy_guard = [0, 0, 0]
	for key in d.keys():
		chunks = [d.get(key)[i: i + 2] for i in range(0, len(d.get(key)), 2)]
		minutes_asleep = list(chain.from_iterable(list(range(*i)) for i in chunks))
		if len(minutes_asleep) > sleepy_guard[1]:
			sleepy_guard = [int(key.replace('#', '')), len(minutes_asleep), 
				max(minutes_asleep, key=minutes_asleep.count)]

	print('The answer is {}'.format(sleepy_guard[0] * sleepy_guard[-1]))


if __name__ == '__main__':
	puzzle1()
