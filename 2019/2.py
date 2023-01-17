#https://adventofcode.com/2019/day/2
'''
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
'''

with open("2.txt") as file:
	lines = file.read().split(',')

def one(a,b):
	return int(a) + int(b)

def two(a,b):
	return int(a) * int(b)

def ninenine():
	quit()
'''
for kullanınca patlıyor çünkü i'yi dinamik değiştirmemiz gerekiyor.
Mesela 1 veya 2 gelirse 4 atla şeklinde. 
'''
i = 0
while i < len(lines):
	if lines[i] == '1':
		#print('Opcode1')
		'''
		1 gelirse i+1'de belirtilen konumdaki değeri, i+2'de belirtilen konumdaki değerle topla.
		bir sonraki opcode için 4 git
		'''
		lines[int(lines[i+3])] = str(one(lines[int(lines[i+1])],lines[int(lines[i+2])]))
		i += 4

	if lines[i] == '2':
		#print('Opcode2')
		'''
		2 gelirse i+1'de belirtilen konumdaki değeri, i+2'de belirtilen konumdaki değerle çarp.
		bir sonraki opcode için 4 git
		'''
		lines[int(lines[i+3])] = str(two(lines[int(lines[i+1])],lines[int(lines[i+2])]))
		i += 4

	if lines[i] == '99':
		#print('Opcode99')
		ninenine()
print(lines)
