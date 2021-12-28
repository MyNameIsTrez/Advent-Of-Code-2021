import copy

from collections import defaultdict


def main():
	amphipods, positions = parse()
	print(amphipods)
	print(positions)

	amphipods_copy = get_amphipods_copy(amphipods)
	amphipods_copy["A"].pop()
	print(amphipods_copy)
	print(amphipods)


def parse():
	amphipods = defaultdict(list)

	positions = {
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
						amphipods[character].append(coordinates)
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

	amphipods = dict(amphipods)

	return amphipods, positions


def get_amphipods_copy(amphipods):
	amphipods_copy = copy.deepcopy(amphipods)

	return amphipods_copy


if __name__ == "__main__":
	main()
