import utils
from functools import reduce


def main():
	data = utils.parse(filename, parse)

	world = { (y, x): height for y, row in enumerate(data) for x, height in enumerate(row) }

	visited = { (y, x): False for y in range(HEIGHT) for x in range(WIDTH) }

	basin_sizes = []

	for point in world:
		if is_low_point(world, point):
			basin_size = get_basin_size(world, visited, point)
			basin_sizes.append(basin_size)

	basin_sizes.sort()
	three_largest_basins = basin_sizes[-3:]
	print(reduce(lambda a, b : a * b, three_largest_basins))


def parse(line):
	return list(map(int, list(line[:-1])))


def is_low_point(world, point):
	for neighbor in ( (point[0]-1, point[1]), (point[0]+1, point[1]), (point[0], point[1]-1), (point[0], point[1]+1) ):
		if neighbor in world and world[neighbor] <= world[point]:
			return False
	return True


def get_basin_size(world, visited, starting_point):
	stack = [starting_point]
	size = 0

	while len(stack) > 0:
		point = stack.pop()

		if not visited[point] and world[point] < 9:
			visited[point] = True

			size += 1

			for neighbor in ( (point[0]-1, point[1]), (point[0]+1, point[1]), (point[0], point[1]-1), (point[0], point[1]+1) ):
				if neighbor in world and world[neighbor] >= world[point]:
					stack.append(neighbor)

	return size


if __name__ == "__main__":
	filename = "9"
	WIDTH = 100
	HEIGHT = 100

	main()