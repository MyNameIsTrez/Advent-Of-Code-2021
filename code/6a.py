import utils


def parse(line):
	return map(int, line.strip().split(","))


def update(fishes):
	for i in range(len(fishes)): # Enumerating fishes wouldn't work as appended values would also be enumerated
		if fishes[i] == 0:
			fishes[i] = 6
			fishes.append(8)
		else:
			fishes[i] -= 1 # fish -= 1 doesn't work


if __name__ == "__main__":
	days = 80

	fishes = utils.parse_line("6", parse)

	for i in range(days):
		update(fishes)

	print(len(fishes))
