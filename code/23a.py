from collections import defaultdict


def main():
	positions = parse()
	print(positions)


def parse():
	positions = {
		"amphipods": defaultdict(list),
		"hallways": [],
		"doorways": [],
		"rooms": [],
	}

	unsorted_hallways = []

	with open("../inputs/23_example_1.txt") as f:
		x = 0
		y = 0

		for line in f:
			line = line.rstrip()

			for character in line:
				coordinates = (x, y)

				if character not in "# ":
					if character == ".":
						unsorted_hallways.append(coordinates)
					else:
						positions["amphipods"][character].append(coordinates)
						positions["rooms"].append(coordinates)

				x += 1

			y += 1
			x = 0

	# Filters out doorways from the unsorted hallways
	for unsorted_hallway_space in unsorted_hallways:
		below_unsorted_hallway_space = (unsorted_hallway_space[0], unsorted_hallway_space[1] + 1)

		if below_unsorted_hallway_space in positions["rooms"]:
			positions["doorways"].append(unsorted_hallway_space)
		else:
			positions["hallways"].append(unsorted_hallway_space)

	positions["amphipods"] = dict(positions["amphipods"])

	return positions


if __name__ == "__main__":
	main()
