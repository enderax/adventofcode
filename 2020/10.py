from os.path import dirname, join
from itertools import combinations  

current_dir = dirname(__file__)
file_path = join(current_dir, "./10.txt")

with open(file_path) as file:
	joltage = [int(x) for x in file.read().split()]

joltage.sort()
print(joltage)

def average(n,m):
    if m - n == 3:
        return 3
    if m - n == 2:
        return 2
    if m - n == 1:
        return 1

count = []

for i in range(len(joltage)-1):
    count.append(average(joltage[i],joltage[i+1]))

print(count.count(1)+1) #+1 for effective rating of 0 
print(count.count(2))
print(count.count(3)+1) #+1 bc your device's built-in adapter is always 3 higher than the highest adapter

print((count.count(3)+1) * (count.count(1)+1))
    
