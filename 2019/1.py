import math

#https://adventofcode.com/2019/day/1#part1
with open("1.txt") as file:
	lines = file.read().splitlines()

def part1():
	fuel = 0

	for mass in lines:
		fuel += math.floor(int(mass) / 3) - 2

	print(fuel)

##https://adventofcode.com/2019/day/1#part2
def getFuel(mass):
	return int(math.floor(round((mass / 3),2)) - 2)

def part2():
	fuelsum = 0

	for mass in lines:
		mass = int(mass)
		fuel = getFuel(mass)
		while ( getFuel(fuel) > 0 ):
			#print(type(fuel(mass)))
			fuelsum += fuel
			fuel = getFuel(fuel)
		fuelsum += fuel
	print(fuelsum)

#doğrulama 1969 kütle için 966 toplam fuel gerekir.
def part3(mass):
	fuelsum = 0
	fuel = getFuel(mass)
	while ( getFuel(fuel) > 0 ):
		fuelsum += fuel
		fuel = getFuel(fuel)
	fuelsum += fuel
	print(fuelsum)

part2()
#part3(1969)