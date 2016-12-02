import cPickle
import random


NUM_ITERATIONS = 15
VERBOSE = True

with open("output.out", "r") as f:
	flines = f.read().split("\n")

def load_obj(name):
	with open('obj/' + name, 'rb') as f:
		return cPickle.load(f)

def random_walk(input_number):
	adj = load_obj(str(input_number) + ".adj")
	perf = load_obj(str(input_number) + ".perf")
	size = len(adj)
	unmarked = range(0, size)
	start = random.choice(unmarked)
	current = start
	unmarked.remove(current)
	team = [current]
	allTeams = []
	while not len(unmarked) == 0:
		outgoing = adj[current]
		toConsider = []
		for vertex in outgoing:
			if vertex in unmarked:
				toConsider.append(vertex)
		if len(toConsider) == 0:
			allTeams.append(team)
			current = random.choice(unmarked)
			unmarked.remove(current)
			team = [current]
			continue
		next = random.choice(toConsider)
		unmarked.remove(next)
		team.append(next)
		current = next
	allTeams.append(team)
	return allTeams

def compute_score(teams):
	total = 0
	for i in teams:
		total += len(i) * sum(i)
	return total

def find_best(input_number):
	best = 0
	perf = load_obj(str(input_number) + ".perf")
	for i in range(NUM_ITERATIONS):
		teams = random_walk(input_number)
		teamsPerf = []
		for team in teams:
			teamPerf = []
			for i in team:
				teamPerf.append(perf[i])
			teamsPerf.append(teamPerf)
		score = compute_score(teamsPerf)
		if score >= best:
			best = score
			bestTeams = teams
	return (bestTeams, best, len(bestTeams))

def convert_to_out(teams):
	out = ""
	for i in teams:
		for j in i:
			out += str(j) + " "
		out = out.rstrip()
		out += "; "
	out = out[:len(out) - 2]
	out += "\n"
	return out

def score_from_file(line_number):
	perf = load_obj(str(line_number) + ".perf")
	line = flines[line_number - 1]
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

def write_output(where_to_write):

	with open(where_to_write, "w") as f:
		for i in range(1, 601):
			prevbest = score_from_file(i)
			if prevbest[2] == 1:
				if VERBOSE:
					print(str(i) + " is solved with 1 team.")
				f.write(prevbest[1])
				continue
			newbest_tup = find_best(i)
			if newbest_tup[1] >= prevbest[0]:
				if VERBOSE:
					print(str(i) + ": found better solution: " + str(newbest_tup[1]) + " over: " + str(prevbest[0]) + ". Teams: " + str(newbest_tup[2]))
				f.write(convert_to_out(newbest_tup[0]))
			else:
				if VERBOSE:
					print(str(i) + ": no better found over: " + str(prevbest[0]))
				f.write(prevbest[1])

write_output("jakeoutput.out")