#https://adventofcode.com/2020/day/3#part2
'''
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
'''

G = []
# Tree -> # Space -> .
with open("3.txt") as file:
	lines = file.read().splitlines()
	for line in lines:
		G.append(list(line))

#Right 1, down 1.
def slope11():
	r = 0 #row
	c = 0 #column
	tree = 0

	while r + 1 < len(G):
		c += 1
		r += 1
		if G[r][c % len(G[r])] == '#': # Column pattern is repeted as necessary till get the bottomline
			#print('Tree')
			tree += 1
	return tree

#Right 3, down 1.
def slope31():
	r = 0 #row
	c = 0 #column
	tree = 0

	while r + 1 < len(G):
		c += 3
		r += 1
		if G[r][c % len(G[r])] == '#': # Column pattern is repeted as necessary till get the bottomline
			#print('Tree')
			tree += 1
	return tree

def slope51():
	r = 0 #row
	c = 0 #column
	tree = 0

	while r + 1 < len(G):
		c += 5
		r += 1
		if G[r][c % len(G[r])] == '#': # Column pattern is repeted as necessary till get the bottomline
			#print('Tree')
			tree += 1
	return tree

def slope71():
	r = 0 #row
	c = 0 #column
	tree = 0

	while r + 1 < len(G):
		c += 7
		r += 1
		if G[r][c % len(G[r])] == '#': # Column pattern is repeted as necessary till get the bottomline
			#print('Tree')
			tree += 1
	return tree

def slope12():
	r = 0 #row
	c = 0 #column
	tree = 0

	while r + 1 < len(G):
		c += 1
		r += 2
		#print(G[r][c % len(G[r])])
		#print(r,c,c % len(G[r]))
		if G[r][c % len(G[r])] == '#': # Column pattern is repeted as necessary till get the bottomline
			#print('Tree')
			tree += 1
	return tree

print(slope11() * slope31() * slope51() * slope71() * slope12())


