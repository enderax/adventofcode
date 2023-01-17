from os.path import dirname, join
from itertools import combinations  

current_dir = dirname(__file__)
file_path = join(current_dir, "./10.sample.txt")

with open(file_path) as file:
	joltage = [int(x) for x in file.read().split()]

sorted_joltage = sorted(joltage)
print(sorted_joltage)

comb3 = 1
comb2 = 1
i = 0

while i < len(sorted_joltage)-3:
    #print(i)
    if sorted_joltage[i+3] - sorted_joltage[i] == 3:
        print('Average is 3')
        comb3 *= 4
        i += 2
        continue
    if sorted_joltage[i+2] - sorted_joltage[i] == 2:
        print('Average is 2')
        comb2 *= 2
        i += 1
        continue
    else:
        i += 1
print(comb3 * comb2)
