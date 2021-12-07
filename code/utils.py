def parse(day, fun):
	with open("../inputs/" + day + ".txt") as f:
		return list(map(fun, f.readlines()))


def parse_line(day, fun):
	with open("../inputs/" + day + ".txt") as f:
		return fun(f.readline())


def parse_line_csv(day):
	with open("../inputs/" + day + ".txt") as f:
		return list(map(int, f.readline().strip().split(",")))
