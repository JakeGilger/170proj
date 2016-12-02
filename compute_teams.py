import cPickle

def read_in_files():
	for i in range(1, 601):
		print(str(i))
		with open("cs170_final_inputs/" + str(i) + ".in") as f:
			dicts = compute_dict(f.read())
			save_obj(dicts[0], str(i) + ".adj")
			save_obj(dicts[1], str(i) + ".perf")

def compute_dict(input_file):
	lines = input_file.split("\n")
	size = int(lines[0])
	adjacency = {}
	performance = {}
	for i in range(1, size + 1):
		line = lines[i].split(" ")
		performance[i] = int(line[i - 1])
		adjacents = []
		for j in range(1, size + 1):
			if line[j - 1] == "1" and not j == i:
				adjacents.append(j)
		adjacency[i] = adjacents
	return (adjacency, performance)

def save_obj(obj, name):
    with open('obj/'+ name, 'wb') as f:
        cPickle.dump(obj, f, cPickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name, 'rb') as f:
        return cPickle.load(f)

read_in_files()

adj = load_obj("13.perf")
print(adj)