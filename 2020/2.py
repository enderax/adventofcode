import re

#https://adventofcode.com/2020/day/2
with open("2.txt") as file:
	lines = file.read().splitlines()

#Check number of occurrance in the password
def numOfChar(char, password) -> int:
	c = 0
	for i in password:
		if char == i:
			c +=1
	return c

#Check password is valid
def checkValidity(mini, maxi, count):
	if count >= mini and count <= maxi:
		return True

valid = 0

for i in lines:
	#Convert '5-7 s: wstqqsbcss' to ['5','7','s','wstqqsbcss']
	i = re.split('-|: |\s|\n',i)
	count = numOfChar(i[2],i[3])
	if checkValidity(int(i[0]),int(i[1]),int(count)):
		valid +=1

print(valid)