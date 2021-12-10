import utils


def main():
	data = utils.parse("10", parse)

	incomplete = filter(is_incomplete, data)

	scores = []

	for line in incomplete:
		score = get_incomplete_line_score(line)
		scores.append(score)

	scores.sort()

	middle_index = int(len(scores) / 2) # Floors and converts to int for indexing
	middle_score = scores[middle_index]

	print(middle_score)


def parse(line):
	return list(line[:-1])


def is_incomplete(line):
	stack = []

	for char in line:
		if char in PAIRS:
			stack.append(char)
		else:
			if char != PAIRS[stack.pop()]:
				return False

	return True


def get_incomplete_line_score(line):
	stack = []

	for char in line:
		if char in PAIRS:
			stack.append(char)
		else:
			stack.pop()

	score = 0

	while len(stack) > 0:
		score *= 5
		score += POINTS[stack.pop()]

	return score


if __name__ == "__main__":
	PAIRS = {
		"(": ")",
		"[": "]",
		"{": "}",
		"<": ">"
	}

	POINTS = {
		"(": 1,
		"[": 2,
		"{": 3,
		"<": 4
	}

	main()