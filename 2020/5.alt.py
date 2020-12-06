#https://adventofcode.com/2020/day/5
#Alternative solution for Day 5 part 1

with open("5.txt") as file:
	lines = file.read().splitlines()

#PART1
def bin2dec(n):
	return int(n,2) 

for line in lines:
	#Replace letters with 1 and 0. Get decimal value of binaries for row and column
	line = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
	row = bin2dec(line[:7])
	col = bin2dec(line[-3:])
	print(row,col)