import utils
from functools import reduce


def main():
	world = utils.parse("9", parse)

	# print(world)

	visited = [[False]*WIDTH for _ in range(HEIGHT)]

	# print(visited)

	basin_sizes = []

	for y in range(HEIGHT):
		for x in range(WIDTH):
			if is_low_point(world, x, y):
				stack = [[x, y]]
				basin_size = solve(world, visited, stack)
				basin_sizes.append(basin_size)

	basin_sizes.sort()
	three_largest_basins = basin_sizes[-3:]
	print(reduce(lambda a, b : a * b, three_largest_basins))


def parse(line):
	return list(map(int, list(line[:-1])))


def is_low_point(world, x, y):
	if y > 0 and world[y-1][x] <= world[y][x]: # Top edge
		return False
	if y + 1 < HEIGHT and world[y+1][x] <= world[y][x]: # Bottom edge
		return False

	if x > 0 and world[y][x-1] <= world[y][x]: # Left edge
		return False
	if x + 1 < WIDTH and world[y][x+1] <= world[y][x]: # Right edge
		return False

	return True


def solve(world, visited, stack):
	size = 0

	while len(stack) > 0:
		node = stack.pop()
		x, y = node
		# print(x, y)

		if not visited[y][x]:
			visited[y][x] = True

			size += 1
			# print(x, y)

			if y > 0 and world[y-1][x] >= world[y][x] and world[y-1][x] < 9: # Top edge
				stack.append([x, y - 1]) # Go up
			if y + 1 < HEIGHT and world[y+1][x] >= world[y][x] and world[y+1][x] < 9: # Bottom edge
				stack.append([x, y + 1]) # Go down

			if x > 0 and world[y][x-1] >= world[y][x] and world[y][x-1] < 9: # Left edge
				stack.append([x - 1, y]) # Go left
			if x + 1 < WIDTH and world[y][x+1] >= world[y][x] and world[y][x+1] < 9: # Right edge
				stack.append([x + 1, y]) # Go right

	return size


if __name__ == "__main__":
	WIDTH = 100
	HEIGHT = 100

	main()