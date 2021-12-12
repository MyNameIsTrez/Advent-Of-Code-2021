import utils

import numpy as np


def main():
	data = utils.parse("11", parse)

	width = len(data[0])
	height = len(data)

	world = tuple( (x, y) for y, row in enumerate(data) for x in range(len(row)) )

	print("Before any steps:")
	print_data(data)

	flashes = 0

	step = 0

	returned_flashes = 0

	while returned_flashes < width * height:
		step += 1

		returned_flashes = flash_all(data, width, height, world)
		flashes += returned_flashes

		print(f"After step {step}:")
		print_data(data)

	print(f"Flashes: {flashes}")
	print(f"The first step during which all octopuses flash: {step}")


def parse(line):
	return list(map(int, line[:-1]))


def print_data(data):
	print(np.array(data), end="\n" * 2)


def flash_all(data, width, height, world):
	flashed = [[False] * width for _ in range(height)]

	stack = []

	for point in world:
		stack.append(point)

	flashes = 0

	while len(stack) > 0:
		x, y = stack.pop()

		# data[y][x]
		if (x, y) in world and not flashed[y][x]:
			data[y][x] += 1

			if data[y][x] > 9:
				flashed[y][x] = True
				data[y][x] = 0
				flashes += 1

				for point in (
								(x-1, y-1),
								(x  , y-1),
								(x+1, y-1),

								(x-1, y  ),
								(x+1, y  ),

								(x-1, y+1),
								(x  , y+1),
								(x+1, y+1)
								):
					stack.append(point)

	return flashes


if __name__ == "__main__":
	STEPS = 100

	main()
