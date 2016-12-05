import cPickle
import sys

if len(sys.argv) < 2:
	print "Usage Example: python line_check.py exampoutput.out"
	exit()


OUTPUT_FILE_TO_CHECK = sys.argv[1]
with open(OUTPUT_FILE_TO_CHECK) as f:
	flines = f.readlines()

def load_obj(name):
	with open('obj/' + name, 'rb') as f:
		return cPickle.load(f)

def score_from_line(line_number, line):
	perf = load_obj(str(line_number) + ".perf")
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
	return (total, num_teams)

def check_line(problem_number, output_line):
	adj = load_obj(str(problem_number) + ".adj")
	teamed_line = output_line.split(";")
	teams = []
	for t in teamed_line:
		team = t.strip()
		team = team.split(" ")
		teams.append(team)
	for team_num in range(len(teams)):
		curr_team = teams[team_num]
		for horse_posit in range(len(teams[team_num]) - 1):
			if int(curr_team[horse_posit + 1]) not in adj[int(curr_team[horse_posit])]:
				print("Horse at position: " + str(horse_posit + 1) + " in team: " + str(team_num + 1) + " has no edge to: " + str(curr_team[horse_posit + 1]))
	score = score_from_line(problem_number, output_line)
	if score[1] == 1:
		print("Line: " + str(problem_number) + " solved.")
	else:
		print("Line: " + str(problem_number) + " " + str(score))

for i in range(1, 601):
	line = flines[i - 1]
	check_line(i, line)
