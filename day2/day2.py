from pathlib import Path
from operator import mul
from collections import Counter
from itertools import zip_longest

ROOT = Path(__file__).parents[0].resolve()

def puzzle1():
	check_sum = {2: 0, 3: 0}
	with open(str(ROOT / 'day2_input.txt'), 'r') as fin:
		for line in fin:
			l = line.strip()
			counts = Counter(l)
			if 2 in counts.values():
				check_sum[2] += 1
			if 3 in counts.values():
				check_sum[3] += 1
	print('The final check sum is {}'.format(mul(*check_sum.values())))

def puzzle2():
	lines = []
	seen = []
	with open(str(ROOT / 'day2_input.txt'), 'r') as fin:
		for line in fin:
			lines.append(line.strip())
		for row in lines:
			seen.append(line)
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