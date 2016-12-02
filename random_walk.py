import cPickle
import random


NUM_ITERATIONS = 50
VERBOSE = True
FORCE_START_NODE = None

SINGLE_CASE = None

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
	if FORCE_START_NODE and size > FORCE_START_NODE:
		start = FORCE_START_NODE
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
		if len(bestTeams) == 1:
			break
	possibleBetter = find_better_path(input_number, bestTeams)
	if possibleBetter:
		print "found better path"
		teamsPerf = []
		for team in possibleBetter:
			teamPerf = []
			for i in team:
				teamPerf.append(perf[i])
			teamsPerf.append(teamPerf)
		best = compute_score(teamsPerf)
		bestTeams = possibleBetter
	return (bestTeams, best, len(bestTeams))

def find_better_path(input_number, teams):
	adj = load_obj(str(input_number) + ".adj")
	for i in range(len(teams)):
		firstTeam = teams[i]
		for j in range(i, len(teams)):
			if i == j:
				continue
			secondTeam = teams[j]
			if secondTeam[0] in adj[firstTeam[len(firstTeam) - 1]]:
				joined_team = firstTeam + secondTeam
				teams.pop(j)
				teams.pop(i)
				teams.append(joined_team)
				recurse = find_better_path(input_number, teams)
				if recurse:
					return recurse
				return teams
			if firstTeam[0] in adj[secondTeam[len(secondTeam) - 1]]:
				joined_team = secondTeam + firstTeam
				teams.pop(j)
				teams.pop(i)
				teams.append(joined_team)
				recurse = find_better_path(input_number, teams)
				if recurse:
					return recurse
				return teams
			for vertex in range(len(firstTeam) - 1):
				firstStart = firstTeam[vertex]
				firstEnd = firstTeam[vertex + 1]
				secondStart = secondTeam[0]
				secondEnd = secondTeam[-1]
				if secondStart in adj[firstStart] and firstEnd in adj[secondEnd]:
					joined_team = firstTeam[:vertex + 1] + secondTeam + firstTeam[vertex + 1:]
					teams.pop(j)
					teams.pop(i)
					teams.append(joined_team)
					recurse = find_better_path(input_number, teams)
					if recurse:
						return recurse
					return teams
	return False

			

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
		multi_team_cases = 0
		for i in range(1, 601):
			if not VERBOSE:
				print(str(i))
			prevbest = score_from_file(i)
			if SINGLE_CASE:
				if i != SINGLE_CASE:
					f.write(prevbest[1])
					continue
			if prevbest[2] == 1:
				if VERBOSE:
					print(str(i) + " is solved with 1 team.")
				f.write(prevbest[1])
				continue
			multi_team_cases += 1
			new_best_tup = find_best(i)
			if new_best_tup[1] >= prevbest[0]:
				if VERBOSE:
					print(str(i) + ": found better solution: " + str(new_best_tup[1]) + " over: " + str(prevbest[0]) + ". Teams: " + str(new_best_tup[2]))
				f.write(convert_to_out(new_best_tup[0]))
			else:
				if VERBOSE:
					print(str(i) + ": no better found over: " + str(prevbest[0]))
				f.write(prevbest[1])
	print("There were " + str(multi_team_cases) + " cases that were not previously solved with 1 team.")

write_output("jakeoutput.out")
