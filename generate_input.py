import random

matrix = ""
for i in range(32):
	line = ""
	for j in range(32):
		if i == j:
			line += str(random.randint(1, 99)) + " "
		else:
			line += str(random.sample((0, 0, 1), 1)[0]) + " "
	line.rstrip()
	line += "\n"
	matrix += line
with open("evil.txt", "w") as f:
	f.write(matrix)