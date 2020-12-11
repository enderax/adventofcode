from collections import deque, defaultdict

PARENTS = defaultdict(list)
CONTENTS = defaultdict(list)

target = 'shinygold'

with open("7.txt") as file:
	lines = file.read().splitlines()
	for line in lines:
		words = line.strip().split()
		container = words[0]+words[1]
		if words[-3] == 'no':
		 	continue
		else:
			idx = 4
			while idx < len(words):
				bag = words[idx+1]+words[idx+2]
				n = int(words[idx])
				
				PARENTS[bag].append(container)
				CONTENTS[container].append((n, bag))
				idx += 4

def sum(bag):
	a = 1
	for (n,y) in CONTENTS[bag]:
		a += n*sum(y)
	return a
print(sum(target)-1)

print(CONTENTS)
