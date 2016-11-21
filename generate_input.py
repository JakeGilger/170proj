import random

#Put the reciprocal of the odds into odds (i.e. 1/10: odds = 10)
odds = 10
all_zeroes = 0
vertex_count = 256
file_number = 3

#Set the following value to true if you wish to force a Hamiltonian Path in the graph.
force_hamiltonian_path = True
num_paths = 6

sample_list = [0] * (odds - 1)
sample_list.append(all_zeroes)

def writeline():
	line = []
	for i in range(vertex_count):
		line.append(random.choice(sample_list))
	return line

matrix = []
for j in range(vertex_count):
	matrix.append(writeline())

if (force_hamiltonian_path):
	for a in range(num_paths):
		path = range(0, vertex_count)
		random.shuffle(path)
		print("The path through this graph is: " + str(path))
		for i in range(0, vertex_count - 1):
			matrix[path[i]][path[i+1]] = 1
		

matrix_string = ""
for i in range(vertex_count):
	line = ""
	for j in range(vertex_count):
		if i == j:
			line += str(random.randint(1, 99)) + " "
		else:
			line += str(matrix[i][j]) + " "
	line.rstrip()
	line += "\n"
	matrix_string += line
with open(str(file_number) + ".in", "w") as f:
	f.write(str(vertex_count) + "\n" + matrix_string)