from pathlib import Path
from itertools import cycle

ROOT = Path(__file__).parents[0].resolve()

def puzzle1():
	frequency = 0
	with open(str(ROOT / 'day1_input.txt'), 'r') as fin:
		for line in fin:
			l = line.strip()
			frequency += int(l)
	print('The final frequency is {}'.format(frequency))

def puzzle2():
	frequency = 0
	seen = set([0])
	with open(str(ROOT / 'day1_input.txt'), 'r') as fin:
		for line in cycle(fin):
			l = line.strip()
			frequency += int(l)
			if frequency in seen:
				print('The first repeated frequency is {}'.format(frequency))
				break
			else:
				seen.add(frequency)
			


if __name__ == '__main__':
	puzzle1()
	puzzle2()