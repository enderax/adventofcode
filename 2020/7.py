from collections import deque

E = {}

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
				if bag not in E:
					E[bag] = []
				E[bag].append(container)
				idx += 4

a = set()
init = E[target]

for i in E[target]:
	if i in a:
		continue
	a.add(i)
	for k in E.get(i, []):
		init.append(k)
print(len(a))


# SEEN = set() #unique set of containers
# Q = deque([target])
# while Q:
# 	x = Q.popleft() #take one by one from left
# 	if x in SEEN:
# 		continue
# 	SEEN.add(x)
# 	for y in E.get(x, []):
# 		Q.append(y)

# print(len(SEEN)-1)
