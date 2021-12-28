from collections import defaultdict


def main():
	amphipods, empty_spaces = parse()

	print(amphipods)
	print(empty_spaces)


def parse():
	amphipods = defaultdict(list)
	empty_spaces = []

	with open("../inputs/23.txt") as f:
		x = 0
		y = 0

		for line in f:
			line = line.rstrip()

			for character in line:
				coordinates = (x, y)

				if character not in "# ":
					if character == ".":
						empty_spaces.append(coordinates)
					else:
						amphipods[character].append(coordinates)

				x += 1

			y += 1
			x = 0

	return dict(amphipods), empty_spaces


if __name__ == "__main__":
	main()
