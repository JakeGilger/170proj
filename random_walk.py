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

random_walk(310)

def compute_score(teams):
	total = 0
	for i in teams:
		total += len(i) * sum(i)
	return total

def find_best(input_number):
	best = 0
	for i in range(10):
		teams = random_walk(input_number)
		score = compute_score(teams)
		if score > best:
			best = score
			bestTeams = teams
	print (bestTeams, best)

find_best(310)
