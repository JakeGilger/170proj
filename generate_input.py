import random

#Put the reciprocal of the odds into odds (i.e. 1/10: odds = 10)
odds = 10
vertex_count = 64
file_number = 2



sample_list = [0] * (odds - 1)
sample_list.append(1)

matrix = ""
for i in range(vertex_count):
	line = ""
	for j in range(vertex_count):
		if i == j:
			line += str(random.randint(1, 99)) + " "
		else:
			line += str(random.sample(sample_list, 1)[0]) + " "
	line.rstrip()
	line += "\n"
	matrix += line
with open(str(file_number) + ".in", "w") as f:
	f.write(str(vertex_count) + "\n" + matrix)