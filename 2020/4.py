#https://adventofcode.com/2020/day/4
'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''
import re

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

with open("4.txt") as file:
	lines = file.read().split('\n\n') #split pasaports by blankline(\n\n)

valid = 0

for line in lines:
	'''
	Split fields by space and newline within passport. Converting them from
	cid:331
	ecl:blu eyr:2021 hcl:#733820 hgt:174cm
	iyr:2010 byr:1950 pid:405416908
	to ['cid:331', 'ecl:blu', 'eyr:2021', 'hcl:#733820', 'hgt:174cm', 'iyr:2010', 'byr:1950', 'pid:405416908']
	'''
	line = re.split('\s|\n',line)
	#l = { re.split(':', k)[0]:re.split(':', k)[1] for k in line } #splitting each field:value pairs by : then insert keys to a list
	l = [ re.split(':', k)[0] for k in line ]
	#print(set(fields))
	if set(fields).issubset(l):	
		valid += 1

print(valid)



