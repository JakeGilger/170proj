import cPickle
import sys

if len(sys.argv) != 3:
	print "Usage Example: python combine.py output1.out output2.out"
	exit()

OUTPUT1 = sys.argv[1]
OUTPUT2 = sys.argv[2]

def combine_outputs(output1, output2):
	with open(output1, "r") as f:
		f1lines = f.readlines()
	with open(output2, "r") as f:
		f2lines = f.readlines()
	score1sum = 0
	score2sum = 0
	neithersum = 0
	with open("combined_output.out", "w") as f:
		for i in range(1, len(f1lines) + 1):
			score1 = score_from_file(i, f1lines)
			score2 = score_from_file(i, f2lines)
			if score1[0] > score2[0]:
				score1sum += 1
				f.write(f1lines[i - 1])
			else:
				if score1[0] == score2[0]:
					neithersum += 1
				else:
					score2sum += 1
				f.write(f2lines[i - 1])
	print(str(score1sum) + ", " + str(score2sum) + ", with " + str(neithersum) + " equal.")

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
			teamSum += perf[int(j)]
		total += len(team) * teamSum
	return (total, orig_line + "\n", num_teams)

def load_obj(name):
	with open('obj/' + name, 'rb') as f:
		return cPickle.load(f)

combine_outputs(OUTPUT1, OUTPUT2)

