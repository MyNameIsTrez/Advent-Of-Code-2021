import utils


def main():
	data = utils.parse("10", parse)

	score = 0

	for line in data:
		stack = []

		for char in line:
			if char in PAIRS:
				stack.append(char)
			else:
				if char != PAIRS[stack.pop()]:
					score += POINTS[char]
					break

	print(score)


def parse(line):
	return list(line[:-1])


if __name__ == "__main__":
	PAIRS = {
		"(": ")",
		"[": "]",
		"{": "}",
		"<": ">"
	}

	POINTS = {
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137
	}

	main()