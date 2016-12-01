def read_in_files():
	for i in range(1, 2):
		with open("cs170_final_inputs/" + str(i) + ".in") as f:
			compute_horse_teams(f.read())

def compute_horse_teams(input_file):
	print input_file[:10]
	lines = input_file.split("\n")