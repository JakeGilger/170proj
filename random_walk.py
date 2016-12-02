import cPickle
import random

def load_obj(name):
    with open('obj/' + name, 'rb') as f:
        return cPickle.load(f)

def random_walk(input_number):
	adj = load_obj(str(input_number) + ".adj")
	perf = load_obj(str(input_number) + ".perf")
	size = len(adj)
	unmarked = range(1, size + 1)
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
	for i in range(1000):
		teams = random_walk(input_number)
		score = compute_score(teams)
		if score > best:
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
#hello
def score_from_file(line_number):
	with open("output.out", "r") as f:
		lines = f.read().split("\n")
	line = lines[line_number - 1]
	line = line.split(";")
	total = 0
	for i in line:
		team = i.strip()
		team = team.split(" ")
		teamSum = 0
		for j in team:
			teamSum += int(j)
		total += len(team) * teamSum
	return total

def write_output():
	with open("output.out", "w") as f:
		for i in range(1, 10):
			f.write(convert_to_out(find_best(i)[0]))

print find_best(4)