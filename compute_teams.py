import cPickle

def read_in_files():
	for i in range(1, 601):
		print(str(i))
		with open("cs170_final_inputs/" + str(i) + ".in") as f:
			dicts = compute_dict(f.read())
			save_obj(dicts[0], str(i) + ".adj")
			save_obj(dicts[1], str(i) + ".perf")
			save_obj(dicts[2], str(i) + ".prev")

def compute_dict(input_file):
	lines = input_file.split("\n")
	size = int(lines[0])
	del lines[0]
	sizerange = range(0, size)
	adjacency = {}
	performance = {}
	prev = {}
	for i in sizerange:
		line = lines[i].split(" ")
		performance[i] = int(line[i])
		adjacents = []
		for j in sizerange:
			if line[j] == "1" and not j == i:
				adjacents.append(j)
		adjacency[i] = adjacents

	for i in sizerange:
		lines[i] = lines[i].split(" ")
		prev[i] = []
	
	for key in adjacency.keys():
		for item in adjacency[key]:
			if item in prev:
				prev[item].append(key)
			else:
				prev[item] = [key]

	return (adjacency, performance, prev)

def save_obj(obj, name):
    with open('obj/'+ name, 'wb') as f:
        cPickle.dump(obj, f, cPickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name, 'rb') as f:
        return cPickle.load(f)

read_in_files()