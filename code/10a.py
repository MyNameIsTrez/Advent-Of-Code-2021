import utils


def main():
	data = utils.parse("10", parse)

	pairs = {
		"(": ")",
		"[": "]",
		"{": "}",
		"<": ">"
	}

	points = {
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137
	}

	score = 0

	for line in data:
		stack = []

		for char in line:
			if char in pairs:
				stack.append(char)
			else:
				if char != pairs[stack.pop()]:
					score += points[char]
					break

	print(score)


def parse(line):
	return list(line[:-1])


if __name__ == "__main__":
	main()