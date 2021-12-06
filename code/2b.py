import utils


def parse(line):
	spl = line.split()
	return spl[0][0], int(spl[1])


def basic(data):
	aim = 0
	forward = 0
	depth = 0

	for pair in data:
		if pair[0] == "f":
			forward += pair[1]
			depth += aim * pair[1]
		else:
			aim += pair[1] if pair[0] == "d" else -pair[1]

	print(forward * depth)


if __name__ == "__main__":
	data = utils.parse("2", parse)

	print("basic")
	basic(data)
