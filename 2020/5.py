'''
For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.

'''
#https://adventofcode.com/2020/day/5

with open("5.txt") as file:
	lines = file.read().splitlines()

#PART1
l_sid = [] #sid list 

for line in lines:
	r:int = 127 #row
	c:int = 7 #column
	pr = 6  #power of 2 for row 
	pc = 2 	#power of 2 for column 
	sid = 1 #seat id
	#Deduct half of seats and reduce power if F, otherwise reduce only power
	while ( pr > 0 and pc > 0 ):
		for l in line:
			if l == 'F':
				r = r - (2 ** pr)
				pr -= 1
			elif l == 'B':
				pr -=  1
			elif l == 'L':
				c = c - (2 ** pc)
				pc -= 1
			elif l == 'R':
				pc -= 1
			else:
				pass
		sid = 8 * r + c
		l_sid.append(sid)
		#print(r,c,sid)
print(max(l_sid))

#PART 2 - find the missing seat ID
l_sid.sort()
missing = sum(range(l_sid[0],l_sid[-1]+1)) - sum(l_sid)
print(missing)
