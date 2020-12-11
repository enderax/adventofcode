from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./8.txt")

with open(file_path) as file:
	lines = file.read().splitlines()
	opcode = [line.split() for line in lines]
	#print(opcode)
	accu = 0 #accumulator
	order = 0 #order of opcode
	i = 0 
	loop = [] # a list of runned opcodes.
	while i < len(opcode):
		if i in loop: # if code is runned before, print the latest accu
			print(accu)
			quit()
		elif i not in loop:
			loop.append(i)
		if opcode[i][0] == 'acc':
			order += 1
			accu += int(opcode[i][1])
			print(f'Order#{order}:{opcode[i]}')
			print(f'Accu:{accu}')
			i += 1
		elif opcode[i][0] == 'jmp':
			order += 1
			print(f'Order#{order}:{opcode[i]}')
			i += int(opcode[i][1])
		elif opcode[i][0] == 'nop':
			order += 1
			print(f'Order#{order}:{opcode[i]}')
			i += 1
			continue

