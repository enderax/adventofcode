from os.path import dirname, join
from itertools import combinations  

current_dir = dirname(__file__)
file_path = join(current_dir, "./9.txt")

TARGET = 675280050

with open(file_path) as file:
	num = [int(x) for x in file.read().split()]

def findPairs(lst, K, N): 
    return [pair for pair in combinations(lst, N) if sum(pair) == int(K)] 

for i in range(21,len(num)):
    for j in range(0,20):
        findPairs(num[i-j:i],TARGET,j)
        if findPairs(num[i-j:i],TARGET,j):
            print(max(num[i-j:i]) + min(num[i-j:i]))
            break
        