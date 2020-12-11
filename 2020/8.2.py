from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./8.txt")

with open(file_path) as file:
	lines = file.read().splitlines()
	opcode = [line.split() for line in lines]

def part1(opcode):
	#print(opcode)
	accu = 0 #accumulator
	order = 0 #order of opcode
	i = 0 
	loop = [] # a list of runned opcodes.
	hasLoop = False
	while i < len(opcode):
		print(f'Order#{order}\t\t i:{i}\t {opcode[i]}\t Acc:{accu}')
		if i in loop: # if code is runned before, print the latest accu
			print(accu)
			hasLoop = True
			break
		elif i not in loop:
			loop.append(i)
		if opcode[i][0] == 'acc':
			order += 1
			accu += int(opcode[i][1])
			i += 1
		elif opcode[i][0] == 'jmp':
			order += 1
			i += int(opcode[i][1])
		elif opcode[i][0] == 'nop':
			order += 1
			i += 1
			continue
	return (accu, hasLoop)

swapDict = {'nop':'jmp','jmp':'nop'}
for i, (op,value) in enumerate(opcode):
  if op == 'nop' or op == 'jmp':
    swappedOp = [(swapDict[op], value)]
    newOpcode = opcode[:i] + swappedOp + opcode[i+1:]
    newAcc, hasLoop = part1(newOpcode)
    if not hasLoop:
      print(f'Part 2\n{newAcc}')

part1(opcode)





		

with open(file_path) as file:
	lines = file.read().splitlines()
	opcode = [line.split() for line in lines]
	#print(len(opcode))
	accu = 0 #accumulator
	order = 0 #order of opcode
	i = 0 
	loop = [] # a list of runned opcodes.
	changelist = []
	while i < len(opcode):
		print(f'Order#{order}\t\t i:{i}\t {opcode[i]}\t Acc:{accu}')
		if opcode[i][0] == 'acc':
			order += 1
			accu += int(opcode[i][1])
			i += 1
		elif opcode[i][0] == 'jmp':
			order += 1
			i += int(opcode[i][1])
		elif opcode[i][0] == 'nop':
			order += 1
			i += 1
			continue







		