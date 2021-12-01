def parse(day, fun):
	with open("../inputs/" + day + ".txt") as f:
		return list(map(fun, f.readlines()))
