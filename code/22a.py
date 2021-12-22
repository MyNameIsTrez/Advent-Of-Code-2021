import utils


def main():
	data = parse()
	print(data)

	grid = get_empty_grid()
	# print(grid)

	for cuboid in data:
		update_grid(cuboid, grid)

	print(recursively_sum(grid))


def parse():
	data = []

	with open("../inputs/22.txt") as f:
		for line in f.readlines():
			state, coordinates = line.split()

			x_coordinates, y_coordinates, z_coordinates = coordinates.split(",")

			x_start, x_end = get_start_and_end(x_coordinates)
			y_start, y_end = get_start_and_end(y_coordinates)
			z_start, z_end = get_start_and_end(z_coordinates)

			if (x_start < MINIMUM_COORDINATE or x_end > MAXIMUM_COORDINATE or
				y_start < MINIMUM_COORDINATE or y_end > MAXIMUM_COORDINATE or
				z_start < MINIMUM_COORDINATE or z_end > MAXIMUM_COORDINATE
				):
				continue

			data.append({
				"state": True if state == "on" else False,
				"x_start": x_start, "x_end": x_end,
				"y_start": y_start, "y_end": y_end,
				"z_start": z_start, "z_end": z_end
			})

	return data


def get_start_and_end(coordinates):
	start_string, end_string = coordinates.split("..")
	start = int(start_string[2:])
	end = int(end_string)
	return start, end


def get_empty_grid():
	grid = []

	for z in range(COORDINATE_RANGE):
		grid.append([])
		for y in range(COORDINATE_RANGE):
			grid[z].append([False] * COORDINATE_RANGE)

	return grid


def update_grid(cuboid, grid):
	for z in range(cuboid["z_start"], cuboid["z_end"] + 1):
		for y in range(cuboid["y_start"], cuboid["y_end"] + 1):
			for x in range(cuboid["x_start"], cuboid["x_end"] + 1):
				grid[z][y][x] = cuboid["state"]


def recursively_sum(element):
	if type(element) == list:
		sub_elements_sum = 0
		for sub_element in element:
			sub_elements_sum += recursively_sum(sub_element)
		return sub_elements_sum
	else:
		return element


if __name__ == "__main__":
	MINIMUM_COORDINATE = -50
	MAXIMUM_COORDINATE = 50

	COORDINATE_RANGE = MAXIMUM_COORDINATE - MINIMUM_COORDINATE

	main()
