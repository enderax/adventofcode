#https://adventofcode.com/2020/day/4
'''
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
'''
import re

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

with open("4.txt") as file:
	lines = file.read().split('\n\n') #split pasaports by blankline(\n\n)

valid = 0

for line in lines:
	line = re.split('\s|\n',line)
	l = { re.split(':', k)[0]:re.split(':', k)[1] for k in line }

	if set(fields).issubset(l):	#First field validation 
		#print(l)
		#Data validations
		if not (1920 <= int(l['byr']) <= 2002):
			continue
		elif not (2010 <= int(l['iyr']) <= 2020):
			continue
		elif not (2020 <= int(l['eyr']) <= 2030):
			continue
		#165cm , 72in
		elif not ((str(l['hgt']).endswith('cm') and 150 <= int(re.findall('\d+',l['hgt'])[0]) <= 193) or (str(l['hgt']).endswith('in') and 59 <= int(re.findall('\d+',l['hgt'])[0]) <= 76)):
			continue
		elif not (re.search('#[0-9a-f]{6}',l['hcl'])):
			continue
		elif not l['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			continue
		elif not (re.findall('^[0-9]{9}$',l['pid'])):
			print(l['pid'])
			continue
		else:
			valid += 1

print(valid)



