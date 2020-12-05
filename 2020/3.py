#https://adventofcode.com/2020/day/3

r = 0 #row
c = 0 #column
tree = 0

G = []
# Tree -> # Space -> .
with open("3.txt") as file:
	lines = file.read().splitlines()
	for line in lines:
		G.append(list(line))

while r + 1 < len(G):
	c += 3
	r += 1
	if G[r][c % len(G[r])] == '#': # Column pattern is repeated as necessary till get the bottomline
		#print('Tree')
		tree += 1
print(tree)



