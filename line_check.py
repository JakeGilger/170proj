import cPickle
import sys

if len(sys.argv) != 2:
	print "Usage Example: python line_check.py exampoutput.out"
	exit()


OUTPUT_FILE_TO_CHECK = sys.argv[1]


def load_obj(name):
	with open('obj/' + name, 'rb') as f:
		return cPickle.load(f)

with open(OUTPUT_FILE_TO_CHECK) as f:
	flines = f.readlines()

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

for i in range(1, 601):
	print("Line: " + str(i))
	line = flines[i - 1]
	check_line(i, line)