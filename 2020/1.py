#https://adventofcode.com/2020/day/1#part1
with open("1.txt") as file:
	lines = file.read().splitlines()

def part1():
	for i in range(0,len(lines)):
		for j in range(1,len(lines)):
			if (int(lines[i]) + int(lines[j])) == 2020:
				print(lines[i],lines[j])
				print(int(lines[i]) * int(lines[j]))
				quit()
			else:
				continue

#https://adventofcode.com/2020/day/1#part2
def part2():
	for i in range(0,len(lines)):
		for j in range(1,len(lines)):
			for k in range(1,len(lines)):
				if (int(lines[i]) + int(lines[j]) + int(lines[k])) == 2020:
					print(lines[i],lines[j],lines[k])
					print(int(lines[i]) * int(lines[j]) * int(lines[k]))
					quit()
				else:
					continue

part1()
part2()