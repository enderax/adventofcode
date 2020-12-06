import re
with open("6.txt") as file:
	groups = file.read().split('\n\n') #split groups by blankline(\n\n)

#PART1
#get unique answers
def part1():
	sum = 0
	for person in groups:
		person = person.replace('\n','')
		sum += len(set(person))
	print(sum)


#PART2
#get common answers
'''
groups: ['ab\nac']
person: ['ab', 'ac']
combined: abac
i: ab
k: a
'''
def part2():
	sum = 0
	common = []
	
	for person in groups:
		person = re.split('\n|\s',person)
		num = len(person)
		combined = ''
		for i in person:
			combined += i
			for k in i:
				#print(groups,person,i,k)
				if combined.count(k) == num:
					common.append(k)
	print(len(common))

#part1()
part2()