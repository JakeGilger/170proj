import cPickle

def combine_outputs(output1, output2):
	with open(output1, "r") as f:
		f1lines = f.readlines()
	with open(output2, "r") as f:
		f2lines = f.readlines()
	with open("combined_output.out", "w") as f:
		for i in range(len(f1lines)):
			score1 = score_from_file(i, f1lines)
			score2 = score_from_file(i, f2lines)
			if score1 > score2:
				f.write(f1lines[i])
			else:
				f.write(f2lines[i])

def score_from_file(line_number, file_lines):
	perf = load_obj(str(line_number) + ".perf")
	line = file_lines[line_number - 1]
	orig_line = line
	line = line.split(";")
	num_teams = len(line)
	total = 0
	for i in line:
		team = i.strip()
		team = team.split(" ")
		teamSum = 0
		for j in team:
			teamSum += perf[j]
		total += len(team) * teamSum
	return (total, orig_line + "\n", num_teams)

def load_obj(name):
	with open('obj/' + name, 'rb') as f:
		return cPickle.load(f)