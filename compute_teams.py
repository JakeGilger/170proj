def read_in_files():
	for i in range(1, 2):
		with open("cs170_final_inputs/" + str(i) + ".in") as f:
			compute_horse_teams(f.read())

def compute_horse_teams(input_file):
	lines = input_file.split("\n")
	size = lines[0]
	adjacency = {}
	performance = {}
	for i in range(1, size + 1):
		line = lines[i].split(" ")
		performance[i] = line[i - 1]
		adjacents = []
		for j in range(1, size + 1):
			if line[j - 1] == "1" and not j == i:
				adjacents.append(j)
		adjacency[i] = adjacents
