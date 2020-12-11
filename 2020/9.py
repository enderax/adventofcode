from os.path import dirname, join
from itertools import permutations  
from itertools import combinations  


current_dir = dirname(__file__)
file_path = join(current_dir, "./9.txt")

with open(file_path) as file:
	num = [int(x) for x in file.read().split()]

def findPairs(lst, K): 
    return [pair for pair in combinations(lst, 2) if sum(pair) == int(K)] 

for i in range(25,len(num)):
    if not findPairs(num[i-25:i],int(num[i])):
        print(num[i])
        