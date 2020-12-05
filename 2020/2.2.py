import re

#https://adventofcode.com/2020/day/2
'''
1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
'''

with open("2.txt") as file:
	lines = file.read().splitlines()

valid = 0

for i in lines:
	#Convert '5-7 s: wstqqsbcss' to ['5','7','s','wstqqsbcss']
	i = re.split('-|: |\s|\n',i)

	pos1 = int(i[0])
	pos2 = int(i[1])
	char = i[2]
	pwd = i[3]

	#!= means XOR here. only one True is valid. otherwise invalid
	if (pwd[pos1-1] == char) != (pwd[pos2-1] == char): #minus -1 because no concept of "index zero"
		valid +=1 

print(valid)